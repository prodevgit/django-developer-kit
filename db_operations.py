import sqlite3
from sqlite3 import OperationalError

class SettingsDb():
    conn = sqlite3.connect('settings.db')
    def __init__(self):
        try:
            self.conn.execute('''CREATE TABLE SETTINGS
                 (ID INT PRIMARY KEY     NOT NULL,
                 NAME           TEXT    NOT NULL,
                 IS_FIELD           INT     NOT NULL,
                 IS_ENABLED        INT NOT NULL
                 );''')
        except OperationalError:
            print("Db exists")

    def getdb(self):
        return self.conn

    def add_field(self,field_name):
        try:
            cursor = self.conn.execute(f"SELECT id from SETTINGS where NAME='{field_name}'")
            if len(cursor.fetchall())==0:
                raise OperationalError
            print("Already added")
        except OperationalError:
            print("No such column")
            print("Adding new entry")
            cursor = self.conn.execute(f"SELECT id from SETTINGS")
            cursor_pointer = cursor.fetchall()
            if len(cursor_pointer) == 0:
                self.conn.execute(f"INSERT INTO SETTINGS (ID,NAME,IS_FIELD,IS_ENABLED) \
                      VALUES ({1}, '{field_name}', 1, 1 );");
            else:
                self.conn.execute(f"INSERT INTO SETTINGS (ID,NAME,IS_FIELD,IS_ENABLED) \
                                      VALUES ({cursor_pointer[-1][0] + 1}, '{field_name}', 1, 1 );");
            self.conn.commit()

    def enable_field(self, field_name):
        try:
            cursor = self.conn.execute(f"UPDATE SETTINGS set IS_ENABLED = 0 where NAME='{field_name}'")
            self.conn.commit()
            print(f"{field_name} enabled")
        except Exception as e:
            print(e)
            print("No such column")

    def disable_field(self, field_name):
        try:
            cursor = self.conn.execute(f"UPDATE SETTINGS  set IS_ENABLED = 1 where NAME='{field_name}'")
            self.conn.commit()
            print(f"{field_name} enabled")
        except Exception as e:
            print(e)
            print("No such column")