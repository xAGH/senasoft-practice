from db_manage import Connection

class Customers(Connection):
    def insert(self, name, email, password):
       return self.do_commit(f"INSERT INTO customers(name, email, password) VALUES('{name}', '{email}', '{password}')")

    def select(self, uid = None):
        if uid == None:
            return self.fetchall(f"SELECT * FROM customers")

        else:
            return self.fetchall(f"SELECT * FROM customers WHERE uid = '{uid}'")

    def update(self, uid, name, email, password):
        return self.do_commit(f"UPDATE customers SET name = '{name}', email = '{email}', password = '{password}' WHERE uid = '{uid}'")

    def delete(self, uid):
        self.do_commit(f"DELETE FROM customers WHERE uid = '{uid}'")