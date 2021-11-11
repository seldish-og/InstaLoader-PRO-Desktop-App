import sqlite3


class DataBase:
    def __init__(self):
        self.connection = sqlite3.connect("database/history.sqlite")
        self.cursor = self.connection.cursor()

    def update_db(self, command):
        self.cursor.execute(command)
        self.connection.commit()

    def add_to_db(self, command, arguments):
        self.cursor.execute(command, arguments)
        self.connection.commit()

    def delete_from_db(self, command):
        self.cursor.execute(command)
        self.connection.commit()

    def get_data_db(self, command):
        self.cursor.execute(command)
        return self.cursor.fetchall()

    def close_connection(self):
        self.cursor.close()
        self.connection.close()
