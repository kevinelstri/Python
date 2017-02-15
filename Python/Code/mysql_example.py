#!/usr/bin/env python
# coding=utf-8

import os
import LeeMdb

# 创建数据库实例
mysql_db = LeeMdb.LeeMySQLdb('localhost', 'root', '123', 'show160')

# 得到data 目录下的所有文件
file_names = [name for name in os.listdir('./data')
              if os.path.isfile(os.path.join('data', name))]
# 创建数据库
sql = '''
create table company_tbl (
	company_id char(10) unique key primary key not null,
	company_logo varchar(200),
	company_name varchar(200),
	company_service varchar(2000),
	company_introduce varchar(2000),
	company_address varchar(40),
	company_linkman varchar(10),
	company_tel varchar(50),
	company_email varchar(50),
	company_fax varchar(50)
    )
'''
mysql_db.createDatabase('company_tbl', sql)
# 读取文件
for i in range(len(file_names)):
    with open(os.path.join('data', file_names[i]), 'r') as f:
        print i
        company_info = f.read()
        # 字符替换
        company_info = company_info.replace('\n', '')
        # 字符分割
        j = -1
        info_list = []
        for info in company_info.split('::'):
            if (j == -1):
                j = 0
                continue
            if (j < 10):
                if (info == ''):
                    info = 'null'
                info_list.append(info)
                j += 1
            else:
                sql = 'insert ignore into company_tbl values(' + info_list[0] + ',"' + info_list[1] + '","' + info_list[
                    2] + '","' + info_list[3] + '","' + info_list[4] + '","' + info_list[5] + '","' + info_list[
                          6] + '","' + info_list[7] + '","' + info_list[8] + '","' + info_list[9] + '")'
                mysql_db.operateDatabase(sql)
                info_list = [info]
                j = 1
