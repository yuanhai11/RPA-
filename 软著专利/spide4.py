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


class sheet1(Base):
    # 表的名字:
    __tablename__ = 'sheet1'

    # 表的结构:
    id = Column(Integer(), primary_key=True, autoincrement=True)
    company_id = Column(String(256))
    company_num = Column(String(256))

class company_patent(Base):
    # 表的名字:
    __tablename__ = 'company_patent_test'

    # 表的结构:
    id = Column(Integer(), primary_key=True, autoincrement=True)
    company_id = Column(String(256))
    company_num = Column(String(256))
    apply_public_date = Column(String(256))
    patent_name = Column(String(256))
    apply_num = Column(String(256))
    apply_public_num = Column(String(256))
    type = Column(String(256))

    gmt_created = Column(String(256))
    gmt_updated = Column(String(256))


class company_software(Base):
    # 表的名字:
    __tablename__ = 'company_software_test'

    # 表的结构:
    id = Column(Integer(), primary_key=True, autoincrement=True)
    company_id = Column(String(256))
    company_num = Column(String(256))
    author_nationality = Column(String(256))
    simple_name = Column(String(256))
    reg_num = Column(String(256))
    full_name = Column(String(256))
    cat_num = Column(String(256))
    version = Column(String(256))
    reg_date = Column(String(256))
    publish_date = Column(String(256))

    gmt_created = Column(String(256))
    gmt_updated = Column(String(256))


class risk_administrative_penalties(Base):
    # 表的名字:
    __tablename__ = 'risk_administrative_penalties'

    # 表的结构:
    id = Column(Integer(), primary_key=True, autoincrement=True)
    company_id = Column(String(256))
    company_num = Column(String(256))
    punish_number = Column(String(256))
    punish_reason = Column(String(256))
    punish_content = Column(String(256))
    punish_date = Column(String(256))
    punish_department = Column(String(256))
    show_type_name = Column(String(256))

    gmt_created = Column(String(256))
    gmt_updated = Column(String(256))


class risk_break_rebuild(Base):
    # 表的名字:
    __tablename__ = 'risk_break_rebuild'

    # 表的结构:
    id = Column(Integer(), primary_key=True, autoincrement=True)
    company_id = Column(String(256))
    company_num = Column(String(256))
    submit_time = Column(String(256))
    case_no = Column(String(256))
    case_type = Column(String(256))
    applicant = Column(String(256))
    respondent = Column(String(256))
    court = Column(String(256))

    gmt_created = Column(String(256))
    gmt_updated = Column(String(256))


class risk_business_exception(Base):
    # 表的名字:
    __tablename__ = 'risk_business_exception'

    # 表的结构:
    id = Column(Integer(), primary_key=True, autoincrement=True)
    company_id = Column(String(256))
    company_num = Column(String(256))
    put_date = Column(String(256))
    put_department = Column(String(256))
    put_reason = Column(String(256))
    put_reason_type = Column(String(256))

    gmt_created = Column(String(256))
    gmt_updated = Column(String(256))


class risk_dishonest(Base):
    # 表的名字:
    __tablename__ = 'risk_dishonest'

    # 表的结构:
    id = Column(Integer(), primary_key=True, autoincrement=True)
    company_id = Column(String(256))
    company_num = Column(String(256))
    reg_date = Column(String(256))
    publish_date = Column(String(256))
    gist_unit = Column(String(256))
    case_code = Column(String(256))
    gis_tid = Column(String(256))
    disrupt_type_name = Column(String(256))
    performance = Column(String(256))
    i_name = Column(String(256))

    gmt_created = Column(String(256))
    gmt_updated = Column(String(256))


class risk_environmental_money(Base):
    # 表的名字:
    __tablename__ = 'risk_environmental_money'

    # 表的结构:
    id = Column(Integer(), primary_key=True, autoincrement=True)
    company_id = Column(String(256))
    company_num = Column(String(256))
    publish_time = Column(String(256))
    punish_number = Column(String(256))
    punish_reason = Column(String(256))
    punish_content = Column(String(256))
    punish_department = Column(String(256))

    gmt_created = Column(String(256))
    gmt_updated = Column(String(256))


class risk_home_mortgage(Base):
    # 表的名字:
    __tablename__ = 'risk_home_mortgage'

    # 表的结构:
    id = Column(Integer(), primary_key=True, autoincrement=True)
    company_id = Column(String(256))
    company_num = Column(String(256))
    reg_date = Column(String(256))
    reg_num = Column(String(256))
    people_info = Column(String(256))
    mort_gagor_info = Column(String(256))
    over_view_type = Column(String(256))
    over_view_term = Column(String(256))
    amount = Column(String(256))
    reg_department = Column(String(256))

    gmt_created = Column(String(256))
    gmt_updated = Column(String(256))


class risk_limit_consumer(Base):
    # 表的名字:
    __tablename__ = 'risk_limit_consumer'

    # 表的结构:
    id = Column(Integer(), primary_key=True, autoincrement=True)
    company_id = Column(String(256))
    company_num = Column(String(256))
    publish_date = Column(String(256))
    case_code = Column(String(256))
    qy_info = Column(String(256))
    x_name = Column(String(256))
    applicant = Column(String(256))
    case_create_time = Column(String(256))

    gmt_created = Column(String(256))
    gmt_updated = Column(String(256))


class risk_owe_tax_notice(Base):
    # 表的名字:
    __tablename__ = 'risk_owe_tax_notice'

    # 表的结构:
    id = Column(Integer(), primary_key=True, autoincrement=True)
    company_id = Column(String(256))
    company_num = Column(String(256))
    legalperson_name = Column(String(256))
    location = Column(String(256))
    name = Column(String(256))
    new_own_tax_balance = Column(String(256))
    own_tax_balance = Column(String(256))
    publish_date = Column(String(256))
    tax_category = Column(String(256))
    taxId_number = Column(String(256))

    gmt_created = Column(String(256))
    gmt_updated = Column(String(256))


class risk_serious_violation(Base):
    # 表的名字:
    __tablename__ = 'risk_serious_violation'

    # 表的结构:
    id = Column(Integer(), primary_key=True, autoincrement=True)
    company_id = Column(String(256))
    company_num = Column(String(256))
    put_reason = Column(String(256))
    put_department = Column(String(256))
    put_date = Column(String(256))

    gmt_created = Column(String(256))
    gmt_updated = Column(String(256))


class risk_tax_money(Base):
    # 表的名字:
    __tablename__ = 'risk_tax_money'

    # 表的结构:
    id = Column(Integer(), primary_key=True, autoincrement=True)
    company_id = Column(String(256))
    company_num = Column(String(256))
    case_type = Column(String(256))
    department = Column(String(256))
    taxpayer_name = Column(String(256))

    gmt_created = Column(String(256))
    gmt_updated = Column(String(256))


class risk_limit_out_city(Base):
    # 表的名字:
    __tablename__ = 'risk_limit_out_city'

    # 表的结构:
    id = Column(Integer(), primary_key=True, autoincrement=True)
    company_id = Column(String(256))
    company_num = Column(String(256))
    issue_date = Column(String(256))
    human_name = Column(String(256))
    executed = Column(String(256))
    executed_address = Column(String(256))
    applicant = Column(String(256))
    money = Column(String(256))
    court = Column(String(256))

    gmt_created = Column(String(256))
    gmt_updated = Column(String(256))


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
}


# 软著3
def soft(company_id, company_num):
    f = False
    max_pages = 100
    # for page in range(1, max_pages + 1):
    #     if f:
    #         break
    time.sleep(0.4)
    while 1:
        try:
            # data = {"_": "1662602428454", "id": "4997169666", "pageSize": 100, "pageNum": page, "regYear": "-100", }
            data = {"_": "1662602428454", "id": company_num, "pageSize": 100, "pageNum": 1, "regYear": "-100", }

            d = requests.get(
                "https://capi.tianyancha.com/cloud-intellectual-property/intellectualProperty/softwareCopyrightListV2?",
                headers=headers, params=data, proxies=proxys[-1], timeout=8).json()
            print("----- soft -----")

            if d["data"] == None:
                break
            try:
                items = d["data"]['items']
            except Exception:
                break
            for item in items:
                try:
                    simple_name = item['simplename']
                    author_nationality = item['authorNationality']
                    reg_num = item['regnum']
                    full_name = item['fullname']
                    cat_num = item['catnum']
                    version = item['version']
                    reg_date = parse_time(item['regtime'])
                    publish_date = parse_time(item['publishtime'])
                    times = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

                    Soft = company_software(company_id=company_id, company_num=company_num, simple_name=simple_name,
                                            author_nationality=author_nationality,
                                            reg_num=reg_num, full_name=full_name, cat_num=cat_num, version=version,
                                            reg_date=reg_date, publish_date=publish_date,
                                            gmt_created=times, gmt_updated=times)
                except Exception:
                    continue
                else:
                    session.add(Soft)
                finally:
                    session.commit()
            print("--soft-- over")
            break

        except Exception as e:
            print(e)
            time.sleep(0.4)
            dl(proxys)


# 专利3
def patent(company_id, company_num):
    time.sleep(0.4)
    while 1:
        try:
            data = {"_": "1662602428454", "id": company_num, "pageSize": 100, "pageNum": 1, "type": "-100",
                    "lprs": "-100", "applyYear": "-100", "pubYear": "-100", "sortType": "-100"}
            d = requests.get("https://capi.tianyancha.com/cloud-intellectual-property/patent/patentListV6?",
                             headers=headers, params=data, proxies=proxys[-1], timeout=8).json()

            print("----- patent -----")
            time.sleep(0.4)

            try:
                items = d["data"]['items']
            except Exception:
                break
            # realTotal = d["data"]['realTotal']

            if items == None or items == []:
                # print("patent is out")
                # f = True
                break
            for item in items:
                try:
                    apply_public_date = item['applicationPublishTime']
                    patent_name = item['title']
                    apply_num = item['pubnumber']
                    # apply_public_num = item['patentNum']
                    type = item['patentType']
                    times = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

                    Patent = company_patent(company_id=company_id, company_num=company_num,
                                            apply_public_date=apply_public_date, patent_name=patent_name,
                                            apply_num=apply_num, type=type,
                                            gmt_created=times, gmt_updated=times)
                except Exception:
                    continue
                else:
                    session.add(Patent)
                finally:
                    session.commit()
            print("--patent-- over")
            break
        except Exception as e:
            print(e)
            time.sleep(0.4)
            dl(proxys)


# 行政处罚3
def Administrative_penalties(company_id, company_num):
    # max_pages = 100
    # for page in range(1, max_pages + 1):
    #     time.sleep(0.4)
    #
    while 1:
        try:
            data = {"withOwner": 0, "_": "1663054546144", "pageSize": 100, "pageNum": 1, "gid": company_num}
            d = requests.get(
                "https://capi.tianyancha.com/cloud-operating-risk/operating/punishment/punishIndexList?",
                headers=headers, params=data, proxies=proxys[-1], timeout=8).json()

            print("----- Administrative_penalties -----")

            time.sleep(0.4)
            try:
                items = d["data"]['list']
            except Exception:
                break
            if items == None or items == []:
                break
            for item in items:
                try:
                    punishContent = item['punishContent']
                    punishDate = item['punishDate']
                    punishDepartment = item['punishDepartment']
                    punishNumber = item['punishNumber']
                    punishReason = item['punishReason']
                    showTypeName = item['showTypeName']
                    times = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

                    Patent = risk_administrative_penalties(company_id=company_id, company_num=company_num,
                                                           punish_content=punishContent, punish_date=punishDate,
                                                           punish_department=punishDepartment,
                                                           punish_number=punishNumber, punish_reason=punishReason,
                                                           show_type_name=showTypeName,
                                                           gmt_created=times, gmt_updated=times)
                except Exception:
                    continue
                else:
                    session.add(Patent)
                finally:
                    session.commit()

            print("--Administrative_penalties-- over")
            break
        except Exception as e:
            print(e)
            time.sleep(0.4)
            dl(proxys)


# 经营异常3
def business_exception(company_id, company_num):
    while 1:
        try:
            data = {"_": "1663054546144", "pageSize": 100, "pageNum": 1, "gid": company_num,
                    "abnormalType": 1}
            d = requests.get(
                "https://capi.tianyancha.com/cloud-operating-risk/operating/abnormal/getAbnormalListByType?",
                headers=headers, params=data, proxies=proxys[-1], timeout=8).json()
            print("----- business_exception -----")
            time.sleep(0.4)
            try:
                items = d["data"]['result']
            except Exception:
                break
            if items == None or items == []:
                break
            for item in items:
                try:
                    putDate = item['putDate']
                    putDepartment = item['putDepartment']
                    putReason = item['putReason']
                    putReasonType = item['putReasonType']
                    times = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

                    Patent = risk_business_exception(company_id=company_id, company_num=company_num,
                                                     put_date=putDate, put_department=putDepartment,
                                                     put_reason=putReason, put_reason_type=putReasonType,
                                                     gmt_created=times, gmt_updated=times)
                except Exception:
                    continue
                else:
                    session.add(Patent)
                finally:
                    session.commit()
            print("--business_exception-- over")
            break
        except Exception as e:
            print(e)
            time.sleep(0.4)
            dl(proxys)


# 严重违法3
def Serious_violation(company_id, company_num):
    while 1:
        try:
            data = {"_": "1663054546144", "pageSize": 100, "illegalType=1": 1, "pageNum": 1, "gid": company_num}
            d = requests.get(
                "https://capi.tianyancha.com/cloud-operating-risk/operating/illegal/getCompanyIllegalInfoListByType?",
                headers=headers, params=data, proxies=proxys[-1], timeout=8).json()
            print("----- Serious_violation -----")

            time.sleep(0.4)
            try:
                items = d["data"]['items']
            except Exception:
                break
            if items == None or items == []:
                break
            for item in items:
                try:
                    putReason = item['putReason']
                    putDepartment = item['putDepartment']
                    putDate = item['putDate']
                    times = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

                    Patent = risk_serious_violation(company_id=company_id, company_num=company_num,
                                                    put_date=putDate, put_department=putDepartment,
                                                    put_reason=putReason,
                                                    gmt_created=times, gmt_updated=times)
                except Exception:
                    continue
                else:
                    session.add(Patent)
                finally:
                    session.commit()
            print("--Serious_violation-- over")
            break
        except Exception as e:
            print(e)
            time.sleep(0.4)
            dl(proxys)


# 税收违法3
def tax_money(company_id, company_num):
    while 1:
        try:
            data = {"_": "1663054546144", "pageSize": 100, "pageNum": 1, "gid": company_num}
            d = requests.get(
                "https://capi.tianyancha.com/cloud-operating-risk/operating/taxContraventions/getTaxContraventions?",
                headers=headers, params=data, proxies=proxys[-1], timeout=8).json()
            print("----- tax_money -----")

            time.sleep(0.4)
            try:
                items = d["data"]['result']
            except Exception:
                break
            if items == None or items == []:
                break
            for item in items:
                try:
                    case_type = item['case_type']
                    department = item['department']
                    taxpayer_name = item['taxpayer_name']
                    times = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

                    Patent = risk_tax_money(company_id=company_id, company_num=company_num,
                                            case_type=case_type, department=department,
                                            taxpayer_name=taxpayer_name,
                                            gmt_created=times, gmt_updated=times)
                except Exception:
                    continue
                else:
                    session.add(Patent)
                finally:
                    session.commit()
            print("--tax_money-- over")
            break
        except Exception as e:
            print(e)
            time.sleep(0.4)
            dl(proxys)


# 动产抵押 3
def home_mortgage(company_id, company_num):
    import json
    while 1:
        try:
            data = {"_": "1663054546144", "pageSize": 100, "pageNum": 1, "gid": company_num, "type": -100}
            d = requests.get(
                "https://capi.tianyancha.com/cloud-operating-risk/operating/chattelMortgage/companyMortgage.json?",
                headers=headers, params=data, proxies=proxys[-1], timeout=8).json()
            print("----- home_mortgage -----")

            time.sleep(0.4)
            try:
                if type(d["data"])==type(''):
                    items = json.loads(d["data"])['items']
                else:
                    items = d["data"]['items']

            except Exception:
                break
            if items == None or items == []:
                break
            for item in items:
                try:
                    regDate = item['baseInfo']['regDate']
                    regNum = item['baseInfo']['regNum']
                    peopleInfo = str(item['peopleInfo'])
                    mortgagorInfo = str(item['mortgagorInfo'])
                    overviewType = item['baseInfo']['overviewType']
                    amount = item['baseInfo']['amount']
                    overviewTerm = item['baseInfo']['overviewTerm']
                    regDepartment = item['baseInfo']['regDepartment']
                    times = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

                    Patent = risk_home_mortgage(company_id=company_id, company_num=company_num,
                                                reg_date=regDate, reg_num=regNum,
                                                people_info=peopleInfo, mort_gagor_info=mortgagorInfo,
                                                over_view_type=overviewType,
                                                amount=amount, over_view_term=overviewTerm,
                                                reg_department=regDepartment,
                                                gmt_created=times, gmt_updated=times)
                except Exception:
                    continue
                else:
                    session.add(Patent)
                finally:
                    session.commit()
            print("--home_mortgage-- over")
            break

        except Exception as e:
            print(e)
            time.sleep(0.4)
            dl(proxys)


# 环保处罚3
def Environmental_money(company_id, company_num):
    while 1:
        try:
            data = {"withOwner": 0, "_": "1663054546144", "pageSize": 100, "pageNum": 1, "gid": company_num,
                    "punishYear": -100}
            d = requests.get(
                "https://capi.tianyancha.com/cloud-operating-risk/operating/environmental/getEnvironmentalPenaltiesNew?",
                headers=headers, params=data, proxies=proxys[-1], timeout=8).json()
            print("----- Environmental_money -----")

            time.sleep(0.4)

            try:
                if type(d["data"]) == type(''):
                    items = json.loads(d["data"])['result']
                else:
                    items = d["data"]['result']
            except Exception:
                break
            if items == None or items == []:
                break
            for item in items:
                try:
                    publish_time = parse_time(item['publish_time'])
                    punish_number = item['punish_number']
                    punish_reason = item['punish_reason']
                    punish_content = item['punish_content']
                    punish_department = item['punish_department']
                    times = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

                    Patent = risk_environmental_money(company_id=company_id, company_num=company_num,
                                                      publish_time=publish_time, punish_number=punish_number,
                                                      punish_reason=punish_reason, punish_content=punish_content,
                                                      punish_department=punish_department,
                                                      gmt_created=times, gmt_updated=times)
                except Exception:
                    continue
                else:
                    session.add(Patent)
                finally:
                    session.commit()
            print("--Environmental_money-- over")
            break

        except Exception as e:
            print(e)
            time.sleep(0.4)
            dl(proxys)


# 欠税公告3
def owe_tax_notice(company_id, company_num):
    while 1:
        try:
            data = {"history": False, "_": "1663054546144", "pageSize": 100, "pageNum": 1, "gid": company_num}
            d = requests.get(
                "https://capi.tianyancha.com/cloud-operating-risk/operating/tax/companyowntax.json?",
                headers=headers, params=data, proxies=proxys[-1], timeout=8).json()
            print("----- owe_tax_notice -----")
            time.sleep(0.4)

            try:
                if type(d["data"]) == type(''):
                    items = json.loads(d["data"])['items']
                else:
                    items = d["data"]['items']
            except Exception:
                break

            if items == None or items == []:
                break
            for item in items:
                try:
                    legalpersonName = item['legalpersonName']
                    location = item['location']
                    name = item['name']
                    newOwnTaxBalance = item['newOwnTaxBalance']
                    ownTaxBalance = item['ownTaxBalance']
                    publishDate = item['publishDate']
                    taxCategory = item['taxCategory']
                    taxIdNumber = item['taxIdNumber']
                    times = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

                    Patent = risk_owe_tax_notice(company_id=company_id, company_num=company_num,
                                                 legalperson_name=legalpersonName, location=location,
                                                 name=name, new_own_tax_balance=newOwnTaxBalance,
                                                 own_tax_balance=ownTaxBalance,
                                                 publish_date=publishDate,
                                                 tax_category=taxCategory,
                                                 taxId_number=taxIdNumber,
                                                 gmt_created=times, gmt_updated=times)
                except Exception:
                    continue
                else:
                    session.add(Patent)
                finally:
                    session.commit()
            print("--owe_tax_notice-- over")
            break

        except Exception as e:
            print(e)
            time.sleep(0.4)
            dl(proxys)


# 限制消费令3
def limit_consumer(company_id, company_num):
    while 1:
        try:
            data = {"_": "1663054546144", "pageSize": 100, "pageNum": 1, "gid": company_num}
            d = requests.get(
                "https://capi.tianyancha.com/cloud-judicial-risk/risk/getRestrictOrder?",
                headers=headers, params=data, proxies=proxys[-1], timeout=8).json()
            print("----- limit_consumer -----")

            time.sleep(0.4)

            try:
                if type(d["data"]) == type(''):
                    items = json.loads(d["data"])['items']
                else:
                    items = d["data"]['items']
            except Exception:
                break
            if items == None or items == []:
                break
            for item in items:
                try:
                    publish_date = item['publishDate']
                    case_code = item['caseCode']
                    qy_info = item['qyinfo']
                    x_name = item['xname']
                    applicant = item['applicant']
                    case_create_time = parse_time(item['caseCreateTime'])
                    times = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

                    Patent = risk_limit_consumer(company_id=company_id, company_num=company_num,
                                                 publish_date=publish_date, case_code=case_code,
                                                 qy_info=qy_info, x_name=x_name, applicant=applicant,
                                                 case_create_time=case_create_time,
                                                 gmt_created=times, gmt_updated=times)
                except Exception:
                    continue
                else:
                    session.add(Patent)
                finally:
                    session.commit()
            print("--limit_consumer-- over")
            break

        except Exception as e:
            print(e)
            time.sleep(0.4)
            dl(proxys)


# 失信被执行人3
def dishonest(company_id, company_num):
    while 1:
        try:
            data = {"_": "1663054546144", "performance": -100, "year": -100, "keyWords": "", "pageSize": 100,
                    "pageNum": 1, "gid": company_num}
            d = requests.get(
                "https://capi.tianyancha.com/cloud-judicial-risk/risk/dishonest?",
                headers=headers, params=data, proxies=proxys[-1], timeout=8).json()
            print("----- dishonest -----")
            time.sleep(0.4)
            try:
                if type(d["data"]) == type(''):
                    items = json.loads(d["data"])['items']
                else:
                    items = d["data"]['items']
            except Exception:
                break
            if items == None or items == []:
                break
            for item in items:
                try:
                    iname = item['iname']
                    disrupttypename = item['disrupttypename']
                    casecode = item['casecode']
                    performance = item['performance']
                    regdate = parse_time(item['regdate'])
                    publishdate = parse_time(item['publishdate'])
                    gistunit = item['gistunit']
                    gistid = item['gistid']
                    times = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

                    Patent = risk_dishonest(company_id=company_id, company_num=company_num,
                                            i_name=iname, disrupt_type_name=disrupttypename,
                                            case_code=casecode, performance=performance, reg_date=regdate,
                                            publish_date=publishdate, gist_unit=gistunit, gis_tid=gistid,
                                            gmt_created=times, gmt_updated=times)
                except Exception:
                    continue
                else:
                    session.add(Patent)
                finally:
                    session.commit()
            print("--dishonest-- over")
            break

        except Exception as e:
            print(e)
            time.sleep(0.4)
            dl(proxys)


# 限制出境3
def limit_out_city(company_id, company_num):
    while 1:
        try:
            data = {"_": "1663054546144", "pageSize": 100, "pageNum": 1, "gid": company_num}
            d = requests.get(
                "https://capi.tianyancha.com/cloud-judicial-risk/risk/company/restrictedOutbound/list?",
                headers=headers, params=data, proxies=proxys[-1], timeout=8).json()
            print("----- limit_out_city -----")

            time.sleep(0.4)
            try:
                items = d["data"]['caseList']
            except Exception:
                break
            if items == None or items == []:
                break
            for item in items:
                try:
                    issue_date = item['issueDate']
                    human_name = item['humanName']
                    executed = str(item['executed'])
                    executed_address = item['executedAddress']
                    applicant = str(item['applicant'])
                    money = item['money']
                    court = item['court']
                    times = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

                    Patent = risk_limit_out_city(company_id=company_id, company_num=company_num,
                                                 issue_date=issue_date, human_name=human_name,
                                                 executed=executed, executed_address=executed_address,
                                                 applicant=applicant, money=money, court=court,
                                                 gmt_created=times, gmt_updated=times)
                except Exception:
                    continue
                else:
                    session.add(Patent)
                finally:
                    session.commit()
            print("--limit_out_city-- over")
            break
        except Exception as e:
            print(e)
            time.sleep(0.4)
            dl(proxys)


# 破产重整3
def break_rebuild(company_id, company_num):
    while 1:
        try:
            data = {"_": "1663054546144", "pageSize": 100, "pageNum": 1, "gid": company_num}
            d = requests.get(
                "https://capi.tianyancha.com/cloud-judicial-risk/bankruptcy/list?",
                headers=headers, params=data, proxies=proxys[-1], timeout=8).json()

            print("----- break_rebuild -----")
            time.sleep(0.4)
            try:
                items = d["data"]['items']
            except Exception:
                break
            if items == None or items == []:
                break
            for item in items:
                try:
                    submitTime = item['submitTime']
                    caseNo = item['caseNo']
                    caseType = item['caseType']
                    applicant = str(item['applicant'])
                    respondent = item['respondent']
                    court = item['court']
                    times = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

                    Patent = risk_break_rebuild(company_id=company_id, company_num=company_num,
                                                submit_time=submitTime, case_no=caseNo,
                                                case_type=caseType, applicant=applicant, respondent=respondent,
                                                court=court,
                                                gmt_created=times, gmt_updated=times)
                except Exception:
                    continue
                else:
                    session.add(Patent)
                finally:
                    session.commit()
            print("--break_rebuild-- over")
            break

        except Exception as e:
            print(e)
            time.sleep(0.4)
            dl(proxys)


def parse_time(timeStamp):
    otherStyleTime = None
    try:
        if timeStamp == None or timeStamp == '':
            return None
        timeStamp = int(timeStamp / 1000)
        timeArray = time.localtime(timeStamp)
        otherStyleTime = time.strftime("%Y-%m-%d", timeArray)
    except Exception as e:
        print(e)
    finally:
        return otherStyleTime


# def patent_unique(table, param2):
#     data = session.query(table).filter(table.apply_num == param2).first()
#     return True if data == None else False
#
#
# def soft_unique(table, param2):
#     data = session.query(table).filter(table.reg_num == param2).first()
#     return True if data == None else False


if __name__ == '__main__':
    proxys = [{}]
    dl(proxys)

    data = session.query(sheet1).filter(sheet1.company_id != None, sheet1.company_num != None).all()
    print(len(data))
    for index,d in enumerate(data[13000:16000]):
        # if index<5 :
        #     continue
        company_id = d.company_id
        company_num = d.company_num
        print(company_id,company_num)
        patent(company_id, company_num)
        soft(company_id, company_num)
        Administrative_penalties(company_id, company_num)
        business_exception(company_id, company_num)
        Serious_violation(company_id, company_num)
        tax_money(company_id, company_num)
        home_mortgage(company_id, company_num)
        Environmental_money(company_id, company_num)
        owe_tax_notice(company_id, company_num)
        limit_consumer(company_id, company_num)
        dishonest(company_id, company_num)
        limit_out_city(company_id, company_num)
        break_rebuild(company_id, company_num)
