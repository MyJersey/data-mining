import requests
import json
from fake_useragent import UserAgent
import time
import numpy as np
url_template='https://m.weibo.cn/comments/hotflow?id={}&mid={}&max_id_type=0'
headers = {           
    'User-Agent': UserAgent().random,
}

def remove_dupli(all_comments):  #数据去重
    mid_set=[]
    new_comsets=[]
    for com in all_comments:
        if com['mid'] not in mid_set:
            new_comsets.append(com)
            mid_set.append(com['mid'])
    return new_comsets

def fetch_comment(file):

    with open('./{}/{}.json'.format(file,file),'r',encoding='utf-8') as f:
        weibo=json.load(f)
        all_comments=[]
        for i in range(len(weibo)):
            try:
                id=weibo[i]['mid']
                url=url_template.format(id,id)
                resp=requests.get(url,headers=headers,verify=False)
                # print(json.loads(resp.text)['data']['data'])
                if 'data' in json.loads(resp.text):
                    each_weibo=json.loads(resp.text)['data']['data']
                    print(each_weibo)
                    time.sleep(np.random.random())
                    for j in range(len(each_weibo)):
                        comment={
                            'mid':each_weibo[j]['id'],
                            'text':each_weibo[j]['text'],
                            'time':each_weibo[j]['created_at'],
                            'userid':str(each_weibo[j]['user']['id']),
                            'source':each_weibo[j]['source'],
                            }
                        all_comments.append(comment)
            except Exception as e:
                print(e)
                continue
        
        print("over!!")
        return all_comments

def fetch_pages(file):
    all_comments=fetch_comment(file)
    print("去重前",len(all_comments))
    all_comments=remove_dupli(all_comments)
    print("去重后",len(all_comments))
    with open("./{}/{}_comments.json".format(file,file),mode="w",encoding="utf-8") as f1:
        json.dump(all_comments,f1,ensure_ascii=False,indent=1)

if __name__=='__main__':
    fetch_pages('merge')