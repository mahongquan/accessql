import os
import re
import time
from havegb import havegb
def mylistdir(p,f):
    a=os.listdir(p)
    fs=myfind(a,f)
    return(fs)
def myfind(l,p):
    lr=[];
    #print p
    p1=p.replace(".",r"\.")
    p2=p1.replace("*",".*")
    p2=p2+"$"
    for a in l:
        #print a
        if  re.search(p2,a,re.IGNORECASE)==None :
           pass
           #print "pass"
        else:
           lr.append(a)
	   #print "append"
    return lr
def filelines(f):
    return(len(open(f).readlines()))
def findfile(f):
    print "---------"+f
    l=open(f,"r").readlines()
    i=0
    for l1 in l:
        i=i+1
        if l1[0]<>"'":
            if havegb(l1)==1:
                print i,l1
filetype=["*.frm","*.bas","*.ctl","*.cls"]
nt=range(len(filetype))
for i in range(len(filetype)):
	files=mylistdir(".",filetype[i])
	nt[i]=0
	for f in  files:
		findfile(f)
