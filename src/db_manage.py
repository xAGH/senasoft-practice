from pymysql import Connection, connect, MySQLError

class Connection:

    mysql: Connection

    @classmethod
    def open_connection(cls):
        try:
            cls.mysql = connect(host="localhost", user="root", passwd="2004", database="db_senasoft", port=3306)
            return cls.mysql
        except MySQLError as e:
            raise e
        except Exception as e:
            print("An error with the dabatase: {e}".format(e))
            raise e
