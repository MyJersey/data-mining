import json,sys
import pandas as pd
import matplotlib.pyplot as plt
import pickle
from datetime import datetime


df=pd.DataFrame(columns=['month','day','senti_pos','senti_neg'])
i=0
def time_visual(file):
    global datetime
    global df
    with open('./{}/{}.json'.format(file,file),encoding='utf-8') as f:
        # print(json.load(f))
        data=json.load(f)
        for i in range(len(data)):
            # data=json.loads(line)
            date=data[i]['time'][4:11] + data[i]['time'][26:30]
            datetime=datetime.strptime(date,'%b %d %Y')
            month=datetime.month
            day=datetime.day
            senti_pos=float(data[i]['senti_score']['pos'])
            senti_neg=float(data[i]['senti_score']['neg'])
            df=df.append({'month':month,'day':day,'senti_pos':senti_pos,'senti_neg':senti_neg},ignore_index=True)

    # 检查数据
    print(df.head())
    print(df.describe())

    with open('data.pickle','wb') as f:
        pickle.dump(df,f)

    df=pickle.load(open("data.pickle","rb"))

    # 绘制序列
    mean_sentiment_pos=df.groupby(['month','day'])['senti_pos'].mean()
    mean_sentiment_neg=df.groupby(['month','day'])['senti_neg'].mean()
    # print(mean_sentiment_pos)
    fig=plt.figure()
    mean_sentiment_pos.plot(kind='line')
    mean_sentiment_neg.plot(kind='line')
    fig.tight_layout()
    plt.legend(loc="upper left")
    plt.ylabel('SENTIMENT')
    plt.xlabel('DATE')
    plt.show()

if __name__=='__main__':
    time_visual('巴赫穆特')