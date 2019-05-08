import pymysql


class DBHelper():
    def __init__(self):
        self.conn = None
        self.cur = None

    # 连接数据库
    def db_connect(self):

        try:
            # 连接数据库
            self.conn = pymysql.connect('localhost', 'root', '000000', 'Blues')
            self.cur = self.conn.cursor()
        except Exception:
            print('连接失败')
            return False

        return True

    # 关闭数据库
    def db_close(self):
        if self.conn and self.cur:
            self.cur.close()
            self.conn.close()
        return True

    #  执行数据库语句
    def db_execute(self, sql):
        self.db_connect()
        try:
            self.cur.execute(sql)
            print(sql)
            self.conn.commit()

        except Exception:
            print('execute error')
            self.db_close()

    # 查询操作
    def db_select(self, sql):
        print(sql)
        self.db_connect()
        self.cur.execute(sql)
        result = self.cur.fetchall()
        print(result)
        return result
