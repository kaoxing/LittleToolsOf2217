from PyQt5.QtWidgets import QMainWindow
from ui.menu import Ui_mainWindow
from ToolsCode.ChatTool.myLogin import MyLogin


class MyMenu(QMainWindow, Ui_mainWindow):
    def __init__(self):
        super().__init__()
        self.chatLogin = None
        self.setupUi(self)
        self.pushButton_menu1.clicked.connect(self.menu1_method)
        self.pushButton_menu3.clicked.connect(self.show_chat)

    def menu1_method(self):
        self.lineEdit.setText("menu1")

    def show_chat(self):
        print("here")
        self.chatLogin = MyLogin()
        self.chatLogin.show()
