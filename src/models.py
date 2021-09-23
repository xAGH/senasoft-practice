from mysql import connector as sql

class StartConnection():
    config = {
        "user": "root",
        "password":"alejo23001",
        "host":"localhost",
        "database":"db_estetica",
        "raise_on_warnings" : True
    }

    def start(self):
        self.db = sql.connect(**self.config)
        self.cursor = self.db.cursor()


class Customers(StartConnection):
    def create(self, name, email, password):
        try:
            self.start()
            self.cursor.execute(f"INSERT INTO customers(name, email, password) VALUES('{name}', '{email}', '{password}')")
            self.db.commit()
            return 200
        
        except:
            return 400
        
        finally:
            self.db.close()

    def read(self, uid = None):
        try:
            self.start()
            
            if uid == None:
                self.cursor.execute(f"SELECT * FROM customers")
                data = self.cursor.fetchall()
            
            else:
                self.cursor.execute(f"SELECT * FROM customers WHERE uid = '{uid}'")
                data = self.cursor.fetchall()

            return data

        except:
            return 400

        finally:
            self.db.close()

    def update(self, uid, name, email, password):
        try:
            self.start()
            self.cursor.execute(f"UPDATE customers SET name = '{name}', email = '{email}', password = '{password}' WHERE uid = '{uid}'")
            self.db.commit()
            return 200

        except:
            return 400
        
        finally:
            self.db.close()

    def delete(self, uid):
        try:
            self.start()
            self.cursor.execute(f"DELETE FROM customers WHERE uid = '{uid}'")
            self.db.commit()
            return 200

        except:
            return 400
        
        finally:
            self.db.close()