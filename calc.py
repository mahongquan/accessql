import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.uic.Loader.loader import DynamicUILoader
from My8112 import My8112
class MyWidget2(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.card1=My8112()
#load ui
        f=QFile("calc.ui")
        f.open(QIODevice.ReadOnly)
        l=DynamicUILoader()
        myWidget=l.loadUi(f,self)
        f.close()
#add to dialog
        layout =QVBoxLayout()
        layout.addWidget(myWidget)
#signal
        self.connect(self,SIGNAL('finished(int)'),self.myclose)
        for i in range(8):
            exec('self.p%d=myWidget.findChild(QCheckBox,"p%d")' % (i,i))
            exec('self.connect(self.p%d,SIGNAL("toggled(bool)"),self.handled%d)' % (i,i))
    def myclose(self,t):
        print "finished"
        self.card1.closeAll()
    def handled1(self,b):
        #print self.p1,dir(self.p1)
        self.card1.handleDigit(1,b)
        #self.updateui()
    def handled2(self,b):
        self.card1.handleDigit(2,b)
        #self.updateui()
    def handled3(self,b):
        self.card1.handleDigit(3,b)
        #self.updateui()
    def handled4(self,b):
        self.card1.handleDigit(3,b)
        #self.updateui()
    def handled5(self,b):
        self.card1.handleDigit(4,b)
        #self.updateui()
    def handled6(self,b):
        self.card1.handleDigit(6,b)
        #self.updateui()
    def handled7(self,b):
        self.card1.handleDigit(7,b)
        #self.updateui()
    def handled8(self,b):
        self.card1.handleDigit(8,b)
        #self.updateui()
    def handled9(self,b):
        self.card1.handleDigit(9,b)
        #self.updateui()
    def handled0(self,b):
        self.card1.handleDigit(0,b)
if __name__=="__main__":
    a=QApplication([''])
    dlg = MyWidget2()
    dlg.show();
    sys.exit(a.exec_())
