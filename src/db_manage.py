from mysql import connector as sql

class Connection():
    # Configuration neccesary to do a connection 
    config = {
        "user": "root",
        "password":"alejo23001",
        "host":"localhost",
        "database":"db_estetica",
        "raise_on_warnings" : True
    }

    def start(self):
        """
            Start a connection with the database. Create a instance and create a cursor.
        """
        self.db = sql.connect(**self.config)
        self.cursor = self.db.cursor()

    def do_commit(self, query):
        """
            Do commits in the database.
            @params: query --> Query what will be done in the database.
            @return True if the query was ejecuted successfully, else, it returns False
        """
        try:
            self.start()
            self.cursor.execute(query)
            self.db.commit()
            return True
        
        except:
            return False
        
        finally:
            self.db.close()

    def fetch_all(self, query):
        """
            Get all data for a select query
            @params: query --> Query what will be done in the database.
            @return Data if the query was ejecuted successfully, else, it returns False
        """
        try:
            self.start()
            self.cursor.execute(query)
            data = self.cursor.fetchall()
            return data

        except:
            return False

        finally:
            self.db.close()