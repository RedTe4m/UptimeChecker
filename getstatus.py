print("| | | |_ __ | |_(_)_ __ ___   ___ / ___| |__   ___  ___| | _____ _ __ ")
print("| | | | '_ \| __| | '_ ` _ \ / _ \ |   | '_ \ / _ \/ __| |/ / _ \ '__|")
print("| |_| | |_) | |_| | | | | | |  __/ |___| | | |  __/ (__|   <  __/ |   ")
print("\____/| .__/ \__|_|_| |_| |_|\___|\____|_| |_|\___|\___|_|\_\___|_|   ")
print("      |_|                                                            ")

### setup module
import subprocess
import requests
encoding = 'utf-8'
lnks = input("Type the name of the file with the URLs (with complete path if not in same folder as script). ")

headers = {
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9,tr-TR;q=0.8,tr;q=0.7',
          }

### URL list import module
fp = open(lnks, 'r')
num_lines = sum(1 for line in open(lnks))
print("Okay. Testing", lnks, "which has", num_lines, "total entries.")
print("................................................................................")

### Run thru list
line = fp.readline()
while line:
    try:
        site = line.rstrip()
        chk = requests.get(site, headers = headers, verify=False, timeout=2.5)
        st = chk.status_code
        #print(st)
        if '200' in str(st):
            print(site, "is Up - ", st)
        elif '403' in str(st):
            print(site, "is Up - ", st)
        else: print(site, "is Down - ", st)

    except Exception as e:
        if 'SSL' in str(e):
            print(site, "is Up - requested CAC")
        elif 'timeout' in str(e):
            print(site, "is Down -  Connection Timed-out")
        else: print(site, " -- ", e)
    line = fp.readline()
fp.close
quit()
print("................................................................................")
print("Job complete.")
