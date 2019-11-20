from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListView, QMessageBox, QPushButton, QLineEdit,QInputDialog
from PyQt5.QtCore import QStringListModel,QThread
import sys
from core import *

class ListViewDemo(QWidget):
    college_list = college_info.keys()
    def __init__(self, parent=None):
        super(ListViewDemo, self).__init__(parent)
        self.setWindowTitle("医学招聘数据抓取工具")
        self.resize(300, 270)

        layout = QVBoxLayout()
        self.showDialog()
        # download_single_collage_info('河北医科大学')

        listView = QListView()  # 创建一个listview对象
        slm = QStringListModel()  # 创建mode
        # self.qList = ['Item 1', 'Item 2', 'Item 3', 'Item 4']  # 添加的数组数据
        self.qList = self.college_list
        slm.setStringList(self.qList)  # 将数据设置到model
        listView.setModel(slm)  ##绑定 listView 和 model
        listView.clicked.connect(self.clickedlist)  # listview 的点击事件
        layout.addWidget(listView)  # 将list view添加到layout
        self.setLayout(layout)  # 将lay 添加到窗口

    def clickedlist(self, qModelIndex):
        # QMessageBox.information(self, "QListView", "你选择了: " + self.qList[qModelIndex.row()])
        # print("点击的是：" + str(qModelIndex.row()))
        print(qModelIndex.row())
        # 调用下载函数
        self.run_one_download_task(qModelIndex.row())

    def showDialog(self):

        text, ok = QInputDialog.getText(self, '医学招聘数据抓取工具-身份验证',
            '请输入管理员密码:')
        if ok:
            # 登录成功
            print("登录进来了,密码是",str(text))
            # self.le.setText(str(text))
        else:
            exit()
        print(text)


    def run_one_download_task(self,index):
        print("当前正在下载")
        print(list(college_info.keys())[index])
        # 创建一个新的线程
        thread = Thread()
        thread.start(list(college_info.keys())[index])

        # print()

class Thread(QThread):

    def __init__(self):
        super().__init__()

    def run(self,choice_college):
        # 线程相关代码
        download_single_collage_info(choice_college)
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = ListViewDemo()
    win.show()
    sys.exit(app.exec_())