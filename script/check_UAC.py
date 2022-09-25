import winreg

# "SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System"  EnableLUA 0


def check_UAC():
    path = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                          r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System")      # 打开注册表的指定路径
    return winreg.QueryValueEx(path, "EnableLUA")[0]

