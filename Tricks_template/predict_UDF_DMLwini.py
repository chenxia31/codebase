import warnings
warnings.filterwarnings('ignore')
import causalml
import os, sys, time, argparse, pickle
from pytoolkit import TDWSQLProvider
from pyspark.sql import SparkSession
import pandas as pd 
import numpy as np
from causalml.inference.meta import LRSRegressor
from sklearn.model_selection import train_test_split
from causalml.inference.meta import BaseXRegressor,  BaseRRegressor, BaseSRegressor,BaseTRegressor
from causalml.inference.meta import XGBTRegressor
from sklearn.model_selection import train_test_split
import pandas as pd
# test for pandas_udf
import numpy as np
import pandas as pd
import os, sys, time, argparse, pickle
from datetime import date, timedelta, datetime
import os
import math
from pyspark.sql.functions import col
from pyspark.sql import functions as F
from pyspark.sql import types
#from pyspark.sql import udf
from pyspark.sql.functions import udf
from pyspark.sql.functions import pandas_udf, PandasUDFType
import matplotlib.pyplot as plt


# config for the spark session
user_name = "tdw_lydialiuliu"
psw = "19950429"
db = 'wxg_finder_ds'

os.environ['GROUP_ID'] = 'g_wxg_wxt_g_wxg_weixin_emoticon'
os.environ['GAIA_ID'] = '5729'
os.environ['PYSPARK_PYTHON'] = 'pythonenv/python3.6/bin/python3.6'

python_pkg = "hdfs://ss-wxg-11-v2/data/SPARK/WXG/g_wxg_wxt_product_analytics/tdw_vinyxzhao/envs/vinpython3.6v2.tar.gz"

spark = SparkSession \
    .builder \
    .appName("PythonPi") \
    .config("spark.pyspark.driver.python", "python3.6") \
    .config("spark.pyspark.python", "pythonenv/python3.6/bin/python3.6") \
    .config("spark.yarn.dist.archives", "%s#pythonenv" % python_pkg) \
    .config("spark.driver.memory", "8g") \
    .config("spark.executor.memory", "16g") \
    .config("spark.driver.maxResultSize", "4g") \
    .getOrCreate()

provider = TDWSQLProvider(spark, user_name, psw, db = db, group='同乐')


# loaded_model
if len(sys.argv) > 1:
    print("params:{}".format(sys.argv[1]))
    ds = sys.argv[1]
else:
    yesterday = datetime.today() + timedelta(-1)
    ds = yesterday.strftime('%Y%m%d')
print("curr_datestr:{}".format(ds))
ds = int(ds)

print('STEP1:get the samples')
tb_feat = 'dws_promotion_voucher_finderuin_exp_di'
provider.table(tb_feat,priParts = ['p_'+str(ds)]).createOrReplaceTempView(tb_feat)
input_sql = 'SELECT * FROM dws_promotion_voucher_finderuin_exp_di  where ds = '+str(ds)+" "
sdf = spark.sql(input_sql)

print('STEP2:config the loaded model')
model_name = 'DMLWINI'
group_name = 'A'     
new_model_name = 'DMLXGB1.pkl'
sdf = sdf.fillna(0)
with open(new_model_name, 'rb') as f:
    loaded_model = pickle.load(f)

print('STEP3: spark.pandas_UDF')
output_schema = 'ds long,uin long,lift_value double,model_name string,group_name string'
@pandas_udf(output_schema, PandasUDFType.GROUPED_MAP)
def model_predict(df):
    # loaded trained model
    import os
    os.environ["ARROW_PRE_0_15_IPC_FORMAT"] = "1"
    # Define the feature name
    feature_names = ['use_lifecycle', 'promotion_cnt_1d', 'promotion_cnt_1d_7d', 'promotion_cnt_8d_14d', 'promotion_cnt_15d_21d', 'promotion_cnt_22d_28d', 'cost_1d', 'cost_1d_7d', 'cost_8d_14d', 'cost_15d_21d', 'cost_22d_28d', 'home_expose_cnt', 
                 'create_order_cnt', 'confirm_order_cnt', 'place_order_cnt', 'pay_order_cnt', 'total_operate_score', 'post_cnt', 'post_acc7d_cnt', 'post_acc30d_cnt', 'stay_cnt', 'stay_acc7d_cnt', 'stay_acc30d_cnt', 'category_lv1', 'native_type_detailed',
                 'ad_acc30d_income', 'xrw_income_30d', 'ad_comment_income_30d_yuan', 'vip_income_30d', 'order_commission_2_acc30d', 'self_sale_order_gmv_acc30d', 'profile_order_commission_2_acc30d', 'self_sale_profile_order_gmv_acc30d', 
                 'live_gift_acc30d_income_yuan', 'live_fenxiao_commission_acc30d', 'live_self_sale_gmv_acc30d', 'lifecycle_level', 'auth_icon_type', 'if_invite', 'fsex', 'fage_level', 'is_weishang', 'most_content_tag', 'fans_acc7d_cnt', 
                 'fans_acc30d_cnt', 'self_forward_acc30d_cnt', 'self_singleforward_acc30d_cnt', 'self_groupforward_acc30d_cnt', 'self_snsforward_acc30d_cnt', 'self_like_svr_acc30d_cnt', 'self_unlike_svr_acc30d_cnt', 'self_nointerest_svr_acc30d_cnt', 
                 'self_comment_svr_acc30d_cnt', 'self_reply_svr_acc30d_cnt', 'self_delcomment_svr_acc30d_cnt', 'self_likecomment_svr_acc30d_cnt', 'self_unlikecomment_svr_acc30d_cnt', 'self_fav_svr_acc30d_cnt', 'self_unfav_svr_acc30d_cnt', 
                 'self_forward_acc7d_cnt', 'self_singleforward_acc7d_cnt', 'self_groupforward_acc7d_cnt', 'self_snsforward_acc7d_cnt', 'self_like_svr_acc7d_cnt', 'self_unlike_svr_acc7d_cnt', 'self_nointerest_svr_acc7d_cnt', 'self_comment_svr_acc7d_cnt',
                 'self_reply_svr_acc7d_cnt', 'self_delcomment_svr_acc7d_cnt', 'self_likecomment_svr_acc7d_cnt', 'self_unlikecomment_svr_acc7d_cnt', 'self_fav_svr_acc7d_cnt', 'self_unfav_svr_acc7d_cnt', 'liveid_cnt', '7d_liveid_cnt', '30d_liveid_cnt',
                 'selfprofile_visit_cnt', 'otherprofile_visit_cnt', 'center_visit_cnt', 'reddot_center_visit_cnt', 'is_bizuin', 'area_in_post_rate', 'area_in_allarea_rate', 'if_mcnid', 'pr_score_rank', 'douyin_fans_cnt', 'ks_fans_cnt', 'bi_fans_cnt',
                 'weibo_fans_cnt', 'generated_content_type', 'is_have_post_good_permission', 'creator_center_vv', 'reddot_creator_center_vv', 'creator_service_vv', 'data_center_vv', 'commodity_post_1d_cnt', 'commodity_post_3d_cnt', 'commodity_post_7d_cnt',
                 'commodity_post_14d_cnt', 'commodity_post_30d_cnt', 'post_acc_cnt_at_1k_fans', 'rd_expose_cnt_left', 'rd_click_cnt_left', 'sphnews_expose_cnt', 'sphnews_click_cnt', 'out_fans_cnt', 'post_operate_score', 'account_operate_score', 
                 'interact_operate_score', 'income_operate_score', 'if_hx_valid', 'if_vertical']

    feature_name_dummies = ['promotion_cnt_1d', 'promotion_cnt_1d_7d', 'promotion_cnt_8d_14d', 'promotion_cnt_15d_21d', 'promotion_cnt_22d_28d', 'cost_1d', 'cost_1d_7d', 'cost_8d_14d', 'cost_15d_21d', 'cost_22d_28d', 'home_expose_cnt', 'create_order_cnt',
                        'confirm_order_cnt', 'place_order_cnt', 'pay_order_cnt', 'total_operate_score', 'post_cnt', 'post_acc7d_cnt', 'post_acc30d_cnt', 'stay_cnt', 'stay_acc7d_cnt', 'stay_acc30d_cnt', 'ad_acc30d_income', 'xrw_income_30d',
                        'ad_comment_income_30d_yuan', 'vip_income_30d', 'order_commission_2_acc30d', 'self_sale_order_gmv_acc30d', 'profile_order_commission_2_acc30d', 'self_sale_profile_order_gmv_acc30d', 'live_gift_acc30d_income_yuan', 
                        'live_fenxiao_commission_acc30d', 'live_self_sale_gmv_acc30d', 'auth_icon_type', 'fsex', 'is_weishang', 'fans_acc7d_cnt', 'fans_acc30d_cnt', 'self_forward_acc30d_cnt', 'self_singleforward_acc30d_cnt', 'self_groupforward_acc30d_cnt',
                        'self_snsforward_acc30d_cnt', 'self_like_svr_acc30d_cnt', 'self_unlike_svr_acc30d_cnt', 'self_nointerest_svr_acc30d_cnt', 'self_comment_svr_acc30d_cnt', 'self_reply_svr_acc30d_cnt', 'self_delcomment_svr_acc30d_cnt',
                        'self_likecomment_svr_acc30d_cnt', 'self_unlikecomment_svr_acc30d_cnt', 'self_fav_svr_acc30d_cnt', 'self_unfav_svr_acc30d_cnt', 'self_forward_acc7d_cnt', 'self_singleforward_acc7d_cnt', 'self_groupforward_acc7d_cnt', 
                        'self_snsforward_acc7d_cnt', 'self_like_svr_acc7d_cnt', 'self_unlike_svr_acc7d_cnt', 'self_nointerest_svr_acc7d_cnt', 'self_comment_svr_acc7d_cnt', 'self_reply_svr_acc7d_cnt', 'self_delcomment_svr_acc7d_cnt', 
                        'self_likecomment_svr_acc7d_cnt', 'self_unlikecomment_svr_acc7d_cnt', 'self_fav_svr_acc7d_cnt', 'self_unfav_svr_acc7d_cnt', 'liveid_cnt', '7d_liveid_cnt', '30d_liveid_cnt', 'selfprofile_visit_cnt', 'otherprofile_visit_cnt', 
                        'center_visit_cnt', 'reddot_center_visit_cnt', 'is_bizuin', 'area_in_post_rate', 'area_in_allarea_rate', 'if_mcnid', 'pr_score_rank', 'douyin_fans_cnt', 'ks_fans_cnt', 'bi_fans_cnt', 'weibo_fans_cnt', 'is_have_post_good_permission', 
                        'creator_center_vv', 'reddot_creator_center_vv', 'creator_service_vv', 'data_center_vv', 'commodity_post_1d_cnt', 'commodity_post_3d_cnt', 'commodity_post_7d_cnt', 'commodity_post_14d_cnt', 'commodity_post_30d_cnt', 
                        'post_acc_cnt_at_1k_fans', 'rd_expose_cnt_left', 'rd_click_cnt_left', 'sphnews_expose_cnt', 'sphnews_click_cnt', 'out_fans_cnt', 'post_operate_score', 'account_operate_score', 'interact_operate_score', 'income_operate_score', 
                        'if_hx_valid', 'if_vertical', 'use_lifecycle_0', 'use_lifecycle_尝试探索期', 'use_lifecycle_新增', 'use_lifecycle_沉默', 'use_lifecycle_沉默复活', 'use_lifecycle_流失', 'use_lifecycle_流失复活', 'category_lv1_0', 'category_lv1_VLOG',
                        'category_lv1_三农', 'category_lv1_二次元', 'category_lv1_亲子', 'category_lv1_人文艺术', 'category_lv1_体育', 'category_lv1_健康', 'category_lv1_公益', 'category_lv1_军事', 'category_lv1_剧情', 'category_lv1_历史', 'category_lv1_娱乐',
                        'category_lv1_宗教', 'category_lv1_宠物', 'category_lv1_影视综', 'category_lv1_情感', 'category_lv1_搞笑', 'category_lv1_摄影', 'category_lv1_收藏', 'category_lv1_教育', 'category_lv1_旅行', 'category_lv1_无法分类', 'category_lv1_时尚', 
                        'category_lv1_汽车', 'category_lv1_法律', 'category_lv1_游戏', 'category_lv1_生活', 'category_lv1_短剧', 'category_lv1_社会', 'category_lv1_科学科普', 'category_lv1_科技', 'category_lv1_美妆', 'category_lv1_美食', 'category_lv1_职场',
                        'category_lv1_舞蹈', 'category_lv1_财经', 'category_lv1_音乐', 'category_lv1_颜值', 'native_type_detailed_0', 'native_type_detailed_双栖-站外优势', 'native_type_detailed_双栖-站外粉丝未知', 'native_type_detailed_双栖-视频号优势', 
                        'native_type_detailed_无法识别', 'native_type_detailed_纯原生', 'lifecycle_level_0', 'lifecycle_level_持续活跃', 'lifecycle_level_新增', 'lifecycle_level_未知', 'lifecycle_level_沉默', 'lifecycle_level_沉默复活', 
                        'lifecycle_level_活跃沉默', 'lifecycle_level_流失', 'lifecycle_level_流失复活', 'if_invite_0', 'if_invite_邀请作者', 'if_invite_非邀请作者', 'fage_level_0', 'fage_level_fage_01_11', 'fage_level_fage_12_17', 'fage_level_fage_18_24', 
                        'fage_level_fage_25_29', 'fage_level_fage_30_34', 'fage_level_fage_35_39', 'fage_level_fage_40_44', 'fage_level_fage_45_49', 'fage_level_fage_50_54', 'fage_level_fage_55_59', 'fage_level_fage_60_70', 'fage_level_fage_70+', 
                        'fage_level_unknow', 'most_content_tag_0', 'most_content_tag_二次元', 'most_content_tag_动物', 'most_content_tag_工业/机械/施工', 'most_content_tag_影视综艺', 'most_content_tag_情感', 'most_content_tag_才艺', 'most_content_tag_搞笑',
                        'most_content_tag_新闻资讯', 'most_content_tag_旅行风景', 'most_content_tag_时尚', 'most_content_tag_明星名人', 'most_content_tag_游戏', 'most_content_tag_生活', 'most_content_tag_生活技巧', 'most_content_tag_知识', 
                        'most_content_tag_科技', 'most_content_tag_美食', 'most_content_tag_育儿', 'most_content_tag_舞蹈', 'most_content_tag_萌娃', 'most_content_tag_萌宠', 'most_content_tag_车', 'most_content_tag_运动', 'most_content_tag_音乐', 
                        'generated_content_type_0', 'generated_content_type_PGC', 'generated_content_type_UGC']
    
    from econml.dml import CausalForestDML
    from xgboost import XGBRegressor

    # get the dataset
    X_i_pre = pd.get_dummies(df[feature_names])
    X_i = pd.DataFrame({
        i: X_i_pre[i] if i in X_i_pre.columns else 0
        for i in feature_name_dummies
    })
    # get the predict output
    cate_i = loaded_model.effect(X_i, T0=0, T1=1)

    df['lift_value'] = cate_i # double
    df['model_name'] = model_name # string
    df['group_name'] = group_name # string
    df['ds'] = ds 
    return  df[['ds','uin','lift_value','model_name','group_name']]

sdf = sdf.withColumn("random_int", (F.rand() * 100).cast("integer"))
output = sdf.groupby(['random_int']).apply(model_predict)
output = output.select(['ds','uin','lift_value','model_name','group_name'])
# top5%
quantile = output.approxQuantile("lift_value", [0.85], 0.001)[0]
print(quantile)
output = output.withColumn("promotion_label", F.when(col("lift_value") >= quantile, F.lit(1)).otherwise(F.lit(0)))

# 写入到对应的分区
def create_partition(table_name, partition, partition_val, dbName="wxg_finder_ds"):
    # 更新TDW账号和密码：http://tdw.oa.com/register/update_account
    tdw = TDWUtil(user="tdw_lydialiuliu", passwd="19950429", dbName=dbName)
    if not tdw.partitionExist(table_name, partition):
        print('create partition: {}'.format(partition))
        tdw.createListPartition(table_name, partition, partition_val)
    else:
        print('skip create partition: {}, as it already existed'.format(partition))
    return
print('STEP4: save to table')
from pytoolkit import TDWUtil
output_table_name = 'dws_promotion_voucher_finderuin_exp_uplift_ds_result_di'
create_partition(output_table_name, 'p_'+str(ds), str(ds))
provider.saveToTable(output, output_table_name, priPart = 'p_'+str(ds), overwrite = True)