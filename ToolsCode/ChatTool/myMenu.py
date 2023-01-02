from PyQt5.QtWidgets import QMainWindow
from ToolsCode.ChatTool.ui.myUi import Ui_mainWindow
from myChatContent import MyChatContent


class MyMenu(QMainWindow, Ui_mainWindow):
    def __init__(self):
        super().__init__()
        self.chat = None
        self.setupUi(self)
        self.pushButton_menu1.clicked.connect(self.menu1_method)
        self.pushButton_menu3.clicked.connect(self.show_chat)

    def menu1_method(self):
        self.lineEdit.setText("menu1")

    def show_chat(self):
        print("here")
        self.chat = MyChatContent("KaoXing")
        self.chat.show()
