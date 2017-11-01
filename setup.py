import subprocess
import fileinput
import os
import sys

def init():
    os.chdir('/home/pi')
    print("Updating")
    os.system('sudo apt-get update')
    os.system('sudo apt-get upgrade')

def installWireguard():
    os.chdir('/home/pi')
    print("Installing WireGuard")

    print(" - installing required packages")
    os.system('sudo apt-get install bc libcurses5-dev libmnl-dev \
        build-essential git')

    # rpi-source
    print(" - installing rpi-source")
    os.system('sudo wget https://raw.githubusercontent.com/notro/rpi-source/master/rpi-source \
        -O /usr/bin/rpi-source && sudo chmod +x /usr/bin/rpi-source \
        && /usr/bin/rpi-source -q --tag-update')

    print(" - running rpi-source")
    os.system('rpi-source --skip-gcc')

    # WireGuard
    print(" - installing WireGuard")
    os.chdir('/home/pi')
    os.system('git clone https://git.zx2c4.com/WireGuard')
    os.chdir('/home/pi/WireGuard/src/')
    os.system('make && sudo make install')

    print(" - generating keys")
    os.system('wg genkey | tee server-private.key | wg pubkey > server-public.key')

def installGstreamer():
    os.chdir('/home/pi')
    print("Installing GStreamer")
    os.system('sudo apt-get install gstreamer1.0-tools')

def finish():
    print("Installation complete")

def install():
    init()
    installWireguard()
    installGstreamer()

install()
