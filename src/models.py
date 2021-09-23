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

class Employee(Connection):
    def insert(self, name, lastname, service):
       return self.do_commit(f"INSERT INTO employees(name, lastname, service) VALUES('{name}', '{lastname}', '{service}')")

    def select(self, uid = None):
        if uid == None:
            return self.fetchall(f"SELECT * FROM employees")

        else:
            return self.fetchall(f"SELECT * FROM employees WHERE uid = '{uid}'")

    def update(self, uid, name, lastname, service):
        return self.do_commit(f"UPDATE employees SET name = '{name}', lastname = '{lastname}', service = '{service}' WHERE uid = '{uid}'")

    def delete(self, uid):
        self.do_commit(f"DELETE FROM employees WHERE uid = '{uid}'")

class Schedules(Connection):
    def insert(self, timeStart, timeEnd, status):
       return self.do_commit(f"INSERT INTO schedules(timeStart, timeEnd, status) VALUES('{timeStart}', '{timeEnd}', '{status}')")

    def select(self, code = None):
        if code == None:
            return self.fetchall(f"SELECT * FROM schedules")

        else:
            return self.fetchall(f"SELECT * FROM schedules WHERE code = '{code}'")

    def update(self, code, timeStart, timeEnd, status):
        return self.do_commit(f"UPDATE schedules SET timeStart = '{timeStart}', timeEnd = '{timeEnd}', status = '{status}' WHERE code = '{code}'")

    def delete(self, code):
        self.do_commit(f"DELETE FROM schedules WHERE code = '{code}'")

class Services(Connection):
    def insert(self, name, price):
       return self.do_commit(f"INSERT INTO services(name, timeEnd) VALUES('{name}', '{price}')")

    def select(self, uid = None):
        if uid == None:
            return self.fetchall(f"SELECT * FROM services")

        else:
            return self.fetchall(f"SELECT * FROM services WHERE uid = '{uid}'")

    def update(self, uid, name, price):
        return self.do_commit(f"UPDATE services SET name = '{name}', price = '{price}' WHERE uid = '{uid}'")

    def delete(self, uid):
        self.do_commit(f"DELETE FROM services WHERE uid = '{uid}'")

class Appointments(Connection):
    def insert(self, employee, service, customer, schedule):
       return self.do_commit(f"INSERT INTO appointments(employee, service, customer, schedule) VALUES('{employee}', '{service}', '{customer}', '{schedule}')")

    def select(self, uid = None):
        if uid == None:
            return self.fetchall(f"SELECT * FROM appointments")

        else:
            return self.fetchall(f"SELECT * FROM appointments WHERE uid = '{uid}'")

    def update(self, uid, employee, service, customer, schedule):
        return self.do_commit(f"UPDATE appointments SET employee = '{employee}', service = '{service}', customer = '{customer}', schedule = '{schedule}' WHERE uid = '{uid}'")

    def delete(self, uid):
        self.do_commit(f"DELETE FROM appointments WHERE uid = '{uid}'")

class Epmployee_schedule(Connection):
    def insert(self, employee, schedule):
       return self.do_commit(f"INSERT INTO epmployee_schedule(employee, schedule) VALUES('{employee}', '{schedule}')")

    def select(self, employee = None):
        if employee == None:
            return self.fetchall(f"SELECT * FROM epmployee_schedule")

        else:
            return self.fetchall(f"SELECT * FROM epmployee_schedule WHERE employee = '{employee}'")

    def update(self, uid, employee, schedule):
        return self.do_commit(f"UPDATE epmployee_schedule SET employee = '{employee}', schedule = '{schedule}' WHERE uid = '{uid}'")

    def delete(self, employee):
        self.do_commit(f"DELETE FROM epmployee_schedule WHERE uid = '{employee}'")

class Favorites(Connection):
    def insert(self, employee, customer):
       return self.do_commit(f"INSERT INTO favorites(employee, customer) VALUES('{employee}', '{customer}')")

    def select(self, employee = None):
        if employee == None:
            return self.fetchall(f"SELECT * FROM favorites")

        else:
            return self.fetchall(f"SELECT * FROM favorites WHERE employee = '{employee}'")

    def update(self, uid, employee, customer):
        return self.do_commit(f"UPDATE favorites SET employee = '{employee}', customer = '{customer}' WHERE uid = '{uid}'")

    def delete(self, employee):
        self.do_commit(f"DELETE FROM favorites WHERE uid = '{employee}'")