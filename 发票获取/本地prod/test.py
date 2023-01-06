#encoding=utf-8
import random,re
import logging.config
import time
from ctypes import windll
# 加入pywintypes，打包成功
from threading import Lock

from Crypto.Cipher import AES
# 导入config里的变量信息
from decouple import config
from kafka import KafkaConsumer
from sqlalchemy.dialects import mysql
import sqlalchemy.ext.baked
import sqlalchemy.sql.default_comparator
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.orm import sessionmaker

import requests, json


def dl():
    time.sleep(1)
    try:
        dlurl = 'http://api.ip.data5u.com/dynamic/get.html?order=fba1729fce7d27397dc2db1dc5db9977&random=2&sep=3'
        resp = requests.get(dlurl).text
        resp = re.sub(r'\n', '', resp)
        # proxy = {
        #     'https': resp
        # }
        proxy =  {"http": 'http://' + resp, "https": 'https://' + resp}
        proxys[0] = proxy
        print(proxys)
    except Exception as e:
        print(e)
        dl()

def main():
    headers = {
        'cookie':'DTL_SESSION_ID=36c0f7f0-3248-4201-bdb9-91236b085448',
        'Content-Type': 'application/json;charset=UTF-8',
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
    }

    while 1:
        try:
            time.sleep(2)
            # session = requests.Session()
            # session.trust_env = False
            # response = session.get(url=url, headers=headers, )
            result = requests.get(
                'http://etax.zhejiang.chinatax.gov.cn/zjgfdacx/fpxxcx/query.do?rqq=20221127&rqz=20221127&fplx=zzsptfp&cxfs=KPF&kpfxx=&fpdm=&fphm=',
                # , data=data,
                headers=headers,proxies=proxys[-1], timeout=8,verify=False
            ).content.decode("utf-8")
            print("{}-{}".format(proxys,result))
            # result = requests.get(
            #   "http://www.baidu.com",
            #   headers=headers, proxies = proxys[-1],timeout=20,
            # ).text
            # print(result)
        except Exception as e:
            print(e)
            dl()



if __name__ == '__main__':
    proxys = [{'http': 'http://114.97.184.243:47916', "https": 'https://114.97.184.243:47916'}]
    main()
