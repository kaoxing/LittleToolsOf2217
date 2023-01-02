from PyQt5.QtWidgets import QWidget
from ToolsCode.ChatTool.ui.loginWindow import Ui_loginWindow
from myMenu import MyMenu
import loginTool as log


class MyLogin(QWidget, Ui_loginWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.menu = None
        self.pushButton.clicked.connect(self.login)

    def login(self):
        id = self.lineEdit.text()
        pwd = self.lineEdit_2.text()
        if log.check(id, pwd):
            self.menu = MyMenu()
            self.menu.show()
            self.close()
        else:
            self.lineEdit_2.clear()
