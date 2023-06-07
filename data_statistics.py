import jieba
import json
import collections
import os
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
    input_file=open('./{}/{}_content.txt'.format(file,file),mode='r',encoding='utf-8')
    output_file=open('./{}/{}_words.txt'.format(file,file),mode='w',encoding='utf-8')

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
    f = open('./{}/{}.json'.format(file,file), encoding='utf-8')
    setting = json.load(f)  # 把json文件转化为python用的类型
    f.close()
    values=[]
    for i in range(len(setting)):
        my_value = setting[i]['{}'.format(key)]  # 提取元素中所需要的的值
        values.append(my_value)
    # print(values)
    f2=open("./{}/{}_content.txt".format(file,file),'w',encoding='utf-8')
    for line in values:
        f2.write(line+'\n')
    f2.close()
    # print(f2.name)


# 以下词频分析
def word_coll(file):
    with open('./dict/stop_words.txt',encoding='utf-8') as f:
        stop=f.readlines()
    stop=[x.strip() for x in stop]
    word_box=[]
    with open('./{}/{}_words.txt'.format(file,file),'r',encoding='utf-8') as wf,open('./{}/{}word_filtered.txt'.format(file,file),'w',encoding='utf-8') as wf2:
        for word in wf:
            word_box.extend(word.split(' '))
            filtered_woed_box=[x for x in word_box if x not in stop]
        results=collections.Counter(filtered_woed_box)
        for word in results:
            wf2.write(word+' ')
    print(collections.Counter(word_box).most_common(20))
    print(collections.Counter(filtered_woed_box).most_common(20))

if __name__=='__main__':
    jsontotxt('merge_comments','text')
    word_spli('merge_comments')
    word_coll('merge_comments')
