import os
import re
import time
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
lt=time.localtime()
fn= "filelines"+str(lt[0])+"-"+str(lt[1])+"-"+str(lt[2])+".txt"
fl=open(fn,"w")
filetype=["*.frm","*.bas","*.ctl","*.cls"]
nt=[]
for i in range(len(filetype)):
    nt.append(0)
for i in range(len(filetype)):
#for ft in filetype:
    files=mylistdir(".",filetype[i])
    print(nt[i])
    for f in  files:
        n1=filelines(f)
        fl.write(str(f)+"\t"+str(n1)+"\n")
        nt[i]=nt[i]+n1
    print(nt[i])
    fl.write(filetype[i]+"\t"+str(nt[i])+"\n")
print(filetype)
print(nt)
t=0
for i in nt:
    t=t+i
print(t)
fl.write("*\t"+str(t)+"\n")
fl.close()