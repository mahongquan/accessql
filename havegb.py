# -*- coding: gbk -*-
def havegb(s):
    if len(s)<2:
        return 0
    else:
        for i in range(len(s)-1):
            #print s[i]+s[i+1]
            if isgb(s[i],s[i+1])==1:
                #print "yes"
                return 1
            else:
                #print "no"
                pass
    return 0
def isgb(ch1,ch2):
    ch1=ord(ch1)
    ch2=ord(ch2)
    if (0x81<=ch1 and ch1<=0xFE) and (0x40<=ch2<=0x7E or 0x7E<=ch2<=0xFE):  
        return 1
    else:
        return 0
if __name__=="__main__":
    print havegb("a汉")
    print havegb("ab")
