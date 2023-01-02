from PyQt5.QtWidgets import QMainWindow
from ToolsCode.Main.ui.menu import Ui_mainWindow
from ToolsCode.ChatTool.myLogin import MyLogin


class MyMenu(QMainWindow, Ui_mainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.chat=None
        self.pushButton_menu1.clicked.connect(self.set_page0)
        self.pushButton_menu2.clicked.connect(self.set_page1)
        self.pushButton_menu3.clicked.connect(self.set_page2)
        self.pushButton_startChat.clicked.connect(self.startChat)

    def set_page0(self):
        self.stackedWidget.setCurrentIndex(0)

    def set_page1(self):
        self.stackedWidget.setCurrentIndex(1)

    def set_page2(self):
        self.stackedWidget.setCurrentIndex(2)

    def startChat(self):
        self.chat = MyLogin()
        self.chat.show()

