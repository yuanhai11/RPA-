import requests
import json

headers = {
    'Content-Type': 'application/json;charset=UTF-8',
}
master_url_delete = 'http://192.168.2.98:48050/api/delete'
task_id = 824078
# 删除当前账户信息
data = {
    'id': task_id
}
res = requests.request("POST", master_url_delete, data=json.dumps(data, ensure_ascii=False),headers=headers).content.decode('utf8')
print(res)