from os.path import join
from os import getcwd
from os import system
from pywinauto import Application
from time import sleep

def t20_cra():
    program = Application().start(join(getcwd(), "app_pkg", 'T20', 'crack', 'crack.exe'))
    temp = program.top_window()['\n点我Button'].wait('ready', timeout=5)
    temp.click_input()
    sleep(1)
    system('taskkill /IM crack.exe /F')