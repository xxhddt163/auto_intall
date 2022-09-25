from os.path import join
from os import getcwd
from pywinauto import Application
from script.install_from_png import install_from_png
from pyperclip import paste, copy
from time import sleep
from pyautogui import click, tripleClick, hotkey
from script.simple_install import simple_install

def cad2019_cra():
    
    sleep_time = [30, 40, 10, 10]  # 各图片的等待时间
    grayscale = [True, False, True, True]  # 各图片是否使用灰度搜索
    skewing = [[0, 0], [0, 0], [0, 0], [0, 0]]  # x、y坐标偏移
    png_file_name = "_shot1"
    
    if install_from_png(app_name="CAD2019", confidence=0.8, sleep_time_list=sleep_time, grayscale_list=grayscale,
                        skewing_list=skewing, png_file_name=png_file_name):
            sleep(3)
            copy('666')
            hotkey('ctrl','v')
            sleep(1)
            copy('69696969')
            hotkey('ctrl','v')
            sleep(1)
            copy('001K1')
            hotkey('tab')
            hotkey('ctrl','v')
            sleep(1)
            hotkey('tab')
            sleep(1)
            hotkey('tab')
            sleep(1)
            hotkey('tab')
            sleep(1)
            hotkey('enter')
            
            sleep_time = [10]  # 各图片的等待时间
            grayscale = [True]  # 各图片是否使用灰度搜索
            skewing = [[0, 0]]  # x、y坐标偏移
            png_file_name = "_shot2"
            
            sleep(5)
            
            if install_from_png(app_name="CAD2019", confidence=0.8, sleep_time_list=sleep_time, grayscale_list=grayscale,
                        skewing_list=skewing, png_file_name=png_file_name):
                
                sleep_time = [10, 15]  # 各图片的等待时间
                grayscale = [True, True]  # 各图片是否使用灰度搜索
                skewing = [[200, 0], [0, 0]]  # x、y坐标偏移
                png_file_name = "_shot3"
                coordinate_list = install_from_png(app_name="CAD2019", confidence=0.8, sleep_time_list=sleep_time,
                                           grayscale_list=grayscale, skewing_list=skewing, png_file_name=png_file_name,
                                           coordinate=True)
                
                if len(coordinate_list) == 2:
                    button1 = coordinate_list[0]  # 申请号坐标
                    button2 = coordinate_list[1]  # 我具有序列号坐标
                    tripleClick(button1[0], button1[1])
                    hotkey('ctrl', 'c')  # 复制申请号
                    
                    key_soft = Application().start(join(getcwd(), 'app_pkg', 'CAD2019', 'crack', 'crack.exe'))  # 打开注册机
                    
                    step = {0: ["Request :Edit", paste(), 'edit', 10],  # 将申请号粘贴
                    1: ["CButton", 'click', 6],  # 按下注册机patch按钮
                    2: ["确定Button", 'click', 6],  # 按下弹出窗口的确定按钮
                    3: ["GButton", 'click', 6]}  # 按下注册机Gen按钮获得激活码
                    if simple_install(window_backend='win32', step=step, program=key_soft):
                        while True:  # 判断生成的激活码是否正确
                            dict_temp = key_soft.top_window()._ctrl_identifiers()
                            for each in dict_temp.keys():  # 通过按钮便签值获取激活码
                                if 'Activation :Edit' in dict_temp[each]:
                                    temp = str(each)
                            key = temp.split("'")[1]
                            if len(key) == 57:
                                copy(key)
                                break
                            else:
                                key_soft.top_window()['GButton'].click_input()
                        key_soft.top_window()['QQButton'].click_input()  # 按下注册机Quit按钮
                        click(button2[0], button2[1])  # 按下我具有激活码坐标
                        sleep(1)
                        hotkey('ctrl', 'v')  # 粘贴激活码
                        sleep(1)

                        for _ in range(5):
                            hotkey('tab')
                            sleep(.5)
                        hotkey('enter')
                        sleep(3)
                        
                        
                
                        
                        
                        