import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from design.design_app import Ui_MainWindow


class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.label.setText("OK")


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyApp()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())