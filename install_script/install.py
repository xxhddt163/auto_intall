from pywinauto import Application, findwindows
from pyautogui import hotkey
from pyperclip import copy
from os.path import join
from os import getcwd
from time import sleep
from os import system

from script.install import install
from script.kill_program import kill_program
from script.txt_change import txt_change
from script.format_menu import format_menu
from script.install_from_png import install_from_png
from script.system_version import sys_version
from script.install_from_topwindow import install_from_topwindow
from script.simple_install import simple_install

from crack.office2021LTSC_cra import office2021LTSC_crack
from crack.pscc2019_cra import ps_crack
from crack.max2020_cra import cra_3dmax
from crack.cad2007_cra import cad2007_cra
from crack.t20_cra import t20_cra
from crack.cad2019_cra import cad2019_cra
from crack.cad2020_cra import cad2020_cra
from crack.cad2014_cra import cra_cad2014

def install_CAD2019(choose, prom_name, menu_change, failure):
    step = {0: ["ListBox3", 'click', 30],
            1: ["我接受Button", 'click', 6],
            2: ["下一步Button", 'click', 6],
            3: ["ADSK_ACRDN_GROUP", 'click2', 6],     # 展开第一项的三角箭头
            4: ["CheckBox", 'click', 6],    # 关闭3个子组件的√
            5: ["CheckBox2", 'click', 6],
            6: ["CheckBox3", 'click', 6],
            7: ["ADSK_ACRDN_GROUP", 'click2', 6],    # 合并第一项的三角箭头
            # 8: ["安装路径:Edit", r"d:\dddd", 'edit', 6],
            8: ["安装路径:Edit", join(choose, prom_name), 'edit', 6],
            9: ["安装Button", 'click', 6]}

    sleep_time = [5, 1, 1, 3, 1, 1, 1, 3, 2, 1]

    setup_path = join(getcwd(), "app_pkg", 'CAD2019', "Setup.exe")
    # startfile(setup_path)
    copy(setup_path)
    hotkey("win", "r")
    sleep(2)
    hotkey("ctrl", "v")
    sleep(1)
    hotkey("enter")

    time = 20
    while time >= 0:
        try:
            program = Application().connect(title="Autodesk® AutoCAD® 2019")
        except:
            sleep(1)
            time -= 1
        else:
            break
    if simple_install(window_backend='win32', step=step, program=program, sleep_time=sleep_time):
        while True:
            try:
                temp = Application().connect(title_re='文件正在使用')
                if temp.top_window().window(title='忽略(&I)').exists():
                    temp.top_window()['忽略(&I)'].click_input()
            except:
                pass

            if program.top_window().child_window(title="立即启动").exists():
                program.top_window().child_window(title="立即启动").wait("ready", timeout=10)
                program.top_window()['立即启动'].click_input()
                txt_change(prom_name=prom_name, menu_change=menu_change)
                break
            else:
                sleep(3)
        cad2019_cra()
        sleep(3)
        system('taskkill /IM acad.exe /F')
        sleep(1)
        system('taskkill /IM LMU.exe /F')
    else:
        failure.extend(format_menu(prom_name.split()))

def install_CAD2020(choose, prom_name, menu_change, failure):
    step = {0: ["ListBox3", 'click', 30],       # 在此计算机上安装
            1: ["我接受Button", 'click', 6],
            2: ["下一步Button", 'click', 6],
            3: ["安装路径:Edit", join(choose, prom_name), 'edit', 6],
            4: ["安装Button", 'click', 6]}

    sleep_time = [5, 1, 1, 3, 1, 1, 1, 3, 2, 1]

    setup_path = join(getcwd(), "app_pkg", 'CAD2020', "Setup.exe")
    # startfile(setup_path)
    copy(setup_path)
    hotkey("win", "r")
    sleep(2)
    hotkey("ctrl", "v")
    sleep(1)
    hotkey("enter")

    time = 20
    while time >= 0:
        try:
            program = Application().connect(title="Autodesk® AutoCAD® 2020")
        except:
            sleep(1)
            time -= 1
        else:
            break
    if simple_install(window_backend='win32', step=step, program=program, sleep_time=sleep_time):
        while True:
            try:
                temp = Application().connect(title_re='文件正在使用')
                if temp.top_window().window(title='忽略(&I)').exists():
                    temp.top_window()['忽略(&I)'].click_input()
            except:
                pass

            if program.top_window().child_window(title="立即启动").exists():
                program.top_window().child_window(title="立即启动").wait("ready", timeout=10)
                program.top_window()['立即启动'].click_input()
                txt_change(prom_name=prom_name, menu_change=menu_change)
                break
            else:
                sleep(3)
        cad2020_cra()
        sleep(3)
        system('taskkill /IM acad.exe /F')
        sleep(1)
        system('taskkill /IM LMU.exe /F')
    else:
        failure.extend(format_menu(prom_name.split()))





def install_cdr2020(choose, prom_name, menu_change, failure):
    try:
        setup_program = Application(backend="uia").start(
            join(getcwd(), 'app_pkg', 'cdr2020', 'setup', 'Setup.exe'))      # 启动cdr安装程序
        cdr_crack = Application(backend="win32").start(
            join(getcwd(), 'app_pkg', 'cdr2020', 'crack', 'crack.exe'))          # 启动cdr注册机

        """设置注册机并获取key"""
        cdr_crack.window(title_re="Corel 产品注册机").wait("ready", timeout=10)
        cdr_crack_temp = cdr_crack.window(title_re="Corel 产品注册机")
        cdr_crack_temp.set_focus()   # 设置该程序为活动
        cdr_crack_temp.wait("ready", timeout=5)
        cdr_crack_temp.ComboBox.select(7)       # 选择下拉框为cdr2020
        cdr_crack_temp.Button2.wait("ready", timeout=3)
        cdr_crack_temp.Button2.click_input()
        cdr_crack_temp.Edit4.wait("ready", timeout=3)
        key = cdr_crack_temp.Edit4.window_text()        # 注册机生成的序列号

        setup_program.window(title_re="CorelDRAW Graphics Suite 2020").wait(
            "ready", timeout=10)
        setup_program_temp = setup_program.window(
            title_re="CorelDRAW Graphics Suite 2020")
        setup_program_temp.set_focus()
        setup_program_temp.Edit2.wait("ready", timeout=30)
        setup_program_temp.Edit2.set_text(key)              # 填入注册机生成的序列号
        setup_program_temp['下一步 (N)Button'].wait("ready", timeout=3)
        setup_program_temp['下一步 (N)Button'].click_input()
        setup_program_temp.Hyperlink2.wait("ready", timeout=3)
        setup_program_temp.Hyperlink2.click_input()         # 点击自定义安装
        setup_program_temp.CheckBox2.wait("ready", timeout=3)
        setup_program_temp.CheckBox2.click_input()          # 取消勾选位图插图编辑器
        setup_program_temp.CheckBox3.wait("ready", timeout=3)
        setup_program_temp.CheckBox3.click_input()          # 取消勾选高级屏幕截图
        setup_program_temp.CheckBox4.wait("ready", timeout=3)
        setup_program_temp.CheckBox4.click_input()          # 取消勾选字体管理器
        setup_program_temp['下一步 (N)Button'].wait("ready", timeout=3)
        setup_program_temp['下一步 (N)Button'].click_input()
        setup_program_temp.CheckBox1.wait("ready", timeout=3)
        setup_program_temp.CheckBox1.click_input()          # 取消勾选实用工具
        setup_program_temp.CheckBox2.wait("ready", timeout=3)
        setup_program_temp.CheckBox2.click_input()          # 取消勾选启用增强的EPS兼容性
        setup_program_temp['下一步 (N)Button'].wait("ready", timeout=3)
        setup_program_temp['下一步 (N)Button'].click_input()
        setup_program_temp.Edit.wait("ready", timeout=3)
        setup_program_temp.Edit.set_text(join(choose, prom_name))
        setup_program_temp['立即安装 (I)'].wait("ready", timeout=3)
        setup_program_temp['立即安装 (I)'].click_input()

        while setup_program_temp.exists():      # 每隔3秒检查cdr是否安装完毕，安装完毕跳出循环
            sleep(3)
        while not findwindows.find_elements(title_re="CorelDRAW 2020"):
            sleep(3)

        cdr = Application(backend="uia").connect(title_re="CorelDRAW 2020")
        cdr_temp = cdr.window(title_re="CorelDRAW 2020")
        cdr_temp['同意 (A)'].wait("ready", timeout=10)
        cdr_temp['同意 (A)'].click_input()
        sleep(5)
        cdr_crack_temp.set_focus()
        cdr_crack_temp['计算激活代码Button'].wait("ready", timeout=10)
        cdr_crack_temp['计算激活代码Button'].click_input()
        sleep(2)
        cdr_crack.kill()
        sleep(2)
        cdr.kill()
        sleep(2)
        no_sign = Application(backend="win32").start(
            join(getcwd(), 'app_pkg', 'cdr2020', 'no_sign', 'no_sign.exe'))        # 打开免登录补丁
        no_sign.window(title_re="CorelDRAW 2020_64Bit").wait(
            "ready", timeout=10)
        no_sign_temp = no_sign.window(title_re="CorelDRAW 2020_64Bit")
        no_sign_temp['应用Button'].wait("ready", timeout=10)
        no_sign_temp['应用Button'].click_input()
        no_sign.kill()
        txt_change(prom_name=prom_name,
                   menu_change=menu_change)
    except RuntimeError:
        failure.extend(format_menu(prom_name.split()))


def install_QQ(choose, prom_name, menu_change, failure):
    """_summary_

    Args:
        choose (str): 选择的安装目录
        prom_name (str): 程序名
        menu_change (_type_): 选择的安装文件的列表
        failure (_type_): 安装失败的程序
    """
    main_window = ["腾讯QQ安装向导", "win32", "QQ"]
    step = {0: ["自定义选项", 'click', 15],
            # 1: ["添加到快速启动栏", 'click', 6],
            1: ["开机自动启动", 'click', 6],      
            2: ['', 'edit', 6],
            3: ["阅读并同意", 'click', 6],
            4: ["立即安装", 'click', 6],
            5: ["完成安装", 'click', 60]}

    program = Application(backend=main_window[1]).start(
        join(getcwd(), 'app_pkg', 'QQ', 'QQ.exe'))

    if install(main_window=main_window[0], window_backend=main_window[1], step=step, program=program, install_path=join(choose, prom_name), edit_value=2):
        if kill_program(name='QQ.exe'):
            system('taskkill /IM QQ.exe /F')
        txt_change(prom_name=prom_name,
                   menu_change=menu_change)  # 安装成功修改menu文件
    else:
        failure.extend(format_menu(prom_name.split()))  # 安装失败记录安装失败程序


def install_AI2021(choose, prom_name, menu_change, failure, full_screen):
    sleep_time = [10, 70]  # 各图片的等待时间
    grayscale = [False, True]  # 各图片是否使用灰度搜索
    skewing = [[0, 0], [0, 0]]  # x、y坐标偏移

    Application().start(join(getcwd(), "app_pkg", prom_name, "Set-up"))  # 打开指定的安装程序

    result = install_from_png(app_name=prom_name, edit_index=3,
                              confidence=0.8, install_path=choose, sleep_time_list=sleep_time,
                              grayscale_list=grayscale, skewing_list=skewing, paste_identi=True, full_screen=full_screen)  # 采用全图片匹配

    if result:
        txt_change(prom_name=prom_name, menu_change=menu_change)
    else:
        failure.extend(format_menu(prom_name.split()))


def install_DC2021(choose, prom_name, menu_change, failure, full_screen):
    sleep_time = [10, 90]  # 各图片的等待时间
    grayscale = [False, True]  # 各图片是否使用灰度搜索
    skewing = [[0, 0], [0, 0]]  # x、y坐标偏移

    setup_path = join(getcwd(), "app_pkg", prom_name, "Set-up.exe")
    # startfile(setup_path)
    copy(setup_path)
    hotkey("win", "r")
    sleep(2)
    hotkey("ctrl", "v")
    sleep(1)
    hotkey("enter")

    result = install_from_png(app_name=prom_name, edit_index=3,
                              confidence=0.8, install_path=choose, sleep_time_list=sleep_time,
                              grayscale_list=grayscale, skewing_list=skewing, paste_identi=True, full_screen=full_screen)  # 采用全图片匹配

    if result:
        txt_change(prom_name=prom_name, menu_change=menu_change)
    else:
        failure.extend(format_menu(prom_name.split()))


def install_ID2021(choose, prom_name, menu_change, failure, full_screen):
    sleep_time = [10, 90]  # 各图片的等待时间
    grayscale = [False, True]  # 各图片是否使用灰度搜索
    skewing = [[0, 0], [0, 0]]  # x、y坐标偏移

    Application().start(join(getcwd(), "app_pkg", prom_name, "Set-up"))  # 打开指定的安装程序

    result = install_from_png(app_name=prom_name, edit_index=3,
                              confidence=0.8, install_path=choose, sleep_time_list=sleep_time,
                              grayscale_list=grayscale, skewing_list=skewing, paste_identi=True, full_screen=full_screen)  # 采用全图片匹配

    if result:
        txt_change(prom_name=prom_name, menu_change=menu_change)
    else:
        failure.extend(format_menu(prom_name.split()))


def install_AECC2019(choose, prom_name, menu_change, failure, full_screen):
    sleep_time = [10, 180]  # 各图片的等待时间
    grayscale = [False, True]  # 各图片是否使用灰度搜索
    skewing = [[0, 0], [0, 0]]  # x、y坐标偏移

    Application().start(join(getcwd(), "app_pkg", prom_name, "Set-up"))  # 打开指定的安装程序

    result = install_from_png(app_name=prom_name, edit_index=3,
                              confidence=0.8, install_path=choose, sleep_time_list=sleep_time,
                              grayscale_list=grayscale, skewing_list=skewing, paste_identi=True, full_screen=full_screen)  # 采用全图片匹配

    if result:
        txt_change(prom_name=prom_name, menu_change=menu_change)
    else:
        failure.extend(format_menu(prom_name.split()))


def install_baidu_Netdisk(choose, prom_name, menu_change, failure, full_screen):
    sleep_time = [60, 20, 20]  # 各图片的等待时间
    grayscale = [True, True, True]  # 各图片是否使用灰度搜索
    skewing = [[200, 0], [0, 0], [0, 0]]  # x、y坐标偏移

    Application().start(join(getcwd(), "app_pkg", prom_name, prom_name))  # 打开指定的安装程序

    png_file_name = "_shot" if sys_version() in ["10", "11"] else "_shot_win7"
    result = install_from_png(app_name=prom_name, edit_index=0, png_file_name=png_file_name,
                              confidence=0.8, install_path=choose, sleep_time_list=sleep_time,
                              grayscale_list=grayscale, skewing_list=skewing, paste_identi=True, full_screen=full_screen)  # 采用全图片匹配
    if result:
        txt_change(prom_name=prom_name, menu_change=menu_change)
        sleep(2)
        if kill_program(name='BaiduNetdisk.exe', count=90):
            sleep(2)
            system('taskkill /IM BaiduNetdisk.exe /F')
    else:
        failure.extend(format_menu(prom_name.split()))


def install_Wechat(choose, prom_name, menu_change, failure, full_screen):
    sleep_time = [60, 10, 10, 10, 20]  # 各图片的等待时间
    grayscale = [True, True, True, False, False]  # 各图片是否使用灰度搜索
    skewing = [[0, 0], [0, 0], [-300, 0], [0, 0], [0, 0]]  # x、y坐标偏移

    Application().start(join(getcwd(), 'app_pkg', 'wechat', 'wechat.exe'))  # 打开指定的安装程序

    png_file_name = "_shot"
    result = install_from_png(app_name=prom_name, edit_index=2, png_file_name=png_file_name,
                              confidence=0.8, install_path=choose, sleep_time_list=sleep_time,
                              grayscale_list=grayscale, skewing_list=skewing, paste_identi=True, full_screen=full_screen, longtime_wait_file_name='3.png')  # 采用全图片匹配
    if result:
        txt_change(prom_name=prom_name, menu_change=menu_change)
        system('taskkill /IM WeChat.exe /F')
    else:
        failure.extend(format_menu(prom_name.split()))


def install_Dtalk(choose, prom_name, menu_change, failure, full_screen):
    sleep_time = [10, 10, 10, 10, 70, 10, 10, 10]  # 各图片的等待时间
    grayscale = [True, True, True, False, False, False, False, False]  # 各图片是否使用灰度搜索
    skewing = [[0, 0], [0, 0], [-300, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]  # x、y坐标偏移

    Application().start(join(getcwd(), 'app_pkg', 'Dtalk', 'Dtalk.exe'))  # 打开指定的安装程序

    png_file_name = "_shot"
    result = install_from_png(app_name=prom_name, edit_index=2, png_file_name=png_file_name,
                              confidence=0.8, install_path=choose, sleep_time_list=sleep_time,
                              grayscale_list=grayscale, skewing_list=skewing, paste_identi=True, full_screen=full_screen, longtime_wait_file_name='3.png')  # 采用全图片匹配
    if result:
        txt_change(prom_name=prom_name, menu_change=menu_change)
    else:
        failure.extend(format_menu(prom_name.split()))


def install_Winrar(choose, prom_name, menu_change, failure):
    main_window = ["WinRAR 5.91", "win32", 10]
    step = {0: ["", "Edit", 'edit', 6],
            1: ["安装", "Button", 'click', 6]}

    program = Application(backend=main_window[1]).start(
        join(getcwd(), 'app_pkg', 'Winrar', 'Winrar.exe'))
    sleep(2)
    if install(main_window=main_window[0], window_backend=main_window[1], step=step, program=program,
               install_path=join(choose, prom_name), edit_value=0, special=True):
        time = 6
        while time >= 0:
            try:
                temp = Application().connect(title="WinRAR 简体中文版安装")
            except:
                sleep(1)
                time -= 1
            else:  # 未抛出异常时说明程序成功链接
                for button in ["确定", "完成"]:
                    temp2 = temp.window(title='WinRAR 简体中文版安装').child_window(title=button).wait('ready',
                                                                                                timeout=30)
                    temp2.click()
                break
        # 安装成功修改menu文件
        txt_change(prom_name=prom_name, menu_change=menu_change)
    else:
        failure.extend(format_menu(prom_name.split()))  # 安装失败记录安装失败程序


def install_DVN(choose, prom_name, menu_change, failure):
    main_window = "win32"
    step = {0: ["确定", 'click', 10],
            1: ["是(&Y)", 'click', 10]}
    sleep_time = [1, 0]
    program = Application(backend=main_window).start(
        join(getcwd(), 'app_pkg', prom_name, prom_name))

    if install_from_topwindow(window_backend=main_window, step=step, program=program,
                              install_path=join(choose, prom_name), sleep_time=sleep_time):
        ok_dict = {'DX': 'DirectX 9.0c 安装完成！程序即将退出',
                   'VCRedist': 'Visual C++ 运行库 安装完成！程序即将退出',
                   'NF3': '.Net Framework 安装完成！程序即将退出'}
        # 安装成功修改menu文件
        txt_change(prom_name=prom_name, menu_change=menu_change)
        time = 60
        while time >= 0:
            try:
                if program.window(title_re='信息').child_window(title=ok_dict[prom_name]).exists():
                    break
            except:
                sleep(1)
                time -= 1
        program.window(title_re='信息').child_window(
            title=ok_dict[prom_name]).wait('ready', timeout=80)
        program.window(title_re='信息').child_window(
            title="确定").click_input()
    else:
        failure.extend(format_menu(prom_name.split()))  # 安装失败记录安装失败程序


def intall_OFFICE2021LTSC(choose, prom_name, menu_change, failure, full_screen):
    sleep_time = [300]  # 各图片的等待时间
    grayscale = [True]  # 各图片是否使用灰度搜索
    skewing = [[0, 0]]  # x、y坐标偏移

    setup_path = join(getcwd(), "app_pkg", prom_name, "office", "setup.bat")
    copy(setup_path)
    hotkey("win", "r")
    sleep(2)
    hotkey("ctrl", "v")
    sleep(1)
    hotkey("enter")

    png_file_name = "_shot"
    result = install_from_png(app_name=prom_name, edit_index=4, png_file_name=png_file_name,
                              confidence=0.8, install_path=choose, sleep_time_list=sleep_time,
                              grayscale_list=grayscale, skewing_list=skewing, paste_identi=True, full_screen=full_screen, longtime_wait_file_name='5.png')  # 采用全图片匹配
    if result:
        txt_change(prom_name=prom_name, menu_change=menu_change)
        office2021LTSC_crack()
    else:
        failure.extend(format_menu(prom_name.split()))


def install_WPS(choose, prom_name, menu_change, failure, full_screen):
    sleep_time = [30, 10, 10, 10]  # 各图片的等待时间
    grayscale = [True, True, False, False]  # 各图片是否使用灰度搜索
    skewing = [[0, 0], [0, 0], [-200, 0], [0, 0]]  # x、y坐标偏移

    Application().start(join(getcwd(), "app_pkg", 'WPS',
                             'WPS_Setup_19770.exe'))  # 打开指定的安装程序

    png_file_name = "_shot" if sys_version() in ["10", "11"] else "_shot_win7"
    result = install_from_png(app_name=prom_name, edit_index=2, png_file_name=png_file_name,
                              confidence=0.6, install_path=choose, sleep_time_list=sleep_time,
                              grayscale_list=grayscale, skewing_list=skewing, paste_identi=True, full_screen=full_screen, longtime_wait_file_name= '2.png')  # 采用全图片匹配
    if result:
        txt_change(prom_name=prom_name, menu_change=menu_change)
        sleep(2)
        if kill_program(name='wps.exe',count=240):
            sleep(2)
            system('taskkill /IM wps.exe /F')
    else:
        failure.extend(format_menu(prom_name.split()))


def install_360drv(choose, prom_name, menu_change, failure, full_screen):
    sleep_time = [10, 10, 10, 10, 20, 10]  # 各图片的等待时间
    grayscale = [False, False, False, False, False, False]  # 各图片是否使用灰度搜索
    skewing = [[0, 0], [0, 0], [-300, 0], [0, 0], [0, 0], [0, 0]]  # x、y坐标偏移

    Application().start(join(getcwd(), 'app_pkg', prom_name, prom_name))  # 打开指定的安装程序

    png_file_name = "_shot"
    result = install_from_png(app_name=prom_name, edit_index=2, png_file_name=png_file_name,
                              confidence=0.8, install_path=choose, sleep_time_list=sleep_time,
                              grayscale_list=grayscale, skewing_list=skewing, paste_identi=True, full_screen=full_screen)  # 采用全图片匹配
    if result:
        txt_change(prom_name=prom_name, menu_change=menu_change)
    else:
        failure.extend(format_menu(prom_name.split()))


def install_Chrome(prom_name, menu_change):
    program = Application(backend='win32').start(
        join(getcwd(), 'app_pkg', prom_name, prom_name))
    txt_change(prom_name=prom_name, menu_change=menu_change)
    if kill_program(name='chrome.exe'):
        system('taskkill /IM chrome.exe /F')


def install_Lensto(choose, prom_name, menu_change, failure, full_screen):
    sleep_time = [20, 10, 10, 60]  # 各图片的等待时间
    grayscale = [True, False, False, False]  # 各图片是否使用灰度搜索
    skewing = [[0, 0], [-300, 0], [0, 0], [0, 0]]  # x、y坐标偏移

    Application().start(join(getcwd(), "app_pkg", prom_name,
                             prom_name))  # 打开指定的安装程序
    result = install_from_png(app_name=prom_name, edit_index=1,
                              confidence=0.8, install_path=choose, sleep_time_list=sleep_time,
                              grayscale_list=grayscale, skewing_list=skewing, paste_identi=True, full_screen=full_screen, longtime_wait_file_name='2.png')  # 采用全图片匹配
    if result:
        txt_change(prom_name=prom_name, menu_change=menu_change)
        sleep(2)
        system('taskkill /IM "LenovoAppstore.exe" /F')

    else:
        failure.extend(format_menu(prom_name.split()))


def install_TXvideo(choose, prom_name, menu_change, failure, full_screen):
    sleep_time = [10, 10, 10, 10, 50]  # 各图片的等待时间
    grayscale = [True, True, True, False, False]  # 各图片是否使用灰度搜索
    skewing = [[0, 0], [0, 0], [-200, 0], [0, 0], [0, 0]]  # x、y坐标偏移

    Application().start(join(getcwd(), "app_pkg", 'TXvideo',
                             'TXvideo.exe'))  # 打开指定的安装程序

    png_file_name = "_shot" if sys_version() in ["10", "11"] else "_shot_win7"
    result = install_from_png(app_name=prom_name, edit_index=2, png_file_name=png_file_name,
                              confidence=0.8, install_path=choose, sleep_time_list=sleep_time,
                              grayscale_list=grayscale, skewing_list=skewing, paste_identi=True, full_screen=full_screen, longtime_wait_file_name='2.png')  
    if result:
        txt_change(prom_name=prom_name, menu_change=menu_change)
        sleep(2)
        if kill_program(name='QQLive.exe',count=240):
            sleep(2)
            system('taskkill /IM QQLive.exe /F')
    else:
        failure.extend(format_menu(prom_name.split()))


def install_IQIYI(choose, prom_name, menu_change, failure):
    main_window = ["爱奇艺 安装向导", "win32"]
    step = {0: ["阅读并同意", 'click', 30],
            1: ["", 'edit', 6],
            2: ["立即安装", 'click', 6],
            3: ["完成", 'click', 90]}

    Application(backend=main_window[1]).start(
        join(getcwd(), 'app_pkg', prom_name, 'iqiyi_k56008174_107328.exe'))
    time = 5
    while time >= 0:
        try:
            program = Application(backend=main_window[1]).connect(
                title_re=main_window[0])  # 直接打开的程序对象不能直接使用需要重新链接
        except:
            sleep(1)
            time -= 1
        else:
            if install(main_window=main_window[0], window_backend=main_window[1], step=step,
                       program=program,
                       install_path=join(choose, prom_name), edit_value=1):
                # 安装成功修改menu文件
                txt_change(prom_name=prom_name, menu_change=menu_change)
            else:
                # 安装失败记录安装失败程序
                failure.extend(format_menu(prom_name.split()))
            break


def install_PSCS3(choose, prom_name, menu_change, failure):
    main_window = ["安装 - Adobe Photoshop CS3 Extended", "win32"]
    step = {0: ["下一步(&N) >", "TButton", 'click', 10],
            1: [r"C:\Program Files (x86)\Adobe\Adobe Photoshop CS3", "TEdit", 'edit', 6],
            2: ["下一步(&N) >", "TButton", 'click', 6],
            3: ["下一步(&N) >", "TButton", 'click', 6],
            4: ["安装(&I)", "TButton", 'click', 6],
            5: ["完成(&F)", "TButton", 'click', 60]}

    Application(backend=main_window[1]).start(
        join(getcwd(), 'app_pkg', prom_name, prom_name))
    time = 5
    while time >= 0:
        try:
            program = Application(backend=main_window[1]).connect(
                title='安装')  # 直接打开的程序对象不能直接使用需要重新链接
        except:
            sleep(1)
            time -= 1
        else:
            if install(main_window=main_window[0], window_backend=main_window[1], step=step,
                       program=program,
                       install_path=join(choose, prom_name), edit_value=100, special=True):
                # 安装成功修改menu文件
                txt_change(prom_name=prom_name, menu_change=menu_change)
            else:
                # 安装失败记录安装失败程序
                failure.extend(format_menu(prom_name.split()))
            break


def install_PSCC2019(prom_name, menu_change):
    ps_path = join(getcwd(), "app_pkg", prom_name, 'Set-up')
    # startfile(ps_path)
    copy(ps_path)
    hotkey("win", "r")
    sleep(2)
    hotkey("ctrl", "v")
    sleep(1)
    hotkey("enter")
    while True:
        try:
            Application().connect(title="Adobe Photoshop CC 2019")
        except Exception:
            sleep(3)
        else:
            break

    sleep(8)
    system('taskkill /IM "Creative Cloud.exe" /F')
    sleep(1)
    system('taskkill /IM "Photoshop.exe" /F')
    sleep(.5)
    ps_crack()
    txt_change(prom_name=prom_name, menu_change=menu_change)


def install_PRCC2020(choose, prom_name, menu_change, failure, full_screen):
    sleep_time = [10, 100]  # 各图片的等待时间
    grayscale = [False, True]  # 各图片是否使用灰度搜索
    skewing = [[0, 0], [0, 0]]  # x、y坐标偏移

    Application().start(join(getcwd(), "app_pkg", prom_name, "Set-up"))  # 打开指定的安装程序

    result = install_from_png(app_name=prom_name, edit_index=3,
                              confidence=0.8, install_path=choose, sleep_time_list=sleep_time,
                              grayscale_list=grayscale, skewing_list=skewing, paste_identi=True, full_screen=full_screen)  # 采用全图片匹配

    if result:
        txt_change(prom_name=prom_name, menu_change=menu_change)
    else:
        failure.extend(format_menu(prom_name.split()))


def intall_163music(choose, prom_name, menu_change, failure, full_screen):
    sleep_time = [25, 10, 10, 10, 10, 70]  # 各图片的等待时间
    grayscale = [True, True, False, False, False, False]  # 各图片是否使用灰度搜索
    skewing = [[0, 0], [-230, 0], [0, 0],
               [0, 0], [0, 0], [0, 0]]  # x、y坐标偏移

    Application().start(join(getcwd(), "app_pkg", prom_name, prom_name))  # 打开指定的安装程序

    result = install_from_png(app_name=prom_name, edit_index=1,
                              confidence=0.8, install_path=choose, sleep_time_list=sleep_time,
                              grayscale_list=grayscale, skewing_list=skewing, paste_identi=True, full_screen=full_screen, longtime_wait_file_name='4.png')  # 采用全图片匹配
    if result:
        sleep(2)
        txt_change(prom_name=prom_name, menu_change=menu_change)
        system('taskkill /IM cloudmusic.exe /F')
    else:
        failure.extend(format_menu(prom_name.split()))


def install_QQmusic(choose, prom_name, menu_change, failure, full_screen):
    sleep_time = [10, 10, 10, 10, 60]  # 各图片的等待时间
    grayscale = [True, True, True, True, True]  # 各图片是否使用灰度搜索
    skewing = [[0, 0], [0, 0], [-230, 0],
               [0, 0], [0, 0], [0, 0]]  # x、y坐标偏移

    Application().start(join(getcwd(), "app_pkg", prom_name,
                             'QQMusic_Setup_2102.exe'))  # 打开指定的安装程序

    result = install_from_png(app_name=prom_name, edit_index=2,
                              confidence=0.8, install_path=choose, sleep_time_list=sleep_time,
                              grayscale_list=grayscale, skewing_list=skewing, paste_identi=True, full_screen=full_screen, longtime_wait_file_name='3.png')  # 采用全图片匹配
    if result:
        txt_change(prom_name=prom_name, menu_change=menu_change)
        sleep(2)
        system('taskkill /IM QQmusic.exe /F')
    else:
        failure.extend(format_menu(prom_name.split()))


def install_Kugou(choose, prom_name, menu_change, failure, full_screen):
    sleep_time = [10, 10, 10, 10, 10, 60]  # 各图片的等待时间
    grayscale = [True, True, False, False,
                 False, False]  # 各图片是否使用灰度搜索
    skewing = [[0, 0], [-250, 0], [0, 0], [0, 0],
               [0, 0], [0, 0],]  # x、y坐标偏移

    Application().start(join(getcwd(), "app_pkg", prom_name,
                             'kugou.exe'))  # 打开指定的安装程序

    result = install_from_png(app_name=prom_name, edit_index=1,
                              confidence=0.8, install_path=choose, sleep_time_list=sleep_time,
                              grayscale_list=grayscale, skewing_list=skewing, paste_identi=True, full_screen=full_screen, longtime_wait_file_name='5.png')  # 采用全图片匹配
    if result:
        txt_change(prom_name=prom_name, menu_change=menu_change)
        sleep(2)
        system('taskkill /IM Kugou.exe /F')
    else:
        failure.extend(format_menu(prom_name.split()))


def install_Xunlei(choose, prom_name, menu_change, failure, full_screen):
    sleep_time = [10, 50]  # 各图片的等待时间
    grayscale = [True, True]  # 各图片是否使用灰度搜索
    skewing = [[-50, 0], [0, 0]]  # x、y坐标偏移

    Application().start(join(getcwd(), "app_pkg", prom_name, prom_name))  # 打开指定的安装程序
    png_file_name = "_shot" if sys_version() in ["10", "11"] else "_shot_win7"
    result = install_from_png(app_name=prom_name, edit_index=0, png_file_name=png_file_name,
                              confidence=0.8, install_path=choose, sleep_time_list=sleep_time,
                              grayscale_list=grayscale, skewing_list=skewing, paste_identi=True, full_screen=full_screen)  # 采用全图片匹配
    if result:
        txt_change(prom_name=prom_name, menu_change=menu_change)
        if kill_program(name='Thunder.exe'):
            system('taskkill /IM Thunder.exe /F')
    else:
        failure.extend(format_menu(prom_name.split()))


def install_SogouPY(choose, prom_name, menu_change, failure, full_screen):
    sleep_time = [10, 10, 10, 10]  # 各图片的等待时间
    grayscale = [True, True, True, True]  # 各图片是否使用灰度搜索
    skewing = [[0, 0], [0, 0], [-80, 0], [
        0, 0]]  # x、y坐标偏移

    Application().start(join(getcwd(), "app_pkg", prom_name, prom_name))  # 打开指定的安装程序
    png_file_name = "_shot" if sys_version() in ["10", "11"] else "_shot_win7"
    result = install_from_png(app_name=prom_name, edit_index=2, png_file_name=png_file_name,
                              confidence=0.8, install_path=choose, sleep_time_list=sleep_time,
                              grayscale_list=grayscale, skewing_list=skewing, paste_identi=True, full_screen=full_screen, longtime_wait_file_name='4.png')  # 采用全图片匹配
    if result:
        txt_change(prom_name=prom_name, menu_change=menu_change)
    else:
        failure.extend(format_menu(prom_name.split()))


def install_3DMAX(choose, prom_name, menu_change, failure):
    step = {0: ["ListBox3", 'click', 30],       # 在此计算机上安装
            1: ["我接受Button", 'click', 6],
            2: ["下一步Button", 'click', 6],
            3: ["安装路径:Edit", join(choose, prom_name), 'edit', 6],
            4: ["安装Button", 'click', 6]}

    sleep_time = [5, 1, 1, 3, 1, 1, 1, 3, 2, 1]

    setup_path = join(getcwd(), "app_pkg", '3DMAX2020', "Setup.exe")
    # startfile(setup_path)
    copy(setup_path)
    hotkey("win", "r")
    sleep(2)
    hotkey("ctrl", "v")
    sleep(1)
    hotkey("enter")

    time = 20
    while time >= 0:
        try:
            program = Application().connect(title="Autodesk 3ds Max 2020")
        except:
            sleep(1)
            time -= 1
        else:
            break
    if simple_install(window_backend='win32', step=step, program=program, sleep_time=sleep_time):
        while True:
            try:
                temp = Application().connect(title_re='文件正在使用')
                if temp.top_window().window(title='忽略(&I)').exists():
                    temp.top_window()['忽略(&I)'].click_input()
            except:
                pass

            if program.top_window().child_window(title="立即启动").exists():
                program.top_window().child_window(title="立即启动").wait("ready", timeout=10)
                program.top_window()['立即启动'].click_input()
                txt_change(prom_name=prom_name, menu_change=menu_change)
                break
            else:
                sleep(3)
        cra_3dmax()
        sleep(3)
        system('taskkill /IM 3dsmax.exe /F')
        sleep(1)
        system('taskkill /IM LMU.exe /F')
    else:
        failure.extend(format_menu(prom_name.split()))
    


def install_CAD2014(choose, prom_name, menu_change, failure):
    step = {0: ["ListBox3", 'click', 30],
            1: ["我接受Button", 'click', 6],
            2: ["下一步Button", 'click', 6],
            3: ["序列号:Edit", '666', 'edit', 6],
            4: ["Edit2", '69696969', 'edit', 6],
            5: ["产品密钥:Edit5", '001F1', 'edit', 6],
            6: ["下一步Button", 'click', 6],
            7: ["安装路径:Edit", join(choose, prom_name), 'edit', 6],
            8: ["安装Button", 'click', 6]}

    sleep_time = [3, 1, 1, 0.5, 0.5, 0.5, 1, 1, 1]

    setup_path = join(getcwd(), "app_pkg", prom_name, "Setup.exe")
    # startfile(setup_path)
    copy(setup_path)
    hotkey("win", "r")
    sleep(2)
    hotkey("ctrl", "v")
    sleep(1)
    hotkey("enter")

    time = 20
    while time >= 0:
        try:
            program = Application().connect(title="Autodesk® AutoCAD® 2014")
        except:
            sleep(1)
            time -= 1
        else:
            break
    if simple_install(window_backend='win32', step=step, program=program, sleep_time=sleep_time):
        while True:
            try:
                temp = Application().connect(title_re='文件正在使用')
                if temp.top_window().window(title='忽略(&I)').exists():
                    temp.top_window()['忽略(&I)'].click_input()
            except:
                pass

            if program.top_window().child_window(title="完成").exists():
                program.top_window().child_window(title="完成").wait("ready", timeout=10)
                program.top_window()['完成'].click_input()
                txt_change(prom_name=prom_name, menu_change=menu_change)
                break
            else:
                sleep(3)
        cra_cad2014(choose, prom_name)
    else:
        failure.extend(format_menu(prom_name.split()))


def install_CAD2007(choose, prom_name, menu_change, failure):
    program = Application().start(join(getcwd(), "app_pkg", prom_name, 'setup'))
    if program.top_window()['确定Button'].wait("ready", timeout=10) and program.top_window()[
            '确定Button'].exists():
        sleep(1)
        program.top_window()['确定Button'].click_input()
    time = 10
    while time >= 0:
        try:
            program = Application().connect(title="AutoCAD 2007 安装")
        except:
            sleep(1)
            time -= 1
        else:
            break
    step = {0: ["Button2", 'click', 10],
            1: ["RadioButton2", 'click', 6],
            2: ["Button0", 'click', 6],
            3: ["Edit1", '000', 'edit', 6],
            4: ["Edit2", '00000000', 'edit', 6],
            5: ["Button1", 'click', 6],
            6: ["Edit1", "admin", 'edit', 6],
            7: ["Edit2", "admin", 'edit', 6],
            8: ["Edit3", "admin", 'edit', 6],
            9: ["Edit4", "admin", 'edit', 6],
            10: ["Edit5", "admin", 'edit', 6],
            11: ["Button1", "click", 6],
            12: ["Button1", "click", 6],
            13: ["Button1", "click", 6],
            14: ["Edit", join(choose, prom_name), 'edit', 6],
            15: ["Button1", "click", 6],
            16: ["Button1", "click", 6],
            17: ["Button1", "click", 6]}
    sleep_time = [1, 0, 1, 0, 0, 1, 1,
                  0, 0, 0, 0, 1, 3, 3, 0, 3, 3, 3]
    if simple_install(window_backend="win32", step=step, program=program, sleep_time=sleep_time):
        sleep(5)
        try:
            Application().connect(title="AutoCAD 2007 安装程序")
        except:
            failure.extend(format_menu(prom_name.split()))
        sleep(2)
        time = 300
        while time >= 0:
            try:
                program = Application().connect(title="AutoCAD 2007 安装程序")
                if program.top_window()['完成(&F)'].exists():
                    break
            except:
                sleep(1)
                time -= 1
        step = {0: ["CheckBox", 'click', 8],
                1: ["Button1", 'click', 6]}
        simple_install(window_backend="win32",
                       step=step, program=program)
        txt_change(prom_name=prom_name, menu_change=menu_change)
        cad2007_cra(choose)
    else:
        failure.extend(format_menu(prom_name.split()))


def install_T20(choose, prom_name, menu_change, failure):
    program = Application().start(join(getcwd(), "app_pkg", prom_name, 'setup'))
    time = 20
    while time >= 0:
        if program.top_window()["我接受许可证协议中的条款((&A)RadioButton"].exists():
            break
        sleep(1)
        time -= 1

    step = {0: ["我接受许可证协议中的条款((&A)RadioButton", 'click', 10],
            1: ["下一步(&N) >Button", 'click', 6],
            2: ["浏览(&R)...Button", 'click', 6],
            3: ["路径(&P)：Edit", join(choose, prom_name), 'edit', 6],
            4: ["确定Button", 'click', 6],
            5: ["下一步(&N) >Button", 'click', 6],
            6: ["下一步(&N) >Button", 'click', 6]}
    sleep_time = [0, 2, 1, 0, 0.5, 0.5, 0]
    if simple_install(window_backend="win32", step=step, program=program, sleep_time=sleep_time):
        time = 60
        while time >= 0:
            try:
                if program.top_window()['InstallShield Wizard 完成'].exists():
                    break
            except:
                sleep(1)
                time -= 1
        step = {0: ["完成Button", 'click', 10]}
        if simple_install(window_backend="win32", step=step, program=program):
            t20_cra()
            txt_change(prom_name=prom_name, menu_change=menu_change)
    else:
        failure.extend(format_menu(prom_name.split()))
        
def install_Steam(choose, prom_name, menu_change, failure):
    program = Application().start(join(getcwd(), "app_pkg", prom_name, 'SteamSetup.exe'))
    time = 20
    while time >= 0:
        if program.top_window()["下一步(&N) >"].exists():
            break
        sleep(1)
        time -= 1

    step = {0: ["下一步(&N) >", 'click', 10],
            1: ["下一步(&N) >", 'click', 6],
            2: ["目标文件夹Edit", join(choose, prom_name), 'edit', 6],
            3: ["安装(&I)Button", 'click', 6],
            }
    sleep_time = [0, 2, 1, 10]
    if simple_install(window_backend="win32", step=step, program=program, sleep_time=sleep_time):
        time = 60
        while time >= 0:
            try:
                if program.top_window()['运行 Steam(&R)CheckBox'].exists():
                    break
            except:
                sleep(1)
                time -= 1
        step = {0: ["运行 Steam(&R)CheckBox", 'click', 10],
                1: ["完成(&F)Button", 'click', 10]}
        if simple_install(window_backend="win32", step=step, program=program):
            txt_change(prom_name=prom_name, menu_change=menu_change)
    else:
        failure.extend(format_menu(prom_name.split()))
