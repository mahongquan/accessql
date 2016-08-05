import sys
import os
from PyQt4.QtCore import QFile,QIODevice,SIGNAL,QStringList
from PyQt4.QtGui import QPushButton,QApplication,QLineEdit,QListWidget,QTextEdit,QTableWidget,QTableWidgetItem,QMenu,QAction,QFileDialog
from PyQt4 import  uic
from getpath import getpath
inipath = getpath()
import model
import report
import reportPdf
from PyQt4.QtWebKit import *
from OpenSample import OpenSample
class MyApp(QApplication):
    def __init__(self):
        QApplication.__init__(self,[])
        self.mainw=uic.loadUi("main.ui")#l.loadUi(f,None)
        self.pushbutton_go=self.mainw.findChild(QPushButton,"pushButton_go")
        QApplication.connect(self.pushbutton_go,SIGNAL('clicked()'),self.handlego)
        
        self.pushButton_pdf=self.mainw.findChild(QPushButton,"pushButton_pdf")
        QApplication.connect(self.pushButton_pdf,SIGNAL('clicked()'),self.handlepdf)

        
        self.grid1=self.mainw.findChild(QTableWidget,"tableWidget") 
        self.web1=self.mainw.findChild(QWebView,"webView")
        self.loadData()
        self.actionOpen_sample=self.mainw.findChild(QAction,"actionOpen_sample")
        self.connect(self.actionOpen_sample,SIGNAL('triggered (bool)'),self.OnOpenSample)
        
        self.actionClear_all=self.mainw.findChild(QAction,"actionClear_all")
        self.connect(self.actionClear_all,SIGNAL('triggered (bool)'),self.ClearAll)
    def ClearAll(self,b):
        model.clearAll()
        self.loadData()
    def handlepdf(self):
        reportPdf.main()
    def OnOpenSample(self,b):
        print "open"
        o=OpenSample()
        self.loadData()
    def loadData(self):
        aves=model.getAves()
        names =["sampleid","name","c","s","cstd","sstd","mdate","user"]
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
    def handlego(self):
        r=report.Report()
        html=r.genAveSingleReportTonly("aveSingle2")
        self.web1.setHtml(html)
        pass
def main():
    a=MyApp()
    a.mainw.show()
    sys.exit(a.exec_())
        
if __name__=="__main__":
    main()