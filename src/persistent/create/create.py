# coding: utf-8 -*- coding: utf-
import os
import sqlite3
from sqlite3 import OperationalError
from src.start import script
logger = script.logger

# 创建数据库
def createSqlite(self,sqlDataName,createTableCommand):
    logger.info("检查数据库是否存在")
    if  os.path.exists(sqlDataName) is False:
        # 创建数据库
        logger.info("创建数据库")
        conn = sqlite3.connect(sqlDataName)
        cur = conn.cursor()
        try:
            sql = createTableCommand
            cur.execute(sql)
            logger.info("创建表成功")
            return True
        except OperationalError as o:
            logger.info(f"{str(o)}")
            pass
            if str(o) == "table gas_price already exists":
                return True
            return False
        except Exception as e:
            logger.exception(e)
            return False
        finally:
            cur.close()
            conn.close()
    else:
        logger.info(f"{sqlDataName} 数据库已存在")