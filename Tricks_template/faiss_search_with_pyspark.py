#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 Tencent, Inc. All Rights Reserved
#
"""
File: faiss_search_with_pyspark.py
Author: shileicao (eliasslcao@tencent.com)
Date: 2021-1-27 17:06:19
"""

import argparse
import json
import numpy as np
import time
import tempfile
import os
import tarfile
import glob

import faiss
from pyspark.sql import SparkSession

from HadoopUtil import HadoopUtil


def search_by_index(search_topk, nprobe, search_which_user):
    def map_partitions_search(data):
        with open(glob.glob('id2device_id/tmp/*')[0], 'r') as f:
            train_id2device_id = json.load(f)

        if search_which_user == 'search_new_user':
            dt = [[x[0].strip(), list(map(float, x[1].strip().split(' ')))] for x in data]
            search_id2device_id1 = [x[0] for x in dt]
            embedding = np.asarray([x[1] for x in dt], np.float32)
        elif search_which_user == 'search_old_user':
            dt = [[x[0].strip(), x[1].strip(), x[2].strip(), list(map(float, x[-1].strip().split(' ')))] for x in data]
            search_id2device_id2 = [[x[0], x[1], x[2]] for x in dt]
            embedding = np.asarray([x[-1] for x in dt], np.float32)
        index = faiss.read_index(glob.glob('index/tmp/*')[0])
        index.verbose = True
        index.nprobe = nprobe
        faiss.normalize_L2(embedding)
        D, I = index.search(embedding, search_topk)

        u2u_results = []
        if search_which_user == 'search_new_user':
            for ii, device_id in enumerate(search_id2device_id1):
                u2u_results.append(
                    '\t'.join(
                        [device_id] + ['##'.join(train_id2device_id[int(train_index)]) for train_index in I[ii]]))
        elif search_which_user == 'search_old_user':
            for ii, account_info in enumerate(search_id2device_id2):
                u2u_results.append(
                    '\t'.join(
                        account_info + ['##'.join(train_id2device_id[int(train_index)]) for train_index in I[ii]]))
        return u2u_results
    return map_partitions_search


def search_new_user_by_faiss(hdfs_path, nprobe, u2u_path, search_topk):
    spark = (SparkSession
             .builder.
             appName("faiss search on new user").
             enableHiveSupport().
             getOrCreate())
    spark.conf.set("spark.sql.execution.arrow.enabled", "true")
    sc = spark.sparkContext

    embedding_rdd = (sc.textFile(hdfs_path)
                     .map(lambda x: (x.split("\t")[0], x.split("\t")[1])))

    u2u_rdd = embedding_rdd.mapPartitions(search_by_index(search_topk, nprobe, 'search_new_user'))
    print(u2u_rdd.count())
    print(u2u_rdd.take(5))
    u2u_rdd.saveAsTextFile(u2u_path)


def search_old_user_by_faiss(hdfs_path, nprobe, u2u_path, search_topk):
    spark = (SparkSession
             .builder.
             appName("faiss search on new user").
             enableHiveSupport().
             getOrCreate())
    spark.conf.set("spark.sql.execution.arrow.enabled", "true")
    sc = spark.sparkContext

    embedding_rdd = (sc.textFile(hdfs_path)
                     .map(lambda x: (x.split("\t")[0], x.split("\t")[1], x.split("\t")[2], x.split("\t")[3])))

    total_count = embedding_rdd.count()
    u2u_rdd = (embedding_rdd
               .sample(False, 2000000./total_count, 0)
               .mapPartitions(search_by_index(search_topk, nprobe, 'search_old_user')))
    print(u2u_rdd.count())
    print(u2u_rdd.take(5))
    u2u_rdd.saveAsTextFile(u2u_path)


def tar_gz_and_copy_to_hafs(sc, local_path, dest_path):
    if HadoopUtil.file_exists(sc, dest_path):
        HadoopUtil.delete_file(sc, dest_path)

    tmp_file = tempfile.NamedTemporaryFile(delete=True)
    tmp_file.close()

    with tarfile.open(tmp_file.name, "w:gz") as t:
        t.add(local_path)

    HadoopUtil.upload_file(sc, tmp_file.name, dest_path)


def train_faiss(hdfs_path, index_str, use_gpu):
    start_time = time.time()
    spark = (SparkSession
             .builder.
             appName("faiss search on new user").
             enableHiveSupport().
             getOrCreate())
    spark.conf.set("spark.sql.execution.arrow.enabled", "true")
    sc = spark.sparkContext
    old_user_embedding = (sc.textFile(hdfs_path)
                          .map(lambda x: (x.split("\t")[0], x.split("\t")[1], x.split("\t")[2], x.split("\t")[3]))
                          .collect())
    id2device_id = []
    embeddings = []
    for row in old_user_embedding:
        id2device_id.append([row[0].strip(), row[1].strip(), row[2].strip()])
        embeddings.append(list(map(float, row[-1].strip().split(' '))))
    embeddings = np.asarray(embeddings, np.float32)
    faiss.normalize_L2(embeddings)
    print("embedding shape : %s" % str(embeddings.shape))

    try_num = 3
    run_success = False
    while try_num > 0 and not run_success:
        try:
            tmp_file = tempfile.NamedTemporaryFile(delete=True)
            tmp_file.close()
            with open(tmp_file.name, 'w+') as f:
                json.dump(id2device_id, f)

            id2device_id_save_path = os.path.join(os.path.split(os.path.split(hdfs_path)[0])[0],
                                                  'data', 'id2device_id-32d.tar.gz')

            tar_gz_and_copy_to_hafs(sc, tmp_file.name, id2device_id_save_path)
            run_success = True
        except:
            try_num -= 1

    if try_num == 0 and run_success is False:
        raise ValueError("run failed for id2device_id")

    ss = time.time()
    index = faiss.index_factory(32, index_str)
    if use_gpu:
        index_ivf = faiss.extract_index_ivf(index)
        clustering_index = faiss.index_cpu_to_all_gpus(faiss.IndexFlatL2(32))
        index_ivf.clustering_index = clustering_index
    ee = time.time()
    print("-create index costs time: %3.2f" % (ee - ss))
    index.verbose = True
    assert not index.is_trained
    ss = time.time()
    index.train(embeddings if embeddings.shape[0] <= 8000000 else embeddings[:8000000, :])
    ee = time.time()
    print("-train model costs time: %3.2f" % (ee - ss))

    assert index.is_trained

    ss = time.time()
    index.add(embeddings)  # add may be a bit slower as well
    ee = time.time()
    print("-add data costs time: %3.2f" % (ee - ss))

    try_num = 3
    run_success = False
    while try_num > 0 and not run_success:
        try:

            tmp_file = tempfile.NamedTemporaryFile(delete=True)
            tmp_file.close()
            faiss.write_index(index, tmp_file.name)

            index_save_path = os.path.join(
                os.path.split(os.path.split(hdfs_path)[0])[0], 'data', 'index-32d.tar.gz')

            tar_gz_and_copy_to_hafs(sc, tmp_file.name, index_save_path)
            run_success = True
        except:
            try_num -= 1

    if try_num == 0 and run_success is False:
        raise ValueError("run failed for index")

    end_time = time.time()
    print("costs time: %3.2f\n\n" % (end_time - start_time))


def arg_parser():
    parser = argparse.ArgumentParser(prog='faiss_train_and_search',
                                     formatter_class=argparse.RawTextHelpFormatter,
                                     description='faiss search (recall by u2u similarity)')

    parser.add_argument(
        '--index_str',
        dest='index_str',
        default='IVF65536_HNSW32,PQ32x4fs,RFlat',
        type=str,
        help='index str for choosing index'
    )

    parser.add_argument(
        '--nprobe',
        dest='nprobe',
        default=10,
        type=int,
        help='nprobe number for searching'
    )

    parser.add_argument(
        '--process_which',
        dest='process_which',
        default='train',
        type=str,
        choices=['train', 'search_new_user', 'search_old_user'],
        help='process which task'
    )

    parser.add_argument(
        '--hdfs_path',
        dest='hdfs_path',
        default='',
        type=str,
        help=''
    )

    parser.add_argument(
        '--search_topk',
        dest='search_topk',
        default=10,
        type=int,
        help=''
    )

    parser.add_argument(
        '--u2u_path',
        dest='u2u_path',
        default='',
        type=str,
        help=''
    )

    parser.add_argument(
        '--use_gpu',
        dest='use_gpu',
        action='store_true',
    )

    return parser


def main():
    parser = arg_parser()
    args = parser.parse_args()

    if args.process_which == 'search_new_user':
        search_new_user_by_faiss(args.hdfs_path, args.nprobe, args.u2u_path, args.search_topk)
    elif args.process_which == 'train':
        train_faiss(args.hdfs_path, args.index_str, args.use_gpu)
    elif args.process_which == 'search_old_user':
        search_old_user_by_faiss(args.hdfs_path, args.nprobe, args.u2u_path, args.search_topk)


if __name__ == '__main__':
    main()
