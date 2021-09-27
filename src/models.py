from pymysql.err import MySQLError
from src.db_manage import Connection

class Model:

    def __init__(self) -> None:
        self.connection = Connection.open_connection()

    def fetch_all(self, sql: str):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql)
                data = cursor.fetchall()
                return data
        except MySQLError as e:
            raise e
        except Exception as e:
            raise e

    def fetch_one(self, sql: str, *args):
        try:
            with self.connection.cursor() as cur:
                cur.execute(sql, *args)
                data = cur.fetchone()
                return data
        except MySQLError as e:
            raise e
        except Exception as e:
            raise e

    def execute_query(self, sql: str, *args):
        try:
            with self.connection.cursor() as cur:
                cur.execute(sql, *args)
                self.connection.commit()
        except MySQLError as e:
            raise e
        except Exception as e:
            raise e
