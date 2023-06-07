import jieba
import json
import collections
import os
import csv
# 以下jieba分词分析
# 判断是否是中文字符
def is_chinese(uchar):
    if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
        return True
    else:
        return False

# 格式化微博正文
def format_str(content):
    content_str=''
    for i in content:
        if is_chinese(i):
            # print(i)
            content_str=content_str+i
    return content_str

# 分别打开输入输出文本文件
def word_spli(file):
    input_file=open('./merge/{}_content.txt'.format(file),mode='r',encoding='utf-8')
    output_file=open('./merge/{}_words.txt'.format(file),mode='w',encoding='utf-8')

    # 对每行数据进行中文字符判断格式化
    filelines=input_file.readlines()
    for line in filelines:
        # print(line)
        line=format_str(line)
        # print(line)
        seg_list=jieba.cut(line)
        words=' '.join(seg_list)
        output_file.write(words)

    input_file.close()
    output_file.close()



# 读取json文件的内容并存为txt
def jsontotxt(file,key):
    """提取所需元素的方法"""
    # isExists=os.path.exists(file)
    # if not isExists:
    #     os.makedirs(file)
    f = open('./merge/{}.json'.format(file), encoding='utf-8')
    setting = json.load(f)  # 把json文件转化为python用的类型
    f.close()
    values=[]
    for i in range(len(setting)):
        my_value = setting[i]['{}'.format(key)]  # 提取元素中所需要的的值
        values.append(my_value)
    # print(values)
    f2=open("./merge/{}_content.txt".format(file),'w',encoding='utf-8')
    for line in values:
        f2.write(line+'\n')
    f2.close()
    # print(f2.name)


# 以下词频分析
def word_coll(file,filter=[]):
    with open('./dict/stop_words.txt',encoding='utf-8') as f:
        stop=f.readlines()
    stop=[x.strip() for x in stop]
    for i in range(len(filter)):
        stop.append(filter[i])
    # print(stop)
    word_box=[]
    with open('./merge/{}_words.txt'.format(file),'r',encoding='utf-8') as wf,open('./merge/{}word_filtered.txt'.format(file),'w',encoding='utf-8') as wf2:
        for word in wf:
            word_box.extend(word.split(' '))
            filtered_woed_box=[x for x in word_box if x not in stop]
        results=collections.Counter(filtered_woed_box)
        for word in results:
            wf2.write(word+' ')
        word_count=collections.Counter(word_box).most_common(30)
        filtered_word_count=collections.Counter(filtered_woed_box).most_common(30)
        print(word_count)
        print(filtered_word_count)
    with open('./merge/{}_word_counts.csv'.format(file),'w',encoding='utf-8',newline='') as ff:
        csvwriter=csv.writer(ff)
        csvwriter.writerow(('过滤前','数量'))
        for i in range(len(word_count)):
            csvwriter.writerow(word_count[i])
    with open('./merge/{}_flitered_word_counts.csv'.format(file),'w',encoding='utf-8',newline='') as ff2:
        csvwriter=csv.writer(ff2)
        csvwriter.writerow(('过滤后','数量'))
        for j in range(len(filtered_word_count)):
            csvwriter.writerow(filtered_word_count[j])
if __name__=='__main__':
    jsontotxt('merge_comments','text')
    word_spli('merge_comments')
    filter=['俄乌','冲突','巴赫','穆特','俄罗斯','乌克兰','微博','俄','乌']
    word_coll('merge_comments',filter)
