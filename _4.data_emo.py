# 中文情感分析
from cnsenti import Sentiment
from cnsenti import Emotion

senti = Sentiment(pos='positive.txt',  
                  neg='negative.txt', 
                  merge=True,  
                  encoding='utf-8')

emotion = Emotion()
words=[]
with open('无耻之徒_content.txt','r',encoding='utf-8') as f:
    text=f.read()
    for word in text:
        if word!='\n':
            words.append(word)
    # print(words)
    num_words = len(words)
    print(num_words)
    result = emotion.emotion_count(text)
    result2 = senti.sentiment_count(text)
    pos='{:3f}'.format(result2['pos']/num_words)
    neg='{:3f}'.format(result2['neg']/num_words)
    print(result)
    print(result2)
    print('pos:',pos,'neg:',neg)


# #  based on deep learning
# import random
# import pickle
# import nltk
# from nltk.tokenize import word_tokenize
# from nltk.stem import WordNetLemmatizer
# import numpy as np
# from collections import Counter

# lemmatizer=WordNetLemmatizer()
# def creat_lexicon(pos,neg):
#     # 根据输入的pos和neg文件，生成一个词典
#     # 词典用来将测试数据转换为数列
#     lexicon=[]

#     for fi in [pos,neg]:
#         with open(fi,'r',encoding='utf-8') as f:
#             contents=f.readlines()

#             # 每行文字小写化并分词加入词典
#             for l in contents:
#                 all_words=word_tokenize(l.lower())
#                 lexicon+=all_words
    
#     # 标准化词语
#     lexicon=[lemmatizer.lemmatize(i) for i in lexicon]

#     # 统计词频
#     w_counts=Counter(lexicon)

#     # 将词频处于50-1000的词语存入数组l2中，目的是去重
#     l2=[]
#     for w in w_counts:
#         if 1000>w_counts[w]>50:
#             l2.append(w)
    
#     # 输出词典长度，每行文字都会输出为与词典长度一致的二值编码
#     print(len(l2))
#     with open('lexicon.pickle','wb') as f:
#         pickle.dump(l2,f)
#     return l2

# def sample_handling(sample,lexicon,classification):
#     # 将数据根据词典编码
#     featureset=[]
#     with open(sample,'r',encoding='utf-8') as f:

#         contents=f.readlines()
#         for l in contents:
#             current_words=word_tokenize(l.lower())
#             current_words=[lemmatizer.lemmatize(i) for i in current_words]

#             # 初始化为0
#             features=np.zeros(len(lexicon))

#             # 根据词典编码
#             for word in current_words:
#                 if word.lower() in lexicon:
#                     index_value=lexicon.index(word.lower())
#                     features[index_value]+=1
#             # 编码后的结果放入featureset
#             features=list(features)
#             featureset.append([features,classification])
#     return featureset

# def creat_feature_sets_and_lables(pos,neg,test_size=0.1):
#     # 标准化输入数据并保存输出
#     lexicon=creat_lexicon(pos,neg)
#     features=[]
#     features+=sample_handling('pos.txt',lexicon,[1,0])
#     features+=sample_handling('neg.txt',lexicon,[0,1])

#     # 打乱输入数据
#     random.shuffle(features)
#     features=np.array(features)

#     # 计算10%测试数据的数据量
#     testing_size=int(test_size+len(features))

#     # 生成训练数据集
#     train_x=list(features[:,0][:-testing_size])
#     train_y=list(features[:,1][:-testing_size])

#     # 生成测试数据集
#     test_x=list(features[:,0][-testing_size: ])
#     test_y=list(features[:,1][-testing_size: ])

#     return train_x,train_y,test_x,test_y

# if __name__=='__main__':
#     train_x,train_y,test_x,test_y=creat_feature_sets_and_lables('positive.txt','negative.txt')
#     with open('sentiment_set.pickle','wb') as f:
#         pickle.dump([train_x,train_y,test_x,test_y],f)
