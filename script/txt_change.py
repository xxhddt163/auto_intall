def txt_change(prom_name: str, menu_change: list) -> None:
    """
    :param menu_change: 安装文件列表
    :param prom_name: 需要删除的程序名字
    :return:
    """
    menu_change.remove(prom_name)
    with open("menu.ini", mode="w") as file:       # menu.txt 文件隐藏时使用r+模式打开        非隐藏可以用w模式
        file.write("、".join(menu_change))
