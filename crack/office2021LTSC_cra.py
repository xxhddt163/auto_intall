from os import chdir  # 改变目录
from os import system  # 执行cmd命令
from os.path import join
from os import getcwd


def office2021LTSC_crack() -> None:
    """
    通过kms与ospp激活office2013
    :param path: 用户选择安装软件的目录
    :return:
    """
    old_path = getcwd()  # 储存当前路径，激活完office后返回该路径，防止之后的程序打开路径不对
    osbb_path = join(r'C:\Program Files\Microsoft Office\Office16')
    print(osbb_path)
    chdir(osbb_path)
    system('cscript ospp.vbs /sethst:liuzidan.top')
    system('cscript ospp.vbs /setprt:9005')
    system('cscript ospp.vbs /act')
    chdir(old_path)
    
    
