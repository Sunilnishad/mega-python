"""
Website is schedeule with time....
#1st if cond:
# Checking whether the web_list is already exist,if not the write in the hosts file
#else
# Remove the website from the host file if not in working hour..
# ...writing the whole line again and delete except web_list
"""
import time
from datetime import datetime as dt

host_temp = "hosts"
host_link = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
web_list = ["www.facebook.com ","fb.com ","facebook ","www.google.com"]

# inifite loop

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,15) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("|| Working Hour ||")
        with open(host_link,'r+') as file:
            content = file.read()

            for website in web_list:

                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        with open(host_link,'r+') as file:
            content = file.readlines()
            #After readlines goto top....file.seek(0)
            file.seek(0)
            for line in content:

                if not any (website in line for website in web_list):
                    file.write(line)
            file.truncate()
            print("Not Working")
    time.sleep(5)