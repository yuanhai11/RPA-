# encoding:utf-8
import json
import re

import requests
import time

from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()


class risk_marked(Base):
    # 表的名字:
    __tablename__ = 'risk_marked'

    # 表的结构:
    id = Column(Integer(), primary_key=True, autoincrement=True)
    company_id = Column(String(256))
    company_num = Column(String(256))
    info = Column(String(256))

    gmt_created = Column(String(256))
    gmt_updated = Column(String(256))


class sheet1(Base):
    # 表的名字:
    __tablename__ = 'sheet1'

    # 表的结构:
    id = Column(Integer(), primary_key=True, autoincrement=True)
    company_id = Column(String(256))
    company_num = Column(String(256))


# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:BOOT-xwork1024@192.168.2.97:3306/spider')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
# 创建session对象:
session = DBSession()


def dl(proxys):
    time.sleep(0.4)
    try:
        dlurl = 'http://api.ip.data5u.com/dynamic/get.html?order=fba1729fce7d27397dc2db1dc5db9977&random=2&sep=3'
        resp = requests.get(dlurl).text
        resp = re.sub(r'\n', '', resp)
        proxy = {
            'https': resp
        }
        proxys[0] = proxy
        print(proxys)
    except Exception as e:
        dl(proxys)


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
    ,
    # "cookie":"jsid=SEO-BAIDU-ALL-SY-000001; TYCID=7890f8302e8811ed8432ff21f0b4afdc; _bl_uid=p6lFz79RrU6dkjcUnhn89a8akaj5; bdHomeCount=5; HWWAFSESID=7f93e4db213220fa136; HWWAFSESTIME=1663049045642; csrfToken=v8tw_2PEKUlHIjSaxN1tA-2H; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1662539880,1662542320,1662602020,1663049052; bannerFlag=true; ssuid=3016468704; _ga=GA1.2.362850542.1663124541; cid=2350652265; ss_cidf=1; refresh_page=0; cloud_token=9a9e17c9682b44e5b3c1c32607611df7; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%225027336%22%2C%22first_id%22%3A%221831719546e175-062e36a43488d08-26021d51-2073600-1831719546ffe2%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfbG9naW5faWQiOiI1MDI3MzM2IiwiJGlkZW50aXR5X2Nvb2tpZV9pZCI6IjE4MzE3MTk1NDZlMTc1LTA2MmUzNmE0MzQ4OGQwOC0yNjAyMWQ1MS0yMDczNjAwLTE4MzE3MTk1NDZmZmUyIn0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%225027336%22%7D%2C%22%24device_id%22%3A%221831719546e175-062e36a43488d08-26021d51-2073600-1831719546ffe2%22%7D; tyc-user-info=%7B%22state%22%3A%227%22%2C%22vipManager%22%3A%220%22%2C%22mobile%22%3A%2215395831367%22%2C%22isExpired%22%3A%220%22%7D; tyc-user-info-save-time=1663233946703; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNTM5NTgzMTM2NyIsImlhdCI6MTY2MzIzMzk0NCwiZXhwIjoxNjY1ODI1OTQ0fQ.vVYwSpNWp61_OmRQr8_6-lB-JAHmOd_uEkU7J41COJtqKSYXcmnikchajiqEaEcg69GCSo7ssi7-fONeSxNCiQ; searchSessionId=1663394783.68694510; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1663395535"
}

from lxml import etree


# 破产重整3
def aa(company_id, company_num):
    while 1:
        try:
            d = requests.get(
                "https://www.tianyancha.com/company/{}".format(company_num),
                headers=headers, timeout=8).text
            print(d)
            if "股票行情" in d:
                print("----- risk_marked -----")
                d = etree.HTML(d)
                info1 = "".join(d.xpath('//table[@class="index_tableBox__ZadJW "]/tbody/tr[1]'))
                times = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                Patent = risk_marked(company_id=company_id, company_num=company_num,
                                     info=str(info1),
                                     gmt_created=times, gmt_updated=times)
                session.add(Patent)
                session.commit()
            print("--risk_marked-- over")
            break

        except Exception as e:
            print(e)
            time.sleep(0.4)
            dl(proxys)


if __name__ == '__main__':
    proxys = [{}]
    dl(proxys)
    data = session.query(sheet1).filter(sheet1.company_id != None, sheet1.company_num != None).all()
    print(len(data))
    for index, d in enumerate(data):
        company_id = d.company_id
        company_num = d.company_num
        print(company_id, company_num)
        aa(company_id, company_num)
