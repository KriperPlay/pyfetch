
# █▀█ █▄█ █▀▀ █▀▀ ▀█▀ █▀▀ █░█   █▄▄ █▄█   █▀█ █▀█ █▀▀ █▀▀
# █▀▀ ░█░ █▀░ ██▄ ░█░ █▄▄ █▀█   █▄█ ░█░   ▀▀█ █▄█ █▀░ █▀░


import platform
import json
import distro
import os
import shutil


user_name = os.popen("echo $USER").read().strip()
kernel = platform.uname()[2]
full_name = f"{user_name}@{platform.uname()[1]}"
os_name = distro.name()
host = platform.node()
uptime = os.popen("uptime -p").read()[3:-1] 
res = os.popen("xrandr -q | grep '\*'").read()
shell = os.popen("echo $SHELL").read().strip()

de = os.popen("echo $XDG_CURRENT_DESKTOP").read().strip()
wm = os.popen("wmctrl -m").readlines()
if bool(wm) == False:
    wm = ""
else:
    wm = wm[0][6:-1]

config_path = f"/home/{user_name}/.config/pyfetch/config.json"

terminal = os.popen("echo $TERM_PROGRAM").read().strip()
if bool(terminal) == True:
    pass
else:
    terminal = os.popen("tty").read().strip()

total, used, free = shutil.disk_usage('/')
total_gb = total / (1024 ** 3)
used_gb = used / (1024 ** 3)
free_gb = free / (1024 ** 3)

ram = os.popen('free -t -m').readlines()
values = map(int, ram[1].split()[1:])
total_memory, used_memory, free_memory, wqe,qweewq,qeweq = values

swap = os.popen('free -t -m').readlines()
values_swap = map(int, swap[-2].split()[1:])
total_memory2, used_memory2, free_memory2 = values_swap

cpu_name = os.popen("cat /proc/cpuinfo |grep -i name").read()
gpu_name = os.popen("lspci | grep -i vga").read()


for i in range(len(cpu_name)):
    if cpu_name[i] == ':':
        break
for j in range(len(cpu_name)):
    if cpu_name[j] == "H":
        if cpu_name[j+1] == 'z':
            break
        else:
            continue
    else:
        continue

cpu_name = cpu_name[i+1:j+2]

a=0
for q in range(len(gpu_name)):
    if gpu_name[q] == ':':
        a += 1
        if a == 2:
            break

gpu_name = gpu_name[q+1:].strip()

with open(config_path, 'r') as data:
    config_data = json.load(data)

def pkgs():
    pkgs_quantity = f""
    if os.path.isdir("/var/cache/pacman"):
        pacman_pkgs = os.popen("pacman -Qq").read()
        pacman_pkgs_quan = len(pacman_pkgs.splitlines())
        pkgs_quantity += f"{pacman_pkgs_quan} (pacman) "
    if os.path.isdir("/var/lib/dpkg"):
        apt_pkgs = os.popen("dpkg-query -f '.\n' -W").read()
        apt_quan = len(apt_pkgs.splitlines())
        pkgs_quantity += f"{apt_quan} (dpkg) "
    if os.path.isdir("/var/lib/rpm"):
        rpm_pkgs = os.popen("rpm -qa").read()
        rpm_quan = len(rpm_pkgs.splitlines())
        pkgs_quantity += f"{rpm_quan} (rpm) "
    if os.path.isdir("/var/cache/zypper"):
        zypper_pkgs = os.popen("zypper se --installed-only").read()
        zyp_quan = len(zypper_pkgs.splitlines())
        pkgs_quantity += f"{zyp_quan} (zypper) "
    if os.path.isdir("/var/lib/flatpak"):
        flatpaks = os.popen("flatpak list").read()
        flatpaks_quan = len(flatpaks.splitlines())
        pkgs_quantity += f"{flatpaks_quan} (flatpak) "
    return pkgs_quantity

_tcolors = {
    "RED": "\033[31m",
    "GREEN": "\033[32m",
    "BLUE": "\033[34m",
    "YELLOW": "\033[33m",
    "BLACK": "\033[30m",
    "VIOLET": "\033[35m",
    "WHITE": "\033[37m",
    "END": "\033[0m",
    "": ""
}

local_config = {
    "Logo": True,
    "OS": os_name,
    "Host": host,
    "Kernel": kernel,
    "Uptime": uptime,
    "Packages": pkgs(),
    "Shell": shell,
    "Resolution": f"\n{res}",
    "DE": de,
    "WM": wm,
    "Terminal": terminal,
    "CPU": cpu_name,
    "GPU": gpu_name,
    "Disk": f"{used_gb:.2f} / {total_gb:.2f} GB",
    "Swap": f"{used_memory2} / {total_memory2} MB",
    "RAM": f"{used_memory} / {total_memory} MB",
    "path_logo": "",
    "color": ""
}
color = config_data ["color"]

with open(config_path, 'r') as data:
    config_data = json.load(data)
    
    
def logo(file):
    try:
        spaces = " " * 10

        logo1 = open(file, 'r')
        for line in logo1:
            if line[len(line)-2] == "🔴":
                print(f"{spaces}{_tcolors['RED']}{line[:-2]}{_tcolors['END']}\n", end='')
            elif line[len(line)-2] == "🟢":
                print(f"{spaces}{_tcolors['GREEN']}{line[:-2]}{_tcolors['END']}\n", end='')
            elif line[len(line)-2] == "🔵":
                print(f"{spaces}{_tcolors['BLUE']}{line[:-2]}{_tcolors['END']}\n", end='')
            elif line[len(line)-2] == "🟡":
                print(f"{spaces}{_tcolors['YELLOW']}{line[:-2]}{_tcolors['END']}\n", end='')
            elif line[len(line)-2] == "⚪":
                print(f"{spaces}{_tcolors['WHITE']}{line[:-2]}{_tcolors['END']}\n", end='')
            elif line[len(line)-2] == "⚫":
                print(f"{spaces}{_tcolors['BLACK']}{line[:-2]}{_tcolors['END']}\n", end='')
            elif line[len(line)-2] == "🟣":
                print(f"{spaces}{_tcolors['VIOLET']}{line[:-2]}{_tcolors['END']}\n", end='')
            else:
                print(spaces + line, end='')
        logo1.close()
    except FileNotFoundError:
        pass


def down_line(strr):
    for i in range(len(strr)):
        print("-",end='')
    print()

def main():
    if config_data["Logo"] == True:
        logo(f"/home/{user_name}/.config/pyfetch/"+config_data["path_logo"])
    config_data["Logo"] = False
    print(_tcolors[color] + full_name + _tcolors["END"])
    down_line(full_name)

    for key,value in config_data.items():
        if value == True:
            if key == "Resolution":
                if bool(res) == False:
                    pass
                else:
                    print(f"{_tcolors[color]}{key} : {_tcolors['END']}{local_config[key]}", end='')
            elif key == "WM":
                if bool(wm) == False:
                    pass
                else:
                    print(f"{_tcolors[color]}{key} : {_tcolors['END']}{local_config[key]}")
            elif key == "DE":
                if bool(de) == False:
                    pass
                else:
                    print(f"{_tcolors[color]}{key} : {_tcolors['END']}{local_config[key]}")
            elif key == "GPU":
                if bool(de) == False:
                    pass
                else:
                    print(f"{_tcolors[color]}{key} : {_tcolors['END']}{local_config[key]}")
            else:
                print(f"{_tcolors[color]}{key} : {_tcolors['END']}{local_config[key]}")
        else:
            pass

if __name__ == "__main__":
    try:
        main()
    except KeyError:
        color = "WHITE"
        main()
