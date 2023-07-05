'''
Author: xxh
coding: utf-8
Date: 2022-03-08 22:30:38
LastEditTime: 2022-09-24 22:38:22
FilePath: \auto_install\script\install_thread.py
'''
from PyQt5.QtCore import pyqtSignal, QThread
import sys
from log import Logger
import traceback
from PyQt5.QtWidgets import QApplication, QMessageBox
import os
from script.set_network import Change_interface


from install_script.install import install_3DMAX, install_CAD2014, install_CAD2007, install_T20, install_CAD2019
from install_script.install import install_PSCC2019, install_PRCC2020, intall_163music, install_QQmusic, install_Kugou, install_Xunlei, install_SogouPY, install_cdr2020
from install_script.install import install_DVN, intall_OFFICE2021LTSC, install_WPS, install_360drv, install_Chrome, install_Lensto, install_TXvideo, install_IQIYI, install_PSCS3
from install_script.install import install_QQ, install_AI2021, install_DC2021, install_ID2021, install_AECC2019, install_baidu_Netdisk, install_Wechat, install_Dtalk, install_Winrar

from winrt import _winrt        # 防止OleInitialize() failed报错

_winrt.uninit_apartment()      # 防止与主函数OleInitialize() failed报错

c = Change_interface()      # 创建切换网卡状态的全局变量

class New_Thread(QThread):
    program_name = pyqtSignal(str)    # 当前安装的程序名
    failure = pyqtSignal(list)         # 安装失败的程序列表

    def __init__(self, path, screen_check, install_list, check_stat):
        super(New_Thread, self).__init__()
        self.path = path
        self.screen_check = screen_check
        self.menu = install_list
        self.check_stat = check_stat

    def run(self):
        try:
            if self.check_stat:
                c.change_interface()        # 将有网络的网卡禁用
            failure = []  # 保存安装失败的软件名称
            menu = self.menu  # 读取安装目录下的menu.txt获取需要安装的文件
            menu_change = menu.copy()
            for each in menu:
                self.program_name.emit(each)

                exec({
                    'QQ': "install_QQ(choose=self.path, prom_name=each, menu_change=menu_change, failure=failure)",
                    'AI2021': "install_AI2021(choose=self.path, prom_name=each, menu_change=menu_change, failure=failure, full_screen=self.screen_check)",
                    'DC2021': "install_DC2021(choose=self.path, prom_name=each, menu_change=menu_change, failure=failure, full_screen=self.screen_check)",
                    'ID2021': "install_ID2021(choose=self.path, prom_name=each, menu_change=menu_change, failure=failure, full_screen=self.screen_check)",
                    'AECC2019': "install_AECC2019(choose=self.path, prom_name=each, menu_change=menu_change, failure=failure, full_screen=self.screen_check)",
                    'baidu_Netdisk': "install_baidu_Netdisk(choose=self.path, prom_name=each, menu_change=menu_change, failure=failure, full_screen=self.screen_check)",
                    'Wechat': "install_Wechat(choose=self.path, prom_name=each, menu_change=menu_change, failure=failure, full_screen=self.screen_check)",
                    'Dtalk': "install_Dtalk(choose=self.path, prom_name=each, menu_change=menu_change, failure=failure)",
                    'Winrar': "install_Winrar(choose=self.path, prom_name=each, menu_change=menu_change, failure=failure)",
                    'VCRedist': "install_DVN(choose=self.path, prom_name=each, menu_change=menu_change, failure=failure)",
                    'DX': "install_DVN(choose=self.path, prom_name=each, menu_change=menu_change, failure=failure)",
                    'NF3': "install_DVN(choose=self.path, prom_name=each, menu_change=menu_change, failure=failure)",
                    'OFFICE2021LTSC': "intall_OFFICE2021LTSC(choose=self.path, prom_name=each, menu_change=menu_change, failure=failure, full_screen=self.screen_check)",
                    'WPS': "install_WPS(choose=self.path, prom_name=each, menu_change=menu_change, failure=failure, full_screen=self.screen_check)",
                    '360drv': "install_360drv(choose=self.path, prom_name=each, menu_change=menu_change, failure=failure, full_screen=self.screen_check)",
                    'Chrome': "install_Chrome(prom_name=each, menu_change=menu_change)",
                    'Lensto': "install_Lensto(choose=self.path, prom_name=each, menu_change=menu_change, failure=failure, full_screen=self.screen_check)",
                    'TXvideo': "install_TXvideo(choose=self.path, prom_name=each, menu_change=menu_change, failure=failure)",
                    'IQIYI': "install_IQIYI(choose=self.path, prom_name=each, menu_change=menu_change, failure=failure)",
                    'PSCS3': "install_PSCS3(choose=self.path, prom_name=each, menu_change=menu_change, failure=failure)",
                    'PSCC2019': "install_PSCC2019(prom_name=each, menu_change=menu_change)",
                    'PRCC2020': "install_PRCC2020(choose=self.path, prom_name=each, menu_change=menu_change, failure=failure, full_screen=self.screen_check)",
                    '163music': "intall_163music(choose=self.path, prom_name=each, menu_change=menu_change, failure=failure, full_screen=self.screen_check)",
                    'QQmusic': "install_QQmusic(choose=self.path, prom_name=each, menu_change=menu_change, failure=failure, full_screen=self.screen_check)",
                    'Kugou': "install_Kugou(choose=self.path, prom_name=each, menu_change=menu_change, failure=failure, full_screen=self.screen_check)",
                    'Xunlei': "install_Xunlei(choose=self.path, prom_name=each, menu_change=menu_change, failure=failure, full_screen=self.screen_check)",
                    'SougouPY': "install_SogouPY(choose=self.path, prom_name=each, menu_change=menu_change, failure=failure, full_screen=self.screen_check)",
                    # '2345pinyin':"install_2345PY(choose=self.path, prom_name=each, menu_change=menu_change, failure=failure, full_screen=self.screen_check)",
                    '3DMAX2014': "install_3DMAX(choose=self.path, prom_name=each, menu_change=menu_change, failure=failure)",
                    'CAD2014': "install_CAD2014(choose=self.path, prom_name=each, menu_change=menu_change, failure=failure)",
                    'CAD2019': "install_CAD2019(choose=self.path, prom_name=each, menu_change=menu_change, failure=failure)",
                    'CAD2007': "install_CAD2007(choose=self.path, prom_name=each, menu_change=menu_change, failure=failure)",
                    'T20': "install_T20(choose=self.path, prom_name=each, menu_change=menu_change, failure=failure)",
                    'cdr2020': "install_cdr2020(choose=self.path, prom_name=each, menu_change=menu_change, failure=failure)"

                }[each])
            if self.check_stat:
                c.change_interface()        # 安装完程序后恢复网卡
            self.failure.emit(failure)
        except Exception as e:
            if self.check_stat:
                c.change_interface()        # 程序异常退出前恢复网路
            logfile = os.path.join(os.getcwd(), 'error.log')        # 错误日志
            log = Logger(logfile).logger
            log.error(f"{e.args}:--->{traceback.format_exc()}")
            app = QApplication(sys.argv)
            QMessageBox.warning(
                None,
                "程序运行错误",
                "程序运行错误,请查看错误日志",
                QMessageBox.Ok,
            )
            sys.exit(1)
