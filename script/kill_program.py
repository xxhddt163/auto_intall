'''
Author: xxh
coding: utf-8
Date: 2022-03-08 22:30:38
LastEditTime: 2022-09-22 00:55:24
FilePath: \auto_install\script\kill_program.py
'''
import psutil
from time import sleep


def kill_program(name: str, count: int = 50) -> None:
    while count:
        for proc in psutil.process_iter(['name']):
            if name == proc.info['name']:
                return True
            
        sleep(2)
        count -= 1
    return False


