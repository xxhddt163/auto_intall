from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from ui import *
from os.path import isdir, join
from os import mkdir, system, getcwd
from pyautogui import size
from script.install_thread import New_Thread
from script.format_menu import format_menu
from script.load_menu import load_menu
from script.check_UAC import check_UAC
from script.check_DPI import check_DPI
from playsound import playsound

import sys
import warnings

from winrt import _winrt        # 防止与New_Thread模块进程冲突报错OleInitialize() failed:
_winrt.uninit_apartment()       # 防止与New_Thread模块进程冲突报错OleInitialize() failed:

warnings.simplefilter("ignore", UserWarning)
sys.coinit_flags = 2


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowIcon(QIcon('setup.ico'))
        desktop = QApplication.desktop()
        self.move(desktop.width()*0.03, desktop.height()
                  * 0.05)       # 设置窗口打开时在屏幕左上角
        self.setupUi(self)
        self.path = self.lineEdit.text()  # 程序安装位置
        self.sec = 0        # 记录秒
        self.min = 0        # 记录分
        self.pushButton.clicked.connect(
            self.pushButton_clicked)            # 浏览按钮
        self.pushButton_2.clicked.connect(
            self.pushButton_2_clicked)        # 安装按钮
        self.timer = QTimer()
        self.timer.timeout.connect(self.showtime)
        self.menu = load_menu()
        self.check = None       # 自动断网标识

    def showtime(self):
        """用label_3显示安装时间"""
        _translate = QtCore.QCoreApplication.translate
        self.sec += 10
        if self.sec == 60:
            self.sec = 0
            self.min += 1
        if self.sec == 0:
            self.label_3.setText(_translate(
                "MainWindow", f"{self.min}:0{self.sec}"))
        else:
            self.label_3.setText(_translate(
                "MainWindow", f"{self.min}:{self.sec}"))

    def starttime(self):
        """每隔10秒触发一次sle.timer.timeout"""
        self.timer.start(10000)

    def stoptime(self):
        """停止计时器计时"""
        self.timer.stop()

    def change_program(self, _):
        _translate = QtCore.QCoreApplication.translate
        self.label_6.setText(_translate(
            "MainWindow", f"正在安装{format_menu(_.split())[0]}..."))
        self.label_5.setText(_translate(
            "MainWindow", f"第 {self.menu.index(_) + 1} 个 共 {len(self.menu)} 个"))

    def failure(self, _):
        self.stoptime()
        _translate = QtCore.QCoreApplication.translate
        if len(_) != 0:
            reply = QMessageBox.information(
                self,
                "程序运行完毕",
                f"程序运行完毕，安装失败的程序为：{','.join(_)}",
                QMessageBox.Ok,
            )
        else:
            self.label_6.setText(_translate("MainWindow", "所有程序安装完毕"))
            reply = QMessageBox.information(
                self,
                "程序运行完毕",
                "所有程序成功安装,点击ok按钮关闭本程序",
                QMessageBox.Ok,
            )
        if reply == QMessageBox.Ok:
            self.close()
    
    def disable_update(self):   # 关闭系统更新服务
        if bool(self.checkBox_2.isChecked()):
            for _ in ['NET STOP "wuauserv"','sc config "wuauserv" start= DISABLED']:
                system(_)

    def pushButton_2_clicked(self):
        playsound(join(getcwd(), 'app_pkg', 'sound', 'run_click.wav'))
        self.check = bool(self.checkBox.isChecked())
        self.disable_update()
        self.checkBox.setVisible(False)     # 安装时将checkbox隐藏
        self.checkBox_2.setVisible(False)
        self.path = self.lineEdit.text()
        self.check_directory()
        self.install = New_Thread(self.path, screen_check, self.menu, self.check)
        self.lineEdit.setEnabled(False)
        self.pushButton.setEnabled(False)
        self.pushButton_2.setEnabled(False)
        self.setMaximumSize(QtCore.QSize(380, 210))
        self.resize(380, 210)
        self.starttime()
        self.install.program_name.connect(self.change_program)
        self.install.start()
        self.install.failure.connect(self.failure)

    def pushButton_clicked(self):
        playsound(join(getcwd(), 'app_pkg', 'sound', 'run_click.wav'))
        _translate = QtCore.QCoreApplication.translate
        self.path = QFileDialog.getExistingDirectory(None, "选择程序安装路径")
        self.path = self.path.replace('/', '\\')
        if self.path != '':
            self.lineEdit.setText(_translate("Mainwindow", self.path))

    def check_directory(self):
        if not isdir(self.path):
            mkdir(self.path)


if __name__ == '__main__':
    if check_UAC():     # 检查UAC是否关闭
        app = QApplication(sys.argv)
        QMessageBox.warning(
            None,
            "UAC未关闭",
            "程序将自动并关闭UAC与防火墙并重启，重启后请重新打开本软件",
            QMessageBox.Ok,
        )
        for _ in ['netsh advfirewall set allprofiles state off', 'reg add "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" /v "EnableLUA" /t REG_DWORD /d 0 /f', 'shutdown -r -t 1']:
            system(_)
    if check_DPI() != 96:       # 检查显示DPI是否设置为100
        app = QApplication(sys.argv)
        QMessageBox.warning(
            None,
            "DPI显示比例未设置",
            "请将显示比例改为100%，注销后重新打开本程序，修改方法：桌面右键->显示设置->缩放与布局",
            QMessageBox.Ok,
        )
        sys.exit(0)
    screen_check = size().width < 1600
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()
