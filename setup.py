import subprocess
import fileinput
import os
import sys

def init():
    print("Updating")
    os.system('sudo apt-get update')
    os.system('sudo apt-get upgrade')

def installWireguard():
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
    print(" - installing required packages")
    os.system('')

def test():
    os.system('mkdir test')

test()
