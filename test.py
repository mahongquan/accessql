import sys
f=open("log.txt","a")
p=sys.path
for p1 in p:
    f.write(p1+"\n")
f.close()

