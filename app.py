import sys

from datetime import datetime 
from database import history
from instagram import main
from PyQt5.QtWidgets import QApplication, QMainWindow
from views.design.design_app import Ui_MainWindow


class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.db = history.DataBase()
        self.setupUi(self)

        card1 = self.db.get_data_db('''SELECT * FROM history_data WHERE id = 1''')[0]
        self.photo_1.setText(card1[1])
        self.file_1_tochange.setText(card1[2])
        self.path_1_tochange.setText(card1[3])
        self.date_1_tochange.setText(card1[4])

        card2 = self.db.get_data_db('''SELECT * FROM history_data WHERE id = 2''')[0]
        self.photo_2.setText(card2[1])
        self.file_2_tochange.setText(card2[2])
        self.path_2_tochange.setText(card2[3])
        self.date_2_tochange.setText(card2[4])

        card3 = self.db.get_data_db('''SELECT * FROM history_data WHERE id = 3''')[0]
        self.photo_3.setText(card3[1])
        self.file_3_tochange.setText(card3[2])
        self.path_3_tochange.setText(card3[3])
        self.date_3_tochange.setText(card3[4])

        card4 = self.db.get_data_db('''SELECT * FROM history_data WHERE id = 4''')[0]
        self.photo_4.setText(card4[1])
        self.file_4_tochange.setText(card4[2])
        self.path_4_tochange.setText(card4[3])
        self.date_4_tochange.setText(card4[4])

        self.pushButton.clicked.connect(self.download)

    def download(self):
        name = self.name_input.text()
        path = self.path_input.text()

        if self.radio_photo.isChecked():
            mode = "image"
        if self.radio_video.isChecked():
            mode = "video"
         
        
        link = self.link_input.text()
        width = self.width_input.text()
        height = self.height_input.text()

        date = str(datetime.now()).split()
        formated_date = f"{date[1][:-10]}/{date[0]}" 
        self.db.add_to_db(
            "UPDATE history_data SET id = id + 1 WHERE id != 5"
            )
        self.db.add_to_db(
            '''INSERT INTO history_data 
            VALUES ({}, {}, {}, {}, {})'''.format(1, mode, name, path, formated_date)
            )
        self.db.delete_from_db(
            '''DELETE FROM history_data WHERE id = 5'''
        )
        
        try:
            main.main(name, path, mode, link, width, height)
        except Exception as e:
            print(e)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyApp()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())