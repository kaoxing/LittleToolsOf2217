from PyQt5.QtWidgets import QWidget
from ToolsCode.ChatTool.ui.chatContent import Ui_widget


class MyChatContent(QWidget, Ui_widget):
    def __init__(self, str):
        super().__init__()
        self.setupUi(self)
        self.label.setText(str)

