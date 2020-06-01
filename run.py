import os
import csv
from ipnya import *

ip_list_ok=[]
ip_list_nok=[]
for ip in ipnya:
        response=os.system("\nping -c 1 -W 1 {}".format(ip))
        if response == 0:
                print("\n{} is up  ".format(ip))
                ip_list_ok.append(ip)
        else:
                print("\n{} is down  ".format(ip))
                ip_list_nok.append(ip)

for ip in ip_list_ok:
	with open ('data.csv','rw+') as f:
		w = csv.writer(f)
		for ipok in ip_list_ok:
			w.writerow(ipok)
		f.close
				
				
	
