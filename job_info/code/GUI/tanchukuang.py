from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit,
    QInputDialog, QApplication)
import sys

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.btn = QPushButton('登录', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)

        self.le = QLineEdit(self)
        self.le.move(130, 22)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('医学招聘数据抓取工具')
        self.show()


    def showDialog(self):

        text, ok = QInputDialog.getText(self, '身份验证',
            '输入管理员密码:')

        if ok:
            # 登录成功
            self.le.setText(str(text))
        else:
            exit()
        print(text)


app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())