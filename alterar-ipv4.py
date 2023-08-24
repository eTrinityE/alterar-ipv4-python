import subprocess
import sys
import ctypes
from ctypes import windll

#Alterar
nome_adaptador = "Ethernet"
ip_address = "192.168.1.190"
subnet_mask = "255.255.255.0"
gateway = "192.168.1.1"
dns = "8.8.8.8"
dns2 = "8.8.4.4"

def is_admin():
    try:
        return windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    commands = [
    f'netsh interface ipv4 set address "{nome_adaptador}" static {ip_address} {subnet_mask} {gateway}',
    f'netsh interface ipv4 set dns "{nome_adaptador}" static {dns}',
    f'netsh interface ipv4 add dns "{nome_adaptador}" {dns2} index=2'
]

    for command in commands:
        subprocess.run(command, shell=True)
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)




