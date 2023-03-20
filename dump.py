# -- Copyright 2023 by brutalID -- #
# -- MODULE -- #
import requests,bs4,json,os,sys,random,datetime,time,re
from concurrent.futures import ThreadPoolExecutor as thred
from rich.console import Console as sol
from rich.markdown import Markdown as mark
from bs4 import BeautifulSoup as soup
from rich.panel import Panel as nel
from rich import print as cetak
ses=requests.Session()

# -- WARNA -- #
x = '\33[m' 		# PUTIH
m = '\x1b[1;91m' 	# MERAH
s = '\33[100m'		# ABU BG
n = '\33[34m'    	# MATI
k = '\033[93m' 		# KUNING
c = '\33[46m' 		# CYAN BG
h = '\33[92m' 		# HIJAU 
hb = '\33[42m'		# HIJAU BG
mb = '\33[41m'		# MERAH BG

# -- REUNI -- #
id,bahan = [],[]
loop,ok,cp = 0,0,0

# -- BANNER -- #
def banner():
	if "linux" in sys.platform.lower():
		try:os.system('clear')
		except:pass
	elif "win" in sys.platform.lower():
	    try:os.system('cls')
	    except:pass
	else:
	    try:os.sytem('clear')
	    except:pass
	teks = '# FACEBOOK CRACKED TOOLS'
	title = mark(teks, style='red')
	sol().print(title,style='white')
	au = "[white]╔═╗╔╗╔╦╗╦   ╦╔╦╗\n╚═╗╠╩╗║ ║   ║ ║║\n╚═╝╚═╝╩ ╩═╝o╩═╩╝[white][green]\n Copyright 2023 By Brutal.ID[white]"
	text = nel(au,style="cyan")
	cetak(nel(text,style='blue'))

# -- LOGIN -- #
def login():
	try:
		banner()
		cook = input(f'{x}  [{k} ! {x}] Enter Cookies :{h} ')
		try:
			cookie = {'cookie':cook}
			url = 'https://www.facebook.com/adsmanager/manage/campaigns'
			req = ses.get(url,cookies=cookie)
			set = re.search('act=(.*?)&nav_source',str(req.content)).group(1)
			nek = '%s?act=%s&nav_source=no_referrer'%(url,set)
			roq = ses.get(nek,cookies=cookie)
			tok = re.search('accessToken="(.*?)"',str(roq.content)).group(1)
			open(".token.txt", "w").write(tok)
			open(".cookie.txt", "w").write(cook)
			print(f'{x}  [{h} • {x}] LOGIN SUCCESS{x} ');time.sleep(1)
			check()
		except Exception as e:
			print(f'{x}  [{m} • {x}] Cookies Invalid')
	except Exception as e:
		print(f'{x}  [{m} ! {x}]{m} LOGIN FAILED{x} ')
		exit()

# -- CHECK -- #
def check():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cookie.txt','r').read()
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+token, cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login()
		except requests.exceptions.ConnectionError:
			print(f'{x} [{m} ! {x}]{m} CONNECTION ERROR{x} ')
			exit()
	except IOError:
		login()

# -- MENU -- #
def menu(my_name,my_id):
	banner()
	ip = requests.get("https://api.ipify.org").text
	print(f'{x} ╔ [{h} • {x}] Your Name  : {h}'+str(my_name))
	print(f'{x} ╠ [{h} • {x}] Your Id    : {h}'+str(my_id))
	print(f'{x} ╠ [{h} • {x}] Your Ip    : {h}{ip}')
	print(f'{x} ╠ [{h} • {x}] Github     : {x}https://github.com/printalid')
	print(f'{x} ╠ [{h} • {x}] Update     : {x}Version 2.3')
	print(f'{x} ║')
	print(f'{x} ╠══ [{h} • {x}] Select Menu {x}')
	print(f'{x} ║')
	print(f'{x} ╠══ [{h} 1 {x}] Ambil ID dari publik {x}')
	print(f'{x} ╠══ [{h} 2 {x}] Ambil ID dari Publik masal {x}')
	print(f'{x} ╠══ [{h} 0 {x}] Keluar {x}')
	print(f'{x} ║')
	pill = input(f'{x} ╚══ [ {h}•{x} ] Pilih :{n} ')
	if pill in ['1','01']:
		banner()
		akun = input(f'{x} [ {h}•{x} ] Masukan ID publik, Ketik{k} me{x} untuk dump teman sendiri \n{x} [ {h}•{x} ] ID :{n} ')
		nama = input(f'{x} [ {h}•{x} ] Nama filenya [{k} contoh.txt {x}] :{n} ')
		took = open('.token.txt','r').read()
		publik(f'https://graph.facebook.com/{akun}?fields=friends&access_token={took}',nama)
		print(f'{x}\n [{h} • {x}] Berhasil mengumpulkan{h} {len(id)} {x}')
		print(f'{x} [{h} • {x}] File di simpan dengan nama{h} {nama}{x}')
	elif pill in ['2','02']:
		banner()
		jum = int(input(f'{x} [ {h}•{x} ] Masukan Jumlah ID target :{n} '))
		nama = input(f'{x} [ {h}•{x} ] Nama filenya [{k} contoh.txt {x}] :{n} ')
		i = 1
		for ok in range(jum):
			akun = input(f'{x} [ {h}•{x} ] Masukan ID ke{k} {i} {x}:{n} ')
			bahan.append(akun)
			i = i+1
		for akun in bahan:
			took = open('.token.txt','r').read()
			publik(f'https://graph.facebook.com/{akun}?fields=friends&access_token={took}',nama)
		print(f'{x}\n [{h} • {x}] Berhasil mengumpulkan{h} {len(id)} {x}')
		print(f'{x} [{h} • {x}] File di simpan dengan nama{h} {nama}{x}')
	elif pill in ['0','00']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print(f'{x}\n [{h} • {x}] Berhasil keluar dan menghapus info login ')
		exit()
	else:
		print(f'{x}  [{m} ! {x}] input correctly ')
		exit()

# -- publik1 -- #
def publik1(url,nama):
	try:
		cook = open('.cookie.txt','r').read()
		bas = ses.get(url,cookies={'cookies':cook}).json()
		for pi in bas['data']:
			try:
				if 'username' in pi:
					id.append(pi['username']+'|'+pi['name'])
					getuser = (pi['username']+'|'+pi['name']+'\n')
					open(nama,'a').write(getuser)
					print(f'\r{x} [ {h}•{x} ] sedang dump{k} %s{x} id'%(len(id)),end=" ")
				elif 'id' in pi:
					id.append(pi['id']+'|'+pi['name'])
					getid = (pi['id']+'|'+pi['name']+'\n')
					open(nama,'a').write(getid)
					print(f'\r{x} [ {h}•{x} ] sedang dump{k} %s{x} id'%(len(id)),end=" ")
				else:
					pass
			except Exception as e:
				print(e)
		try:
			if 'https' in bas['paging']['next']:
				publik1(bas['paging']['next'],nama)
		except:
			pass
	except (KeyError,IOError):
		print(f'{x}\n [{m} ! {x}] Akun anda di larang memakai fitur ini ')


# -- PUBLIK -- #
def publik(url,nama):
	try:
		cook = open('.cookie.txt','r').read()
		bas = ses.get(url,cookies={'cookies':cook}).json()
		for pi in bas['friends']['data']:
			try:
				if 'username' in pi:
					id.append(pi['username']+'|'+pi['name'])
					getuser = (pi['username']+'|'+pi['name']+'\n')
					open(nama,'a').write(getuser)
					print(f'\r{x} [ {h}•{x} ] sedang dump %s id'%(len(id)),end=" ")
				elif 'id' in pi:
					id.append(pi['id']+'|'+pi['name'])
					getid = (pi['id']+'|'+pi['name']+'\n')
					open(nama,'a').write(getid)
					print(f'\r{x} [ {h}•{x} ] sedang dump{k} %s{x} id'%(len(id)),end=" ")
				else:
					pass
			except Exception as e:
				print(e)
		try:
			if 'https' in bas['friends']['paging']['next']:
				publik1(bas['friends']['paging']['next'].replace('limit=25','limit=5000'),nama)
		except:pass
	except (KeyError,IOError):
		exit(f"{x} [{m} ! {x}] akun tidak publik")



# -- SETUP -- #
check()
