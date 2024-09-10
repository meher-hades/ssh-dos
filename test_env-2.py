#should we make a check wether ssh svc on victim working or not ???
#for prong1 no env check
#for prong two the pwd file and username file should be of same length discrepence can not lead to an issue ...although a warning to be issued if user and pwd file has , as time lapse with uneven O cmplexity to be there
#for prong 3 give out warning for logingrace timer to be 120 change it to 120 sec or something check for os import file or keep the user list passing here a bit small in length
#for prong 4 just check max connections and automate creation of users with 1 password and make sure its working now push it in prong 4, or you can just create 1usr-1pwd and repeat that user in a file and pass that but authenticating with difference user is much better for search time of matching
import sys
try:
	uname=sys.argv[1]
	pname=sys.argv[2]
except:
	print("put in the files user and paswd in this order for env checks..")
	sys.exit()
#print(uname,pname,M.H)

def disclaimer():
    print("CONFIDENTIAL:CISCO")
    print("THIS IS FOR ONLY SSH PASSWORD BASED SERVICE")
    try:
        import pwn
    except:
        print("INSTALL PWNTOOLS MODULE VIA PIP")

def prong1_envcheck():
    print("ENV CHECK FOR PRONG1: OK")

def prong2_envcheck():
    pptr=open(pname,"r")
    uptr=open(uname,"r")
    countu=0
    countp=0
    for usr in uptr.readlines():
        countu=countu+1

    for pwd in pptr.readlines():
        countp=countp+1
    
    if countp!=countu:
        print("WARNING: DISCREPENCE IN PWD AND USER FILE")
    else:
        #print(countp,countu)
        print("ENV CHECK FOR PRONG2: OK")

def prong34_envcheck():
    try:
        import os
    except:
        print("INSTALL OS MODULE VIA PIP")
    print("ENV CHECK FOR PRONG3: OK")
    print("FOLLOWING INSTRUCTION FOR PRONG4:")
    print("CHECK FOR 'LOGINGRACETINMER' & 'MAXCONNECTIONS' ON SERVER SIDE")
    print("CREATE USERS WITH SIMILAR USERNAME ON THE SSH-SERVER WITH SINGLE PASSWORD")
	

disclaimer()
prong1_envcheck()
prong2_envcheck()
prong34_envcheck()
