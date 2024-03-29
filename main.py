import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5 import QtWidgets
from ui_form import Ui_MainWindow
from add_to_bd import add_photo_to_bd, add_template
from photo_editor import edit_photo


class FlagMaker(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.add_picture.clicked.connect(self.picture)
        self.ui.add_template.clicked.connect(self.resize_template)
        self.ui.start_programm.clicked.connect(self.start_programm)

    def start_programm(self):
        self.ui.text_rating_3.setPixmap(QPixmap(self.add_picture))

    def resize_template(self):
        width = self.ui.len_template_X.text()
        height = self.ui.len_template_Y.text()
        add_template(width, height)

    def picture(self):
        self.add_picture = QtWidgets.QFileDialog.getOpenFileName(
            self, "Выбрать картинку", ""
        )[0].__str__()
        photo = edit_photo(self.add_picture)
        add_photo_to_bd(photo)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = FlagMaker()
    ex.show()
    sys.exit(app.exec_())
