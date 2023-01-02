from PyQt5.QtWidgets import QApplication
import sys
from myLogin import MyLogin


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyLogin()
    win.show()
    sys.exit(app.exec_())
