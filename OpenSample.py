import model
from PyQt4 import  uic
from PyQt4.QtCore import QFile,QIODevice,SIGNAL,QStringList
from PyQt4.QtGui import QPushButton,QApplication,QLineEdit,QListWidget,QTextEdit,QTableWidget,QTableWidgetItem,QMenu,QAction,QFileDialog,QDateTimeEdit,QSpinBox,QTableWidgetSelectionRange
import mytime
from getpath import getpath
initpath = getpath()
class OpenSample:
    def __init__(self):
        self.dlg=uic.loadUi(initpath+"opensample.ui")
        self.grid1=self.dlg.findChild(QTableWidget,"table_data") 
        self.dateTimeEdit_begin=self.dlg.findChild(QDateTimeEdit,"dateTimeEdit_begin")
        self.dateTimeEdit_begin.setDateTime(mytime.todaybegin())
        
        self.spinBox_month=self.dlg.findChild(QSpinBox,"spinBox_month")
        QApplication.connect(self.spinBox_month,SIGNAL("valueChanged  (int)"),self.monthChange)
        self.spinBox_day=self.dlg.findChild(QSpinBox,"spinBox_day")
        QApplication.connect(self.spinBox_day,SIGNAL("valueChanged  (int)"),self.dayChange)
        
        QApplication.connect(self.dateTimeEdit_begin,SIGNAL('dateTimeChanged (QDateTime)'),self.btimeChange)
        self.dateTimeEdit_end=self.dlg.findChild(QDateTimeEdit,"dateTimeEdit_end")
        self.dateTimeEdit_end.setDateTime(mytime.todayend())
        self.loadData()
        self.pushButton_open=self.dlg.findChild(QPushButton,"pushButton_open")
        QApplication.connect(self.pushButton_open,SIGNAL('clicked()'),self.handleopen)
        
        self.pushButton_query=self.dlg.findChild(QPushButton,"pushButton_query")
        QApplication.connect(self.pushButton_query,SIGNAL('clicked()'),self.handlequery)
        
        self.pushButton_selectall=self.dlg.findChild(QPushButton,"pushButton_selectall")
        QApplication.connect(self.pushButton_selectall,SIGNAL('clicked()'),self.selectall)
        
        self.dlg.exec_()
    def selectall(self):
        rs=self.grid1.rowCount()
        cs=self.grid1.columnCount()
        # for i in range(ct):
            # print i
            # self.grid1.selectRow(i)
        #self.grid1.selectRow(0)
        r=QTableWidgetSelectionRange(0,0,rs-1,cs-1)
        # print dir(r)
        self.grid1.setRangeSelected(r,1 )
    def monthChange(self,v):
        (btime,etime)=mytime.beforeMonth(v)
        self.dateTimeEdit_begin.setDateTime(btime)
        self.dateTimeEdit_end.setDateTime(etime)
    def dayChange(self,v):
        (btime,etime)=mytime.beforeDay(v)
        self.dateTimeEdit_begin.setDateTime(btime)
        self.dateTimeEdit_end.setDateTime(etime)
    
    def handlequery(self):
        btime=self.dateTimeEdit_begin.dateTime()
        etime=self.dateTimeEdit_end.dateTime()
        tfrom=btime.toPyDateTime()
        tto=etime.toPyDateTime()
        aves=model.getAveBetween(tfrom,tto)
        self.showdata(aves)
    def btimeChange(self,d):
        print d
    def handleopen(self):
        l=self.grid1.selectionModel()
        rs=l.selectedRows()
        for r in rs:
            row=r.row()
            id=int(self.grid1.item(row,0).text())
            #print "========"
            #print row,id
            model.insertTmpId(id)
            # t=model.Tmpid()
            # t.sampleid=id
            # model.session.add(t)
        #model.session.commit()
        self.dlg.accept()
    def showdata(self,aves):
        names =["sampleid","name","c","s","cstd","sstd","num","mdate","user"]
        m1 = len(aves)
        if m1 > 0:
            n1 = len(names)
            self.grid1.setRowCount(m1);
            self.grid1.setColumnCount(n1);
            for j in range(n1):
                for i in range(m1):
                    #print aves[i].
                    #cmdstr="print aves[i]."+names[j]
                    cmdstr="self.grid1.setItem(i, j, QTableWidgetItem(unicode(aves[i]."+names[j]+")))"
                    exec(cmdstr)
                    #grid.setItem(i, j, QTableWidgetItem(unicode(aves[i][j])))
        else:
            n1 = len(names)
            self.grid1.setRowCount(0);
            self.grid1.setColumnCount(n1);
        self.grid1.setHorizontalHeaderLabels(names)        
   
    def loadData(self):
        aves=model.getAveToday()
        self.showdata(aves)
if __name__=="__main__"        :
    a=QApplication([])
    o=OpenSample()