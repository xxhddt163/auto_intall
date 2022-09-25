from os.path import join
from os import getcwd
from os import system

def ps_crack():
    
    file_name = ["Photoshop.exe"]
    for each in file_name:
        crack_path = join(getcwd(), "app_pkg", "PSCC2019", "crack", each)
        target_path = join(r"C:\Program Files\Adobe\Adobe Photoshop CC 2019", each)
        system(f'xcopy "{crack_path}" "{target_path}" /Y')
    

