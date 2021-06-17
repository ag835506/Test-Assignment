import requests
dic={}
comments_url="https://my-json-server.typicode.com/typicode/demo/comments"
post_url="https://my-json-server.typicode.com/typicode/demo/posts"
comment_resp=requests.get(comments_url).json()
post_resp=requests.get(post_url).json()
print(post_resp)
print(comment_resp)
for i in comment_resp:
    if i['postId'] in dic.keys():
        dic[i['postId']].append(i['body'])
    else:
        dic[i['postId']]=[i['body']]
for j in post_resp:
    if j['id'] in dic.keys():
        j['body']=dic[j['id']]
    else:
        data=j['body']=[]
print(post_resp)
    
