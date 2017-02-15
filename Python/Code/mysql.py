#!/usr/bin/env python
# coding=utf-8
import MySQLdb


class LeeMySQLdb:
    def __init__(self, url, username, passwd, database):
        # 连接数据库
        self.db = MySQLdb.connect(url, username, passwd, database)
        # 获取mysql操作游标
        self.cursor = self.db.cursor()

    # 创建数据库
    def createDatabase(self, database_name, create_sql):
        # 如果存在删除
        self.cursor.execute('DROP TABLE IF EXISTS ' + database_name)
        # 创建db
        self.cursor.execute(create_sql)

    # 操作数据:插入、更新、删除
    '''
    insert/update/delete
    '''

    def operateDatabase(self, operate_sql):
        # print operate_sql
        try:
            self.cursor.execute(operate_sql)
            self.db.commit()
        except:
            print '操作失败！'
            self.db.rollback()

    # 查询数据：查询
    def selectDatabase(self, select_sql):
        try:
            result = self.cursor.execute(select_sql)
            return result
        except:
            print '查询失败！'

    # 关闭数据库
    def closeDatabase(self):
        self.db.close()
