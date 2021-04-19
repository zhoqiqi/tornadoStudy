import requests

# print(requests.get("http://172.16.1.128:8888/?name=bobby"))

# post  发送的应该是普通的表单数据
# requests.post("http://172.16.1.128:8888/", data={
#     "name": "zhouqiqi"
# })

# 发送json数据
requests.post("http://172.16.1.128:8888/", json={
    "name": "zhouqiqi"
})
