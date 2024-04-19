import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5 import QtWidgets
from ui_form import Ui_MainWindow
from add_to_bd import add_photo_to_bd, add_template, take_values
from template import start
from PyQt5.QtWidgets import QMessageBox


class FlagMaker(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.len_template_X.setMaxLength(4)
        self.ui.len_template_Y.setMaxLength(4)
        self.ui.len_template_X.setPlaceholderText("X: ")
        self.ui.len_template_Y.setPlaceholderText("Y: ")
        self.ui.add_picture.clicked.connect(self.picture)
        self.ui.add_template.clicked.connect(self.resize_template)
        self.ui.start_programm.clicked.connect(self.start_programm)
        self.widt = ""
        self.heigh = ""

    def start_programm(self):
        if self.widt in ["", 0] and self.heigh in ["", 0]:
            QMessageBox.about(self, "Ошибка", "Введите размеры листа!")
        elif self.widt in ["", 0]:
            QMessageBox.about(self, "Title", "Введите длину листа!")
        elif self.heigh in ["", 0]:
            QMessageBox.about(self, "Title", "Введите ширину листа!")
        else:
            walues = take_values()[0]
            print(walues)
            picture = start(walues[0], walues[1])
            self.ui.text_rating_3.setPixmap(QPixmap(picture))

    def resize_template(self):
        self.widt = self.ui.len_template_X.text()
        self.heigh = self.ui.len_template_Y.text()
        add_template(self.widt, self.heigh)

    def picture(self):
        self.add_picture = QtWidgets.QFileDialog.getOpenFileName(
            self, "Выбрать картинку", ""
        )[0].__str__()
        add_photo_to_bd(self.add_picture)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = FlagMaker()
    ex.show()
    sys.exit(app.exec_())
