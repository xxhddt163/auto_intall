import psutil
from os import system


class Change_interface():
    """自动获取上网的网卡并自动切换其状态"""

    def __init__(self):
        self.key = False
        self.interface = self.get_interfaces()

    def get_interfaces(self):
        """获取具有IP地址的网卡名"""
        all_network = psutil.net_if_addrs()

        step1 = {key: value for key, value in all_network.items(
        ) if "VMware" not in key and "Loop" not in key and "isatap" not in key}

        return {key: step1[key][1].address for key in step1 if not step1[key][1].address.startswith("169.254")}

    def check_interface(self, interface_name, check):
        """禁用或启用网卡"""
        if check:
            command = f'netsh interface set interface name="{interface_name}" admin=enabled'
        else:
            command = f'netsh interface set interface name="{interface_name}" admin=disabled'

        system(command)

    def change_interface(self):
        for name in self.interface.keys():
            self.check_interface(interface_name=name, check=self.key)
        self.key = not self.key


if __name__ == '__main__':
    c = Change_interface()
    