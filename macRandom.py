#!/usr/bin/python
import subprocess
from random import randint

def rand_mac(new_mac,interface ):
    print("[+] Changing MAC-Address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_mac():
    return subprocess.call("/sbin/ifconfig wlan0 | awk '/ether / {print $2}'", shell=True)


print("Mac-Changer Random")
print("1- Show the current MAC-Address (wlan) \n2- change your MAC-Address (wlan) Randomly ")
print("")

mc=input("Select a option a press Enter  ==> ")
if mc==('1'):
    get_mac()

if mc==('2'):
    imap = lambda *args, **kwargs: list(map(*args, **kwargs))
    rmac = ':'.join(['%02x'%x for x in imap(lambda x:randint(0,255), range(6))])
    inter = 'wlan0'
    rand_mac(rmac, inter)
