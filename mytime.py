import time
import locale
import datetime
def mytime():
    t=time.localtime()
    s=locale.format("%4d-%2d-%2d %2d:%2d:%2d",(t[0],t[1],t[2],t[3],t[4],t[5]))
    return s
def todaybeginS():
    t=time.localtime()
    s=locale.format("%4d-%2d-%2d %2d:%2d:%2d",(t[0],t[1],t[2],0,0,0))
    return s
def todayendS():
    t=time.localtime()
    s=locale.format("%4d-%2d-%2d %2d:%2d:%2d",(t[0],t[1],t[2],23,59,59))
    return s
def mydateStr(d):
    s=locale.format("%04d-%02d-%02d %02d:%02d:%02d",(d.GetYear(),d.GetMonth()+1,d.GetDay(),d.GetHour(),d.GetMinute(),d.GetSecond()))
    return s
def todaybegin():
    s=datetime.datetime.now()
    return datetime.datetime(s.year,s.month,s.day,0,0,0)
def todayend():
    s=datetime.datetime.now()
    return datetime.datetime(s.year,s.month,s.day,23,59,59)
def FromMxDateTime(v):
    return datetime.datetime(v.year,v.month,v.day,v.hour,v.minute,v.second)
def beforeMonth(v):
    from mx.DateTime import RelativeDateTime,now
    etime=todayend()
    btime=now()-RelativeDateTime(months=v)
    btime=FromMxDateTime(btime)
    return(btime,etime)    
def beforeDay(v)    :
    etime=todayend()
    btime=todaybegin()-datetime.timedelta(v)
    return(btime,etime)
if __name__=="__main__":    
    print todaybegin()
    print beforeDay(3)
    print beforeMonth(3)