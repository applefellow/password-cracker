from subprocess import call
import platform
from rarfile import RarFile
import itertools
import os,sys
import datetime
import socket
os.system('clear')



def check_os():
    from sys import platform
    if  platform == "linux" or platform == "linux2":
        import platform
        a=list(platform.dist())
        print ("[*]"+a[0]+" os Detected..."+a[1]+" Success \u2713")
    elif platform == "darwin":
        print ("[*]OS-X os Detected...Success \u2713")
    elif platform == "win32":
        print ("[*]Windows os Detected...Success \u2713")
    else:
        print ("[!]OS Detection Faild...Unknown OS !")
print ("[!]Detecting Operating-System...")
check_os()
def is_connected():
    try:
        socket.create_connection(("www.google.com", 80))
        print ("[*]Checking Internet Connection...Success \u2713")
        return True
    except:
        print ("[!]Checking Internet Connection...Faild !")
print ("[!]Checking Internet Connection...")        
is_connected()
def python():
    try:
        from sys import platform
        if platform == "linux" or platform == "linux2":
            os.system('apt-get install python python3')
            #call(["konsole", "-e", "python /root/Desktop/python/My_project/python_install.py"])
        elif platform == "darwin":
            pass
        elif platform == "win32":
            pass
        
        print ("[*]Checking python...Success \u2713")
    except Exception as e:
        print("[!]Checking python...Faild",e)
print ("[!]Checking python...")
python()
print ("\n[\u2713]Checking Process Over\n")
input("Press Enter to continue...")

#Cracking programs start here

def rarcracker(): 
    now = datetime.datetime.now()
    print (now)
    os.system('clear')
    a=0
    for i in range(5):
        if a == 1:
            break
        pass1=itertools.product('12345',repeat=5)
        for j in pass1:
            password=''.join(j)
            try:
                with RarFile('/root/Desktop/test.rar') as file:
                    file.extract(file.namelist()[0],pwd=password)
                    print ("\n\n[+]success password found",password,now,"\n")
                    a=1
                    break
            except:
                print ("[*]Trying password",password,now,end="\r")
    input("Press Enter to continue...")
#rarcracking End Here
while True:
    os.system('clear')
    print("Select The Option\n")
    print("[1]Rar File Cracking")
    print("[2]Facebook Cracking")
    print("[3]Zip file Cracking")
    print("[4]quite\n\n")
    x=input("Enter the Option:-")
    if x == '1':
        rarcracker()
    elif x == '4':
        print("Exiting...")
        os.system('clear')
        exit()

    else:
        print ("Sorry Program Will update Soon")
