import subprocess
import fileinput
import os
import sys

def initInstall():
    os.chdir('/home/pi')
    print()
    print("Updating")
    print()
    os.system('sudo apt-get update')
    os.system('sudo apt-get upgrade')

def installWireguard():
    os.chdir('/home/pi')
    print()
    print("Installing WireGuard")
    print()

    print()
    print(" - installing required packages")
    os.system('sudo apt-get install bc libncurses5-dev libmnl-dev \
        build-essential git -y')

    # rpi-source
    print()
    print(" - installing rpi-source")
    os.system('sudo wget https://raw.githubusercontent.com/notro/rpi-source/master/rpi-source \
        -O /usr/bin/rpi-source && sudo chmod +x /usr/bin/rpi-source \
        && /usr/bin/rpi-source -q --tag-update')

    print()
    print(" - running rpi-source")
    os.system('rpi-source --skip-gcc')

    # WireGuard
    print()
    print(" - installing WireGuard")
    os.chdir('/home/pi')
    os.system('git clone https://git.zx2c4.com/WireGuard')
    os.chdir('/home/pi/WireGuard/src/')
    os.system('make && sudo make install')

    print()
    print(" - generating keys")
    os.system('wg genkey | tee server-private.key | wg pubkey > server-public.key')

def installGstreamer():
    os.chdir('/home/pi')
    print()
    print("Installing GStreamer")
    os.system('sudo apt-get install gstreamer1.0-tools -y')

def installAPI():
    os.chdir('/home/pi')
    print()
    print("Installing API")
    os.system('git clone https://git.inixi.se/alexis/RaspiWiFi.git')
    os.system('sudo apt-get install python3 bundler libsqlite3-dev isc-dhcp-server hostapd -y')
    os.chdir('/home/pi/RaspiWiFi/Configuration App')
    os.system('bundle install')


def finishInstall():
    print()
    print()
    print("Installation complete")
    print()

def install():
    initInstall()
    installWireguard()
    installGstreamer()
    installAPI()
    finishInstall()

def config():
    # TODO

if len(sys.argv) >= 2:
    if sys.argv[1] == "install":
        install()
    elif sys.argv[1] == "config":
        config()
else:
    print()
    print("Nothing to do")
    print()
