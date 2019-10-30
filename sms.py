def salam(kata):
     print (kata) 

salam('\033[1;35m jones :b,hiyaaaa jones')
nama = input('\033[1;32m Siapa Namamu? : ')

print ('\033[1;32m Selamat datang', nama)

print ("\033[1;32m--------------------------------------------------")
print ("\033[1;31m[\033[1;37m1\033[1;31m] \033[1;33m Author=Tania`27")
print ("\033[1;31m[\033[1;37m1\033[1;31m] \033[1;33m WA   =08993307590")
print ("\033[1;32m--------------------------------------------------")
from requests import Session
import re, sys
s = Session()

try:
	print("\033[1;35mhy semua ,ini sms gratis dari web http://sms.payuterus.biz,masukkan nomor dengan +62xx yah,bukan 08xx ")
	no = int(input("\033[1;35mnomernya    : "))
	msg = input("\033[1;35mapa pesannya : ")
except:
	print("\n\t*\033[1;35m cek dulu beb,pesan tadi,dan coba lagi 10-15 menit jika ingin sms lagi ke nomor yang sama  *")
	sys.exit()

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36',
    'Referer': 'http://sms.payuterus.biz/alpha/'
}
bypass = s.get("http://sms.payuterus.biz/alpha/?a=keluar", headers=headers).text
key = re.findall(r'value="(\d+)"', bypass)[0]
jml = re.findall(r'<span>(.*?) = </span>', bypass)[0]
captcha = eval(jml.replace("x", "*").replace(":", "/"))

data = {
	'nohp':no,
	'pesan':msg,
	'captcha':captcha,
	'key':key
}


send = s.post("http://sms.payuterus.biz/alpha/send.php", headers=headers, data=data).text

if 'SMS nyah udah dikirim loh,tunggu aja' in send:
	print(f"\n \033[1;35m ok,Sukses dikirim \n[{no}] => {msg}")
elif 'yahh,' in send:
	print("\n\t* \033[1;35m coba lagi 10-15 menit an yahh*")
else:
	print("\n\t* \033[1;35m ok,udah terkirim *")