import requests
import json
import socket
def get_local_ip():
    sk = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sk.connect(('114.114.114.114',80))
    ip_addr = sk.getsockname()[0]
    return ip_addr
url = "http://{}:3333".format(get_local_ip())

data = ("{'sw_type':'1','id':'1','company_id':'838411'}").encode('utf-8')
response = requests.request(method='post',data=data,url=url).content.decode('utf8')
