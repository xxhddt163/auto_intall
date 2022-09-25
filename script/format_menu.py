def format_menu(choice_list) -> list:
    """将菜单用简化名改为详细名字"""

    menu_dir = {'Wechat': '微信', 'NF3': 'Net Framework3', '360drv': '360驱动大师', 'Chrome': '谷歌浏览器', 'TXvideo': '腾讯视频',
                'IQIYI': '爱奇艺', 'DX': 'DirectX9', '163music': '网易云音乐', 'SougouPY': '搜狗输入法', 'QQmusic': 'QQ音乐',
                'Dtalk': '钉钉', 'Kugou': '酷狗音乐', 'Lensto': '联想软件商店', 'cdr2020': 'CorelDRAW 2020', 'WPS': 'WPS',
                'AECC2019': 'After Effects CC2019', 'T20': '天正建筑T20', 'PSCS3': 'PhotoShop CS3', 'PSCC2019': 'PhotoShop CC2019',
                'OFFICE2013': 'Office 2013 Professional', 'PRCC2020': 'Premiere CC2020', 'Xunlei': '迅雷11', 'ID2021': 'Adobe indesign CC2021',
                'baidu_Netdisk': '百度网盘', 'AI2021': 'Adobe illustrator 2021', 'DC2021': 'Adobe Acrobat DC 2021'}

    menu_temp = choice_list.copy()
    for item in menu_temp:
        if item in menu_dir:
            menu_temp[menu_temp.index(item)] = menu_dir[item]
    return menu_temp
