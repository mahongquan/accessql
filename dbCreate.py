# -*- coding: gb2312 -*-
#改编马红权2005-07-06
import win32com.client
from comerror import com_error
def CreateDatabase(fn):
    try:
        dbLangGeneral = ";LANGID=0x0409;CP=1252;COUNTRY=0"
        conn = win32com.client.Dispatch('DAO.DBEngine.36')
        conn.CreateDatabase(fn, dbLangGeneral)
    except com_error,e:
        print e[2][2]
def CompactDatabase(fn,fn2):
    conn = win32com.client.Dispatch('DAO.DBEngine.36')
    conn.CompactDatabase(fn,fn2)
if __name__=='__main__':
    fn=r"i:\t.mdb"
    fn2=r"i:\t.compact.mdb"
    CreateDatabase(fn)
    CompactDatabase(fn,fn2)