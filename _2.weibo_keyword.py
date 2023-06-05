import json
import requests
import time
url_template='http://m.weibo.cn/api/container/getIndex?type=wb&queryVal={}&containerid=100103type=2%26q%3D{}&page={}'

headers = {           
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
}

def fetch_data(query_val,page_id):
    resp=requests.get(url_template.format(query_val,query_val,page_id),headers=headers,verify=False)
    # print(resp.text)
    card_group=json.loads(resp.text)['data']['cards'][0]
    # print(card_group)
    print('url:',resp.url,'\n','---条数:',len(card_group))

    mblogs=[]  #保存处理过的微博

    mblog=card_group['mblog']
    # print(mblog)
    blog={
        'mid':mblog['id'],
        'text':mblog['text'],
        'time':mblog['created_at'],
        'userid':str(mblog['user']['id']),
        'username':mblog['user']['screen_name'],
        'reposts_count':mblog['reposts_count'],
        'comments_count':mblog['comments_count'],
        'attitudes_count':mblog['attitudes_count']
    }
    print(blog)
    time.sleep(0.5)
    mblogs.append(blog)
    return mblogs

def remove_dupli(mblogs):  #数据去重
    mid_set=[]
    new_blogs=[]
    for blog in mblogs:
        if blog['mid'] not in mid_set:
            new_blogs.append(blog)
            mid_set.append(blog['mid'])
    return new_blogs

def fetch_pages(query_val,page_num):
    mblogs=[]
    for page_id in range(page_num):
        try:
            mblogs.extend(fetch_data(query_val,page_id))
        except Exception as e:
            print(e)
            
    
    print("去重前",len(mblogs))
    mblogs=remove_dupli(mblogs)
    print("去重后",len(mblogs))

    # 保存至 result.json中
    with open('{}.json'.format(query_val),'w',encoding='utf-8', newline='\n') as f:
        data=json.dump(mblogs,f,ensure_ascii=False,indent=1)
        print("已经保存至{}.json".format(query_val))


if __name__=='__main__':
    fetch_pages('无耻之徒',50)


