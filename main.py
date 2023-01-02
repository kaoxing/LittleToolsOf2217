from PyQt5.QtWidgets import QApplication
import sys
from ToolsCode.Main.mainMenu import MyMenu


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyMenu()
    win.show()
    sys.exit(app.exec_())
