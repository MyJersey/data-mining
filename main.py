import weibo_keyword as wk
import data_statistics as ds
import data_emo as de
import word_cloud_visual as wc
import time_visual as tv

# 获取数据
wk.fetch_data('巴赫穆特',100)

# 统计数据
ds.jsontotxt('巴赫穆特','text')
ds.word_spli('巴赫穆特')
ds.word_coll('巴赫穆特')

# 情感分析
de.emo_analysis('巴赫穆特')

# 可视化
wc.cloud_visual('巴赫穆特')
tv.time_visual('巴赫穆特')
