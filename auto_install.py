import contextlib
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
from script.change_DPI import system_info, regedit_win7, regedit_win10, restore_DPI
from script.system_version import sys_version
from playsound import playsound
import threading

import sys
import ctypes
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
        self.network_shutdown = None       # 自动断网标识
        self.check_system()

        self.checkBox.setToolTip(
            '安装程序时将自动断开所有网络，安装完毕后自动恢复')    # checkbox鼠标悬停提示
        self.checkBox_2.setToolTip('关闭windows自动更新服务')
        self.checkBox_3.setToolTip('恢复鼠标右键菜单至经典模式(仅Win11)')

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

    def play_finish_sound(self):
        while True:
            playsound(join(getcwd(), 'app_pkg', 'sound', 'finish.wav'))
            

    def failure(self, _):
        self.stoptime()
        _translate = QtCore.QCoreApplication.translate
        if len(_) != 0:
            reply1 = QMessageBox.information(
                self,
                "程序运行完毕",
                f"程序运行完毕，安装失败的程序为：{','.join(_)}",
                QMessageBox.Ok,
            )
        else:
            if self.comboBox.currentText() == "装完提示":
                play = threading.Thread(target=self.play_finish_sound, args=())
                play.start()

            if self.comboBox.currentText() == "装完关机":
                system('shutdown -s -t 1')

            self.label_6.setText(_translate("MainWindow", "所有程序安装完毕"))
            reply2 = QMessageBox.information(
                self,
                "程序运行完毕",
                "所有程序成功安装,关闭本程序并注销系统恢复DPI...",
                QMessageBox.Ok,
            )
        if reply2 == QMessageBox.Ok:
            restore_DPI()
            system('shutdown -l')

    def disable_update(self):   # 关闭系统更新服务
        if bool(self.checkBox_2.isChecked()):
            for _ in ['NET STOP "wuauserv"', 'sc config "wuauserv" start= DISABLED']:
                system(_)

    def classic_context_menu(self):     # 恢复win11经典开始菜单
        if bool(self.checkBox_3.isChecked()):
            system(
                'reg add "HKCU\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32" /f')

    def check_system(self):
        if sys_version() == '11':
            self.checkBox_3.setEnabled(True)

    def pushButton_2_clicked(self):
        with contextlib.suppress(Exception):
            sound = threading.Thread(target=playsound, args=(
                join(getcwd(), 'app_pkg', 'sound', 'run_click.wav'),))
            sound.start()
            
        self.network_shutdown = bool(self.checkBox.isChecked())
        self.disable_update()
        self.classic_context_menu()
        self.checkBox.setVisible(False)     # 安装时将checkbox隐藏
        self.checkBox_2.setVisible(False)
        self.checkBox_3.setVisible(False)
        self.pushButton.setVisible(False)
        self.pushButton_2.setVisible(False)
        self.comboBox.setVisible(False)
        self.path = self.lineEdit.text()
        self.check_directory()
        self.install = New_Thread(
            self.path, screen_check, self.menu, self.network_shutdown)
        self.lineEdit.setEnabled(False)
        self.setMaximumSize(QtCore.QSize(415, 210))
        self.resize(415, 210)
        self.starttime()
        self.install.program_name.connect(self.change_program)
        self.install.start()
        self.install.failure.connect(self.failure)

    def pushButton_clicked(self):
        with contextlib.suppress(Exception):
            sound = threading.Thread(target=playsound, args=(
                join(getcwd(), 'app_pkg', 'sound', 'run_click.wav'),))
            sound.start()

        _translate = QtCore.QCoreApplication.translate
        self.path = QFileDialog.getExistingDirectory(None, "选择程序安装路径")
        self.path = self.path.replace('/', '\\')
        if self.path != '':
            self.lineEdit.setText(_translate("Mainwindow", self.path))

    def check_directory(self):
        if not isdir(self.path):
            mkdir(self.path)


if __name__ == '__main__':
    UAC = True
    if check_UAC():     # 检查UAC是否关闭
        UAC = False
        app = QApplication(sys.argv)
        QMessageBox.warning(
            None,
            "UAC未关闭",
            "程序将自动并关闭UAC与防火墙并重启，重启后请重新打开本软件",
            QMessageBox.Ok,
        )
        for _ in ['netsh advfirewall set allprofiles state off', 'reg add "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" /v "EnableLUA" /t REG_DWORD /d 0 /f']:
            system(_)

    DPI = True
    if check_DPI() != 96:       # 检查显示DPI是否设置为100
        DPI = False
        if system_info() == '7':
            regedit_win7()
        elif system_info() == '10':
            regedit_win10()

        app2 = QApplication(sys.argv)
        QMessageBox.warning(
            None,
            "DPI显示比例未设置",
            "程序将自动设置DPI并重启，重启后请重新打开本软件",
            QMessageBox.Ok,
        )

    if not UAC or not DPI:      # 任何一个选项不符合都要重启
        reply = QMessageBox.information(
            None, 'UAC或DPI未设置正确', '立即重启(Yes),无视错误继续运行(No)', QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            system('shutdown -r -t 1')
            sys.exit(0)

    screen_check = size().width < 1600
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()
