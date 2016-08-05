from comerror import com_error
import win32com.client
from dbCreate import CreateDatabase
import codecs
#from vb2py.vbfunctions import Variant,String,Chr,IsNumeric,Len,Instr,win32com.client.Dispatch,linesplit,Mid,vbForRange,LCase,Left,Right
class MyError(Exception):
    def __init__(self, n, str):
        self.no = n
        self.value = str
#        self.unic=unicode(str,"gb2312")
    def __str__(self):
        return repr(self.value)
def saveUnicode(fn, t):
   
    f = codecs.open(fn, encoding='utf-8', mode='w+')
    f.write(t)
    f.close()
def loadUnicode(fn):
    f = codecs.open(fn, encoding='utf-8', mode='r')
    t = f.read()
    f.close()
    return t
def exportTableToFile(con, tname):
    cmds = con.export(tname)
    t = "cmds="
    for cmd1 in cmds:
        t = t + '"""' + cmd1 + '"""\r\n'
    saveUnicode("e_" + tname + ".py", t)
def IsNull(a):
    if (a == None or a.Value == None):
        return(1)
    else:
        return(0)
def Replace(a, b, c):
    return(a)

def exportAllToFile():
    dbfn = r"I:\vb\NCS_ON\src\access_2000\data.mdb"
    con = ExportAccess()
    con.setDbName(dbfn)
    exportTableToFile(con, "method")
    exportTableToFile(con, "curvexishu")
    exportTableToFile(con, "curvedata")
    exportTableToFile(con, "powerset")   
class ExportAccess:
    def create(self, pth):
        CreateDatabase(pth)
        self.setDbName(pth)
    def importAll(self, cmdfile):
        cmdstr = loadUnicode(cmdfile)
        cmds = cmdstr.split(";")
        for cmd in cmds:
            try:
                self.execCmd(cmd)
            except MyError, e:
                print e
    def test(self):
        print self.__getColumArr("sample")
    def __Ac2SQLStr(self):
        tmpstr = ''
        rs = self.__conn.OpenSchema(20)
        rs.Filter = 'TABLE_TYPE=\'TABLE\''
        NN = 0
        while not rs.EOF:
            tmpstr = tmpstr + 'SELECT  * INTO [tmp_' + rs('TABLE_NAME') + '] FROM OPENDATASOURCE(\'Microsoft.Jet.OLEDB.4.0\',\'Data Source="d:\\www\\lfgbox\\paintblue2.0f2\\pbbs\\database\\paintbase#.asa"\')...[' + rs('TABLE_NAME') + ']<br>'
            NN = NN + 1
            rs.MoveNext()
        rs.Filter = 0
        rs.Close()
        rs = None

    def __isForeignIndex(self, tablename, IndexName):
        _ret = None
        cols = self.__conn.OpenSchema(27)
        cols.Filter = 'FK_TABLE_Name=\'' + tablename + '\' and FK_NAME=\'' + IndexName + '\''
        if not cols.EOF:
            _ret = True
        else:
            _ret = False
        return _ret

    def __GetInxDesc(self, tablename, IndexName, columnName):
        _ret = None
        cat = win32com.client.Dispatch('ADOX.Catalog')
        cat.ActiveConnection = self.__connstr
        t = cat.Tables('' + tablename + '')
        i = t.Indexes('' + IndexName + '')
        c = i.Columns('' + columnName.Value + '')
        if c.SortOrder == 2:
            _ret = 'Desc'
        else:
            _ret = ''
        cat = None
        return _ret

    def linesplit(self, tablename):
        n = 0
        arr = []#vbObjectInitialize((n,), Variant)
        cols = self.__conn.openSchema(4)
        cols.Filter = 'Table_Name=\'' + tablename + '\''
        while not cols.EOF:
            arr.append(cols('column_name'))
            cols.MoveNext()
            n = n + 1
        cols.Filter = 0
        cols.Close()
        cols = None
        return arr

    def __getInxArr1(self, tablename):
        n = 0
        cols = self.__conn.openSchema(12)
        cols.Filter = 'Table_Name=\'' + tablename + '\''
        tmpCol = None
        arr = []
        while not cols.EOF:
            if cols('index_name') <> tmpCol:
                arr.append(cols('index_name'))
                n = n + 1
            tmpCol = cols('index_name')
            cols.MoveNext()
        cols.Filter = 0
        cols.Close()
        cols = None
        return arr

    def __getInxArr(self, tablename):
        _ret = None
        n = 0
        tmpCol = None
        tmps = ""
        cols = self.__conn.OpenSchema(12)
        cols.Filter = 'Table_Name=\'' + tablename + '\''
        while not cols.EOF:
            if cols.Fields('index_name') <> tmpCol:
                tmps = tmps + ',' + cols.Fields('index_name').Value
                n = n + 1
            tmpCol = cols.Fields('index_name')
            cols.MoveNext()
        cols.Filter = 0
        cols.Close()
        cols = None
        _ret = tmps[1:]#Mid(tmps, 2)
        return _ret

    def __isUnique(self, tablename, IndexName):
        _ret = None
        cols = self.__conn.OpenSchema(12)
        cols.Filter = 'Table_Name=\'' + tablename + '\' and Index_Name=\'' + IndexName + '\' and UNIQUE=True'
        if not cols.EOF:
            _ret = True
        else:
            _ret = False
        cols.Filter = 0
        cols.Close()
        cols = None
        return _ret

    def __isPrimaryKey(self, tablename, IndexName):
        _ret = None
        cols = self.__conn.OpenSchema(12)
        cols.Filter = 'Table_Name=\'' + unicode(tablename) + '\' and Index_Name=\'' + IndexName + '\' and PRIMARY_KEY=True'
        if not cols.EOF:
            _ret = True
        else:
            _ret = False
        cols.Filter = 0
        cols.Close()
        cols = None
        return _ret

    def __getPrimaryKey(self, tablename, columnName):
        _ret = None
        cols = self.__conn.OpenSchema(12)
        cols.Filter = 'Table_Name=\'' + unicode(tablename) + '\' and Column_Name=\'' + unicode(columnName.Value) + '\' and PRIMARY_KEY=True'
        if not cols.EOF:
            _ret = cols.Fields('INDEX_NAME')
            #isPrimaryKey=true
        else:
            _ret = ''
            #isPrimaryKey=false
        cols.Filter = 0
        cols.Close()
        cols = None
        return _ret

    def __existPrimaryKey(self, tablename):
        _ret = None
        cols = self.__conn.openSchema(12)
        cols.Filter = 'Table_Name=\'' + tablename + '\' and PRIMARY_KEY=True'
        if not cols.EOF:
            _ret = True
        else:
            _ret = False
        cols.Filter = 0
        cols.Close()
        cols = None
        return _ret

    def __GetIncrement(self, tablename, columnName):
        _ret = ""
        cat = win32com.client.Dispatch('ADOX.Catalog')
        cat.ActiveCONNection = self.__connstr
        _ret = cat.Tables[ tablename ].Columns[ columnName].Properties['Increment']       
        cat = None
        return _ret

    def __GetSeed(self, tablename, columnName):
        _ret = None
        cat = win32com.client.Dispatch('ADOX.Catalog')
        cat.ActiveCONNection = self.__connstr
        _ret = cat.Tables('' + tablename + '').Columns('' + columnName + '').Properties('Seed')
        cat = None
        return _ret

    def __GetAutoincrementCoulmnT(self, tablename):
        _ret = None
        self.rs.Open('select * from [' + tablename + '] where 1=0', self.__conn, 0, 1)
        for i in range(0, self.rs.Fields.Count - 1):
            if self.rs.Fields.Item(i).Properties('isAutoIncrement').Value == True:
                _ret = self.rs.Fields.Item(i).Name
                self.rs.Close()
                return _ret
        self.rs.Close()
        return _ret

    def __datatypeStr(self, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH):
        #print CHARACTER_MAXIMUM_LENGTH.Value,str(CHARACTER_MAXIMUM_LENGTH.Value)
        _ret = None
        _select0 = DATA_TYPE.Value
        if (_select0 == 130):
            if CHARACTER_MAXIMUM_LENGTH.Value == 0:
                _ret = 'memo'
            else:
                _ret = 'varchar(' + str(int(CHARACTER_MAXIMUM_LENGTH.Value)) + ')'
        elif (_select0 == 17):
            _ret = 'tinyint'
        elif (_select0 == 2):
            _ret = 'Smallint'
        elif (_select0 == 3):
            _ret = 'integer'
        elif (_select0 == 4):
            _ret = 'real'
        elif (_select0 == 5):
            _ret = 'float'
        elif (_select0 == 6):
            _ret = 'money'
        elif (_select0 == 7):
            _ret = 'datetime'
        elif (_select0 == 11):
            _ret = 'bit'
        elif (_select0 == 72):
            _ret = 'UNIQUEIDENTIFIER'
        elif (_select0 == 131):
            _ret = 'DECIMAL'
        elif (_select0 == 128):
            _ret = 'BINARY'
        return _ret

    def __defaultStr(self, DATA_TYPE, COLUMN_DEFAULT, isexec):
        _ret = None
        ##print "------------------------------"
        ##print DATA_TYPE, COLUMN_DEFAULT,type(COLUMN_DEFAULT)
        if IsNull(COLUMN_DEFAULT):
            _ret = ''
            return _ret
        if isexec == 1:
            splitchar = '""'
        elif isexec == 0:
            splitchar = '"'
        COLUMN_DEFAULT = self.__defaultStrfilter(COLUMN_DEFAULT)
        #print  COLUMN_DEFAULT,type(COLUMN_DEFAULT)
        _select1 = DATA_TYPE
        if (_select1 == 130):
            COLUMN_DEFAULT = Replace(COLUMN_DEFAULT, '"', splitchar)
            _ret = ' Default \'' + COLUMN_DEFAULT + '\''
        elif (_select1 == 11):
            if COLUMN_DEFAULT == 'true' or COLUMN_DEFAULT == 'on' or COLUMN_DEFAULT == 'yes':
                COLUMN_DEFAULT = 1
                COLUMN_DEFAULT = 0
            _ret = ' Default ' + str(COLUMN_DEFAULT) + ''
        elif (_select1 == 128):
            _ret = ' Default 0x' + COLUMN_DEFAULT + ''
        elif (_select1 == 7):
            if COLUMN_DEFAULT == 'now()' or COLUMN_DEFAULT == 'date()' or COLUMN_DEFAULT == 'time()':
                COLUMN_DEFAULT = 'getdate()'
            if COLUMN_DEFAULT[:1] == '#':
                COLUMN_DEFAULT = Replace(COLUMN_DEFAULT, '#', '\'')
            _ret = ' Default ' + COLUMN_DEFAULT + ''
        else:
            _ret = ' Default ' + COLUMN_DEFAULT + ''
        return _ret

    def __defaultStrfilter(self, s):
        _ret = None
        s = str(s.Value)
        while s[:1] == '"':
            s = s[1:]#Mid(s, 2)
        while s[:-1] == '"':#Right(s, 1) == '"':
            s = s[:len(s) - 1]# Left(s, Len(s) - 1)
        while s[:1] == '\'':#Left(s, 1) == '\'':
            s = s[1:]# Mid(s, 2)
        while s[:-1] == '\'':#Right(s, 1) == '\'':
            s = s[:len(s) - 1]#Left(s, Len(s) - 1)
        _ret = s
        return _ret

    def __nullStr(self, IS_NULLABLE, tablename, columnName):
        _ret = None
        if IS_NULLABLE.Value:
            if self.__getPrimaryKey(tablename, columnName) == '':
                _ret = ' null '
            else:
                _ret = ' not null '
        else:
            _ret = ' not null '
        return _ret
    
##    def __GetAutoincrementCoulmnT(self, tablename):
##        _ret = None
##        self.rs.Open('select * from [' + tablename + '] where 1=0', self.__conn, 0, 1)
##        for i in vbForRange(0, self.rs.Fields.Count - 1):
##            if self.rs.Fields[i].Properties('isAutoIncrement').Value == True:
##                _ret = self.rs.Fields[i].Name
##                self.rs.Close()
##                return _ret
##        self.rs.Close()
##        return _ret
    def __init__(self):
        self.rs = win32com.client.Dispatch('adodb.recordSet')
        #self.setDbName('J:\\nb\\cs\\access2000\\data.mdb')
    def setDbName(self, mdbName):
        try:
            self.db_name = mdbName
            self.fn = self.db_name.split("\\")[-1]
#            print "filename:" + self.fn
            self.__connstr = 'Provider=Microsoft.Jet.OLEDB.4.0;Data Source=' + self.db_name
            self.__conn = win32com.client.Dispatch('ADODB.Connection')
            self.__conn.Open(self.__connstr)
        except com_error, e:
            print e[2][2]
            raise MyError(1, e[2][2])
    def setCon(self, con):
        self.__conn = con
    def getTables(self):
        r = []
        tbls = self.__conn.OpenSchema(20)
        tbls.Filter = ' TABLE_TYPE=\'TABLE\' '
        while not tbls.EOF:
            r.append(tbls.Fields('TABLE_Name').Value)
            tbls.MoveNext()
        return(r)
    def getTableColumnType(self, tablename):
        cols = self.__conn.OpenSchema(4)
        cols.Filter = 'Table_name=\'' + tablename + '\''
        if cols.EOF:
            return
        autoclumn = self.__GetAutoincrementCoulmnT(tablename)
        cname = []
        ctype = []
        n = 0
        while 1:
            n = n + 1
            cols.Filter = 'Table_name=\'' + str(tablename) + '\' and ORDINAL_POSITION=' + str(n)
            if cols.EOF:
                break
            if autoclumn == cols.Fields('Column_name').Value:
                cname.append(cols.Fields('Column_name').Value)
                ctype.append("integer")
            else:
                tp = self.__datatypeStr(cols.Fields('DATA_TYPE'), cols.Fields('CHARACTER_MAXIMUM_LENGTH'))
                cname.append(cols.Fields('Column_name').Value)
                ctype.append(tp)
        cols.Close()
        return (cname, ctype)
    def execCmd(self, s):
        try:
            self.__conn.Execute(s)
        except com_error, e:
            print e[2][2]
            raise MyError(1, e[2][2])
    def execQuery(self, s):
        try:
            rs = self.__conn.Execute(s)
            rs = rs[0]
            r = []
            n = rs.Fields.Count
            a = []
            for i in range(n):
                x = rs.Fields(i).Name
                a.append(x)
            r.append(a)
            while not rs.EOF:
                n = rs.Fields.Count
                b = []
                for i in range(n):
                    x = rs.Fields(i).Value
                    b.append(x)
                r.append(b)
                rs.MoveNext()
            #self.__conn.Close()
            return(r)
        except com_error, e:
            print e[2][2]
            raise MyError(1, e[2][2])
    def exportAll(self, outpath):
        cmdtable = self.createAccessSql()
        cmddata = self.export()
        saveUnicode(outpath, cmdtable + cmddata)
        
    def export(self):
        r = ""
        tables = self.getTables()
        for tblname in tables:
            cmds = self.exportTable(tblname)
            for cmd in cmds:
                r = r + cmd + ";\r\n"
        return r
    def  exportTable(self, tblname):
        (name, dtype) = self.getTableColumnType(tblname)
        columns = ''
        for name1 in name[:-1]:
            columns = columns + name1 + ","
        columns = columns + name[-1]
        cmd1 = "select " + columns + " from  " + tblname
        r = self.execQuery(cmd1)
        r = r[1:]
        cmds = []
        for r1 in r:
            cmds.append(self.exportOneRec(tblname, name, r1, dtype))
        return(cmds)
    def exportCondition(self, tblname, condition):
        (name, dtype) = self.getTableColumnType(tblname)
        columns = ''
        for name1 in name[:-1]:
            columns = columns + name1 + ","
        columns = columns + name[-1]
        cmd1 = "select " + columns + " from  " + tblname + " " + condition
        r = self.execQuery(cmd1)
        r = r[1:]
        cmds = []
        for r1 in r:
            cmds.append(self.exportOneRec(tblname, name, r1, dtype))
        return(cmds)

    def toDBstr(self, value, dtype):
        if len(dtype) > 7 and dtype[0:7] == "varchar":
            return("'" + unicode(value) + "'")
        else:
            if value == None:
                return("0")
            else:
                return(unicode(value))
    def exportOneRec(self, tblname, name, value, dtype):
        cmd = "insert into [" + tblname + "]("
        for name1 in name:
            cmd = cmd + "[" + name1 + "],"
        cmd = cmd[:-1]
        cmd = cmd + ") values("
        n = len(value)
        for i in range(n):
            cmd = cmd + self.toDBstr(value[i], dtype[i]) + ","
        cmd = cmd[:-1] + ")"
        return(cmd)
    def createAccessSql(self):#,db_name,opth):
        tablecmds = self.createAccessSqlCmd()
        r = ""
        for tcmd in tablecmds:
            for cmd in tcmd:
                r = r + cmd + "\r\n"
        return r
    def createAccessSqlCmd(self):#,db_name,opth):
        tablecmds = []
        tablenames = []
        tbls = self.__conn.OpenSchema(20)
        tbls.Filter = ' TABLE_TYPE=\'TABLE\' '
        while not tbls.EOF:
            tablenames.append(tbls.Fields('TABLE_Name').Value)
            tbls.MoveNext()
        tbls.Filter = 0
        tbls.Close()
        tbls = None
        #export table
        for tablename in tablenames:
            a = self.CreatTableSql(tablename)
            tablecmds.append(a)
        return tablecmds

    def CreatTableSql(self, tablename):
        _ret = None
        #linesplit="\r\n"
        linesplit = "\r\n"
        cmds = []
        mydefault = []
        isexec = 0
        cols = self.__conn.OpenSchema(4)
        splitchar = ''
        splitchar1 = ''
        cols.Filter = 'Table_name=\'' + tablename + '\''
        if cols.EOF:
            return _ret
        autoclumn = self.__GetAutoincrementCoulmnT(tablename)
        TmpStr1 = 'CREATE TABLE [' + tablename + '] (' + splitchar1 + linesplit
        if autoclumn <> None:
            autoclumnStr = '    ' + splitchar + '[' + autoclumn + '] autoincrement'
        n = 0
        while 1:
            n = n + 1
            cols.Filter = 'Table_name=\'' + unicode(tablename) + '\' and ORDINAL_POSITION=' + str(n)
            if cols.EOF:
                break
            if n > 1:
                TmpStr1 = TmpStr1 + ',' + splitchar1 + linesplit
            if autoclumn == cols.Fields('Column_name').Value:
                TmpStr1 = TmpStr1 + autoclumnStr
            else:
                s1 = self.__datatypeStr(cols.Fields('DATA_TYPE'), cols.Fields('CHARACTER_MAXIMUM_LENGTH'))
                s2 = self.__nullStr(cols.Fields('IS_NULLABLE'), tablename, cols.Fields('Column_name'))
                dstr = self.__defaultStr(cols.Fields('DATA_TYPE').Value, cols.Fields('COLUMN_DEFAULT'), isexec)
                if dstr <> "":
                    cmd = "ALTER TABLE [" + unicode(tablename) + "] ALTER COLUMN [" + cols.Fields('Column_name').Value + "] SET " + dstr
                    mydefault.append('' + cmd + ';\n')
                TmpStr1 = TmpStr1 + ' ' + splitchar + '[' + unicode(cols.Fields('Column_name')) + '] ' + s1 + s2
            cols.MoveNext()
        TmpStr1 = TmpStr1 + splitchar1 + linesplit + '  ' + splitchar + ') '
        cols.Close()
        TmpStr1 = TmpStr1 + splitchar1 + linesplit + '' + splitchar + ';'
        cmds.append(TmpStr1)
        s11 = self.__getInxArr(tablename)
        InxArr = s11.split(',')
        cols = self.__conn.OpenSchema(12)
        for i in range(len(InxArr)):
            cols.Filter = 'Table_name=\'' + tablename + '\' and index_name=\'' + InxArr[i] + '\''
            kstr = ''
            TmpStr1 = ''
            if not self.__isForeignIndex(tablename, InxArr[i]):
                while not cols.EOF:
                    kstr = kstr + ',[' + cols.Fields('column_name').Value + '] ' + self.__GetInxDesc(tablename, InxArr[i], cols.Fields('column_name'))
                    cols.MoveNext()
                if self.__isPrimaryKey(tablename, InxArr[i]):
                    TmpStr1 = TmpStr1 + 'Alter TABLE [' + tablename + ']  ADD Primary Key(' + kstr[1:] + ') [PK_' + tablename + '];'
                else:
                    TmpStr1 = TmpStr1 + 'CREATE '
                    if self.__isUnique(tablename, InxArr[i]):
                        TmpStr1 = TmpStr1 + 'Unique '
                    TmpStr1 = TmpStr1 + 'INDEX [' + InxArr[i] + '] on [' + tablename + '](' + kstr[1:] + ') ;'
                TmpStr1 = TmpStr1 + linesplit 
                cmds.append(TmpStr1)
        cols.Close()
        cols.Filter = 0
        for m1 in mydefault:
            cmds.append(m1)
        return cmds
class ExportON(ExportAccess):    
    def add(self, cmds, t):
        for t1 in t:
            cmds.append(t1)
    def saveOld(self, fname, cmds):
        t = "cmds=["
        for cmd1 in cmds:
            t = t + '"""' + cmd1 + '""",\r\n'
        t = t + "]"
        saveUnicode(fname, t)
    def save(self, fname, cmds):
        t = ""
        for cmd1 in cmds:
            t = t + cmd1 + ';\r\n'
        t = t + ""
        saveUnicode(fname, t)
    def exportMethodid(self, mid):
        cmds = []
        condition = "where methodid=" + str(mid)
        t = self.exportCondition("method", "where id=" + str(mid))
        self.add(cmds, t)
        t = self.exportCondition("curvedata", condition)
        self.add(cmds, t)
        t = self.exportCondition("curvexishu", condition)
        self.add(cmds, t)
        t = self.exportCondition("standard", "")
        self.add(cmds, t)
        t = self.exportCondition("powerset", condition)
        self.add(cmds, t)
        self.save(self.fn + "_m" + str(mid) + ".sql", cmds)
    def exportMethod(self):
        cmds = []
        t = self.export("method")
        self.add(cmds, t)
        t = self.export("curvedata")
        self.add(cmds, t)
        t = self.export("curvexishu")
        self.add(cmds, t)
        t = self.export("standard")
        self.add(cmds, t)
        #t=self.export("powerset")
        #self.add(cmds,t)
        self.save(self.fn + "_allmethod.sql", cmds)
        return(cmds)
def eON():
    dbfn = r"D:\src\access_2000\data.mdb"
    con = ExportON()
    con.setDbName(dbfn)
    con.exportMethodid(77)
def test():
    dbfn = r"D:\mahongquan\CreepTesting_nh\GeneratedCode\data.mdb"
    con = ExportAccess()
    con.setDbName(dbfn)
    tablecmds = con.createAccessSql()
    saveUnicode("out.sql",tablecmds)
    for cmd in tablecmds:
        print cmd
    #con.test()    
if __name__ == "__main__":
    test()

