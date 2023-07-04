'''
Author: xxh
coding: utf-8
Date: 2022-10-19 01:10:37
LastEditTime: 2022-10-19 02:52:50
FilePath: \auto_install\script\change_DPI.py
'''
import platform
import winreg

def system_info() -> str:
    """返回操作系统的版本。
    

    Returns:
        str: win7: return "7" ,win10 or win11: return "10"
    """
    return platform.uname().release

def regedit_win7():
    """win7系统直接修改一个注册表文件即可"""
    reg = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                          r"Control Panel\Desktop",0,winreg.KEY_ALL_ACCESS)      # 打开注册表的指定路径并获得所有权限
    winreg.SetValueEx(reg, "LogPixels",0, winreg.REG_DWORD, 96)

def regedit_win10():
    """win10需要创建LogPixels键然后还需要再修改Win8DpiScaling值"""
    reg = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                          r"Control Panel\Desktop",0,winreg.KEY_ALL_ACCESS)      
    winreg.SetValueEx(reg, "LogPixels",0, winreg.REG_DWORD, 96)
    
    reg = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                          r"Control Panel\Desktop",0,winreg.KEY_ALL_ACCESS)      
    winreg.SetValueEx(reg, "Win8DpiScaling",0, winreg.REG_DWORD, 1)
    

def restore_DPI():
    """修改Win8DpiScaling值为1即可关闭自定义缩放"""
    reg = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                          r"Control Panel\Desktop",0,winreg.KEY_ALL_ACCESS)      
    winreg.SetValueEx(reg, "Win8DpiScaling",0, winreg.REG_DWORD, 0)
