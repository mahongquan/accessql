# -*- coding: gb2312 -*-
import sys
import model
import os
import win32com.client
from getpath import getpath
initpath=getpath()
from  comerror import *
# import commands
class MyExcel:
    def __init__(self,tname):
        self.tname=tname
        #para='/C copy /Y "'+initpath+'\\t_'+tname+'.xls" "'+initpath+'\\gen_'+tname+'.xls"'
        para='/C copy /Y "%s\\t_%s.xls" "%s\\gen_%s.xls"' %(initpath,tname,initpath,tname)
        os.spawnl(os.P_WAIT,os.environ['COMSPEC'],para)
    def render(self,aves):
        # try:
            a=win32com.client.Dispatch("Excel.Application")
            a.visible = True
            fn=initpath + "/gen_"+self.tname+".xls"
            a.Workbooks.Open(fn)
            w = a.Worksheets("sheet1")
            curAveRow=5
            xlEdgeTop=8
            xlContinuous=1
            xlThin=2
            xlAutomatic=-4105
            xlCenter=-4108
            w.Cells(1,1).Value =model.getTableHead1()
            w.Cells(4,2).Value =aves[0].mdate
            w.Cells(4,2).NumberFormatLocal = """yyyy年m月d日"""
            for ave in aves:
                # rstr="A"+str(curAveRow)+":H"+str(curAveRow)
                # print rstr
                # w.Range(rstr).Select
                # a.Selection.Borders(xlEdgeTop).LineStyle = xlContinuous
                # a.Selection.Borders(xlEdgeTop).Weight = xlThin
                # a.Selection.Borders(xlEdgeTop).ColorIndex = xlAutomatic
                w.Cells(curAveRow,1).Value ="样品名称:"
                w.Cells(curAveRow,2).Value =ave.name
                w.Cells(curAveRow+1,1).Value =""
                w.Cells(curAveRow+2,1).Value ="C%"
                w.Cells(curAveRow+2,1).HorizontalAlignment = xlCenter
                w.Cells(curAveRow+3,1).Value ="S%"
                w.Cells(curAveRow+3,1).HorizontalAlignment = xlCenter
                curCol=2
                for s in ave.singles[:7]:
                    w.Cells(curAveRow+1,curCol).Value =s.anaxuhao
                    w.Cells(curAveRow+1,curCol).HorizontalAlignment = xlCenter
                    w.Cells(curAveRow+1,curCol).NumberFormatLocal = "G/通用格式"
                    w.Cells(curAveRow+2,curCol).Value =s.c
                    w.Cells(curAveRow+2,curCol).NumberFormatLocal = "0.00000"
                    w.Cells(curAveRow+3,curCol).Value =s.s
                    w.Cells(curAveRow+3,curCol).NumberFormatLocal = "0.00000"
                    curCol=curCol+1
                if len(ave.singles)>7:
                    curAveRow=curAveRow+3
                    w.Cells(curAveRow+1,1).Value =""
                    w.Cells(curAveRow+2,1).Value ="C%"
                    w.Cells(curAveRow+2,1).HorizontalAlignment = xlCenter
                    w.Cells(curAveRow+3,1).Value ="S%"
                    w.Cells(curAveRow+3,1).HorizontalAlignment = xlCenter
                    
                    curCol=2
                    for s in ave.singles[7:]:
                        w.Cells(curAveRow+1,curCol).Value =s.anaxuhao
                        w.Cells(curAveRow+1,curCol).HorizontalAlignment = xlCenter
                        w.Cells(curAveRow+1,curCol).NumberFormatLocal = "G/通用格式"
                        w.Cells(curAveRow+2,curCol).Value =s.c
                        w.Cells(curAveRow+2,curCol).NumberFormatLocal = "0.00000"
                        w.Cells(curAveRow+3,curCol).Value =s.s
                        w.Cells(curAveRow+3,curCol).NumberFormatLocal = "0.00000"
                        curCol=curCol+1
                if len(ave.singles)>1:
                    curAveRow=curAveRow+3
                    w.Cells(curAveRow+1,1).Value =""
                    w.Cells(curAveRow+2,1).Value ="C%"
                    w.Cells(curAveRow+2,1).HorizontalAlignment = xlCenter
                    w.Cells(curAveRow+3,1).Value ="S%"
                    w.Cells(curAveRow+3,1).HorizontalAlignment = xlCenter
                    w.Cells(curAveRow+1,2).Value ="平均值"
                    w.Cells(curAveRow+1,2).HorizontalAlignment = xlCenter
                    w.Cells(curAveRow+2,2).Value =ave.c
                    w.Cells(curAveRow+2,2).NumberFormatLocal = "0.00000"
                    w.Cells(curAveRow+3,2).Value =ave.s
                    w.Cells(curAveRow+3,2).NumberFormatLocal = "0.00000"
                    w.Cells(curAveRow+1,3).Value ="标准偏差"
                    w.Cells(curAveRow+1,3).HorizontalAlignment = xlCenter
                    w.Cells(curAveRow+2,3).Value =ave.cstd
                    w.Cells(curAveRow+2,3).NumberFormatLocal = "0.00000"
                    w.Cells(curAveRow+3,3).Value =ave.sstd
                    w.Cells(curAveRow+3,3).NumberFormatLocal = "0.00000"
                    
                curAveRow=curAveRow+4#下一个样品
            curAveRow=curAveRow+3#末尾行
            w.Cells(curAveRow,1).Value ="检验员：" 
            w.Cells(curAveRow,2).Value =aves[0].user
            w.Cells(curAveRow,7).Value ="校核："        
class Report:
    def genAveSingleReport(self):
        tname="rpt"#"aveSingle2"
        self.genAveSingleReportT(tname)
    def genAveSingleReportT(self,tname):
        aves=model.getAves()
        t=MyExcel(tname)
        t.render(aves=aves)
def main():
    r=Report()
    r.genAveSingleReport()
if __name__=="__main__":
    main()
