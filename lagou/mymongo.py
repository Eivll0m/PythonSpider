#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/1/20 16:03
# @Author   : Eivll0m
# @Site     : https://github.com/Eivll0m
# @File     : mymongo.py
# @Software : PyCharm


import pymongo

class MongodbOPT:
    def __init__(self, host, port, db, passwd, collection):
        self.host = host
        self.port = str(port)
        self.db = db
        self.passwd = passwd
        self.collection = collection

    def getClient(self):
        """返回MongoDB客户端对象"""
        conn = 'mongodb://' + self.db + ':' + self.passwd + '@' + self.host + ':' + self.port + '/' + self.db
        return pymongo.MongoClient(conn)

    def getDB(self):
        """返回MongoDB的一个数据库"""
        client = self.getClient()
        db = client['%s' % (self.db)]
        return db

    def insertData(self, bsonData):
        """插入数据（单条或多条）"""
        if self.db:
            db = self.getDB()
            collections = self.collection
            if isinstance(bsonData, list):
                result = db.get_collection(collections).insert_many(bsonData)
                return result.inserted_ids
            return db.get_collection(collections).insert_one(bsonData).inserted_id
        else:
            return None

    def findAll(self, **kwargs):
        if self.db:
            collections = self.collection
            db = self.getDB()
            def findAllDataQuery(self, dataLimit=0, dataSkip=0, dataQuery=None, dataSortQuery=None,dataProjection=None):
                return db.get_collection(collections).find(filter=dataQuery, projection=dataProjection, skip=dataSkip,
                                                           limit=dataLimit, sort=dataSortQuery)
            return findAllDataQuery(self, **kwargs)

    def updateData(self, oldData=None, **kwargs):
        if self.db:
            collections = self.collection
            db = self.getDB()
            def updateOne(self, oneOldData=None, oneUpdate=None, oneUpsert=False):  # 单个更新
                result = db.get_collection(collections).update_one(filter=oneOldData, update=oneUpdate,
                                                                  upsert=oneUpsert)
                return result.matched_count
            def updateMany(self, manyOldData, manyUpdate=None, manUpsert=False):  # 全部更新
                result = db.get_collection(collections).update_many(filter=manyOldData, update=manyUpdate,
                                                                    upsert=manUpsert)
                return result.matched_count
            if oldData:
                oneup = kwargs.get("oneUpdate", "")
                manyup = kwargs.get("manyUpdate", "")
                if oneup:
                    return updateOne(self, oldData, **kwargs)
                elif manyup:
                    return updateMany(self, oldData, **kwargs)
