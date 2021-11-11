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

# db = DataBase()
# id = 1
# mode = "image"
# name = "file.mp4"
# path = str(r"C:\Users\jegor\Desktop")
# formated_date = "21:42/2021-11-10"

# db.add_to_db(
#     '''INSERT INTO history_data(id, mode, name, path, date) 
#     VALUES (?,?,?,?,?);''', (id, mode, name, path, formated_date))


# if not db.get_data_db('''SELECT * FROM history_data'''):
#     print('hi')
# db.add_to_db("UPDATE history_data SET id = id + 1 WHERE id != 5")
# z = db.get_data_db('''SELECT * FROM history_data WHERE id = 1''')[0]
# print(z[0]) 
# db.add_to_db('''INSERT INTO history_data VALUES (1, "video", "file.mp4", "c:wwewenmnmnewk", "14:13/19.08")''')
# db.delete_from_db('''DELETE FROM history_data WHERE id = 3''')
# db.close_connection()
