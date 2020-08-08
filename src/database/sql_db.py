import pymysql


sql_file = "./lib/database/create_table.sql"

conn = pymysql.connect(
    host='127.1.1.1',
    port=3306,
    user='xiang',
    passwd='123321',
    charset='utf8',
)


class Database:

    @classmethod
    def create_mysql(cls, new_db="test"):
        cur = conn.cursor()
        cur.execute("create database " + new_db + " if not exists")
        cur.execute("SET NAMES utf8")
        cur.execute("set group_concat_max_len = 10240000")
        cur.execute("use " + new_db)
        with open(sql_file, "r") as sql:
            requests = sql.read().split(';')
            requests.pop()
        for request in requests:
            cur.execute(request + ";")
        return conn, cur

    @classmethod
    def get_mysql(cls, db_file='test'):
        cur = conn.cursor()
        cur.execute("use " + db_file)
        return conn, cur
