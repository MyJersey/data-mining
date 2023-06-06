# 等待开放平台认证、、、


# from weibo import APIClient
# import urllib.request,json
# # 获取注册应用的APP_KEY AND APP_SECRET，并配置REDIRECT_URL
# API_KEY='3896047542'
# API_SECRET='2a2f320195b4e4c8c065c47ee2a55591'
# REDIRECT_URL='http://www.sina.com.cn'

# # 获取授权码
# c= APIClient(API_KEY,API_SECRET,REDIRECT_URL)
# url=c.get_authorize_url()
# print(url)

# # 利用授权码获取token
# code='769766ecac9c509e9962f846580d4d77'
# # host=url+'&code=769766ecac9c509e9962f846580d4d77'
# # response = requests.get(host,verify=False)
# # print(response)
# token=c.request_access_token(code)
# # 得到token
# token={}

# # 查找用户资料
# c2=APIClient(API_KEY,API_SECRET,REDIRECT_URL,token)
# user=c2.get('users/show',screen_name="papi酱")
# print(user)

# # 获取自己发过的所有微博
# posted_weibos=c2.get('statuses/user_timeline')['statuses']
# for weibo in posted_weibos:
#     print(weibo['text'])

# # https://m.weibo.cn/api/container/getIndex?type=uid&value=()&containerid=()&page=()
#   https://m.weibo.cn/api/container/getIndex?type=wb&queryVal={keyword}&containerid=100103type=2%26q%3D{keyword}&page={pageNumber}

# 根据微博名获取用户ID
# def get_id(user):
#     API_KEY='3896047542'
#     API_SECRET='2a2f320195b4e4c8c065c47ee2a55591'
#     REDIRECT_URL='http://www.sina.com.cn'
#     token={}
#     c2=APIClient(API_KEY,API_SECRET,REDIRECT_URL,token)
#     user=c2.get('user/show',screen_name=user)
#     print(id)
#     return id

# # 定义request，每次调用都会提供数据
# def request(url):
#     req=urllib.request.Request(url)
#     req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")
#     data=urllib.request.urlopen(req).read().decode('utf-8','ignore')
#     return data
# # 定义get_userInfo,每次调用返回指定用户信息
# def get_userInfo(id):
#     url='https://m.weibo.cn/api/container/getIndex?type=uid&value'+id
#     data=request(url)
#     content=json.loads(data)['data']
#     profile_image_url=content['userInfo']['profile_image_url']
#     description=content['userInfo']['description']
#     profile_url=content['userInfo']['profile_url']
#     verified=content['userInfo']['verified']
#     following=content['userInfo']['follow_count']
#     name=content['userInfo']['followers_count']
#     gender=content['userInfo']['gender']
#     urank=content['userInfo']['urank']

#     print("微博昵称："+name+"\n"+"微博地址主页："+profile_url+"\n")

# # 定义get_containerid, 每次调用都会返回containerid
# def get_containerid(url):
#     data=request(url)
#     content=json.loads(data).get('data')
#     print(content)
#     for data in content.get('tabsInfo').get('tabs'):
#         if data.get('tab_typr')=='weibo':
#             containerid=data.get('containerid')

#     return containerid

# # 获取微博内容信息
# def get_weibo(id,file):
#     i=1
#     while True:
#         url='https://m.weibo.cn/api/container/getIndex?tupe=uid&value'+id
#         weibo_url=url+'&container='+get_containerid(url)+'&page='+str(i)
#         print(weibo_url)
#         try:
#             data=request(weibo_url)
#             content=json.loads(data).get('data')
#             cards=content.get('cards')
#             if len(cards)>0:
#                 for j in range(len(cards)):
#                     print("正在爬取"+str(i)+"页，第"+str(j)+"条微博")
#                     card_type=cards[j].get('card_type')
#                     if card_type==9:
#                         mblog=cards[j].get('mblog')
#                         attitude_count=mblog.get('attitude_count')
#                         comments_count=mblog.get('comment_count')
#                         created_at=mblog.get('created_at')
#                         reports_count=mblog.get('reports_count')
#                         scheme=cards[j].get('scheme')
#                         text=mblog.get('text')
#                         with open(file,'a',encoding='utf-8') as fh:
#                             fh.write("第"+str(i)+"页，第"+str(j)+"条微博"+"\n")
#                             fh.write("微博地址："+str(scheme)+"\n")
#                 i+=1
#             else:
#                 break
#         except Exception as e:
#             print(e)
#             pass

# if __name__=="__main__":
#     username=''
#     # 用输入的用户名命名为文件
#     file=username+".txt"
#     id=get_id(username)
#     get_userInfo(id)
#     get_weibo(id,file)