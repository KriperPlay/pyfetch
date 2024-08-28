# pyfetch

![серега пират гид и лера](https://github.com/user-attachments/assets/8297967b-1e3e-463e-9d31-d9d0ab1b69ed)

# Warning
* pyfetch work only on Linux(Android/Termux not supported!)
* pyfetch support these package managers:
* * dpkg
  * rpm
  * pacman
  * zypper
  * flatpak

# About 
pyfetch - simple fetch programm writen on python, config writen on json

![изображение](https://github.com/user-attachments/assets/b3e9bcdd-bb7a-4566-b247-bb574db0e8fa)

# Need to install for build
* python 3.11+ and pip
* distro and shutil python lib
* pyinstaller
* wmctrl software

# Need to install for using
* wmctrl software

# How to install(not build)
```shell
git clone https://github.com/KriperPlay/pyfetch/
cd pyfetch/release
chmod +x install.sh
./install.sh
```
# How to build
* for start read 'Need to install for build'
```
git clone https://github.com/KriperPlay/pyfetch/
cd pyfetch/src
pyinstaller main.py --onefile
```
* the finished file will be located in the 'dist' directory

# Where located logo file and config?
* they located at '/home/$USER/.config/pyfetch'

# How to paint your logo
* emojis are used to paint the logo(emoji must be the last character in the line):
* * 🔴 - red
  * 🟢 - green
  * 🔵 - blue
  * 🟡 - yellow
  * ⚪ - white
  * ⚫ - black
  * 🟣 - violet

# Config
```json
{
    "Logo": true,
    "OS": true,
    "Host": true,
    "Kernel": true,
    "Uptime": true,
    "Packages": true,
    "Shell": true,
    "Resolution": true,
    "DE": true,
    "WM": true,
    "Terminal": true,
    "CPU": true,
    "GPU": true,
    "Disk": true,
    "Swap": true,
    "RAM": true,
    "path_logo": "logo.txt",
    "color": "VIOLET"
}
```
values ​​for variable 'color':
* "RED"
* "GREEN"
* "BLUE"
* "WHITE"
* "BLACK"
* "YELLOW"
* "VIOLET"

next i think everything is clear here
