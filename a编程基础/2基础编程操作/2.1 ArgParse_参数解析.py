#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Time    : Oct 16, 2024 at 10:39:33
# @Author  : chenlongxu
# @Mail    : xuchenlong796@qq.com
#
# 描述 如何使用外部传入的参数来进行 Python 编程 
# 调用方法  python Scripts_coding.py --option sub --num1 12 --num2 14 --datetime 2024-10-16

import sys
import argparse

# argparse 是 Python 内置的一个用于命令行解析的模块
# 创建一个解析器对象
parser = argparse.ArgumentParser(description='Process some integers.')

# 添加输入参数，现在要求解析 option、datetime、num1、num2 四个参数
# 要求返回再当前日期下，num1 和 num2 两个数的和

# 添加 option 参数
parser.add_argument('--option', type=str, default='add', help='add or sub')
# 添加 datetime 参数
parser.add_argument('--datetime', type=str, default='2024-10-16', help='a date string')
# 添加 num1 参数
parser.add_argument('--num1', type=int, default=0, help='an integer')
# 添加 num2 参数
parser.add_argument('--num2', type=int, default=0, help='an integer')

# 解析参数
args = parser.parse_args()
if args.option == 'add':
    print(args.datetime)
    print(args.num1 + args.num2)
else:
    print(args.datetime)
    print(args.num1 - args.num2)

