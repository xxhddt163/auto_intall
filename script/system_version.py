import wmi, re
import pythoncom

def sys_version():
    pythoncom.CoInitialize()    # 防止在进程中运行时提示语法错误
    try:
        w = wmi.WMI()
        for os in w.Win32_OperatingSystem():
            return re.search('[0-9]+', os.Caption).group()
    except Exception:
        return '10'
    
       