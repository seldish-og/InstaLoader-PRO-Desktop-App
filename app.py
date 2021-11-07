import sys

from instagram import main
from PyQt5.QtWidgets import QApplication, QMainWindow
from views.design.design_app import Ui_MainWindow


class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        
        self.setupUi(self)


        self.pushButton.clicked.connect(self.run)

    def run(self):
        name = self.name_input.text()
        path = self.path_input.text()

        if self.radio_photo.isChecked():
            mode = "image"
        if self.radio_video.isChecked():
            mode = "video" 

        link = self.link_input.text()
        width = self.width_input.text()
        height = self.height_input.text()

        main.main(name, path, mode, link, width, height)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyApp()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())