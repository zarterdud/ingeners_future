import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets
from ui_form import Ui_MainWindow


class FlagMaker(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.add_picture.clicked.connect(self.picture)

    def main(self):
        photo = self.add_picture

    def picture(self):
        self.add_picture = QtWidgets.QFileDialog.getOpenFileName(
            self, "Выбрать картинку", ""
        )[0].__str__()
        print(self.add_picture)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = FlagMaker()
    ex.show()
    sys.exit(app.exec_())
