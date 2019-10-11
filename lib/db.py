import pymysql
from config.config import *
class DB(object):
    def __init__(self):
        self.conn = pymysql.connect(
            host=db_host,
            port=db_port,
            user=db_user,
            passwd=db_passwd,
            db=db
        )
        self.cursor = self.conn.cursor()
    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def query(self,sql):
        logging.debug(sql)
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        logging.debug(result)
        return result

    def exec(self,sql):
        try:
            logging.debug(sql)
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            #print(str(e))
            logging.error(str(e))

    def check_user(self,user_name):
        result = self.query('select * from crm_customer where cust_name="{}"'.format((user_name)))
        return True if result else False

    def del_user(self,user_name):
        pass

    def add_user(self,user_name):
        pass

if __name__ == '__main__':
    db = DB()
    assert db.check_user('俞飞武')