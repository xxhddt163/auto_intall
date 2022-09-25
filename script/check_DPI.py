import winreg

# 计算机\HKEY_CURRENT_USER\Control Panel\Desktop\WindowMetrics  AppliedDPI 60


def check_DPI():
    path = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                          r"Control Panel\Desktop\WindowMetrics")      # 打开注册表的指定路径
    return winreg.QueryValueEx(path, "AppliedDPI")[0]

