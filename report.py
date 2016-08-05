import sys
import jinja2
import model
import os
from export2 import saveUnicode
env=jinja2.Environment()
from getpath import getpath
initpath=getpath()
fileloader=jinja2.FileSystemLoader(initpath)
class Report:
    def genAveSingleReport(self):
        tname="aveSingle2"#"aveSingle2"
        self.genAveSingleReportT(tname)
    def genAveSingleReportT(self,tname):
        aves=model.getAves()
        global fileloader,env
        t=fileloader.load(env,"t_"+tname+".html")
        html=t.render(aves=aves)
        saveUnicode("gen_"+tname+"_report.html",html)
        os.system("start "+"gen_"+tname+"_report.html")
    def genAveSingleReportTonly(self,tname):
        aves=model.getAves()
        global fileloader,env
        t=fileloader.load(env,"t_"+tname+".html")
        html=t.render(aves=aves)
        return html
        #saveUnicode("gen_"+tname+"_report.html",html)
        #os.system("start "+"gen_"+tname+"_report.html")
        
    def genAveReport(self):
        ids=model.getSampleIds()
        for id in ids:
            self.genSingleAveReport(id)
    def genSingleAveReport(self,id):
        tname="ave"#ave2 ave3 aveOld 
        self.genSingleAveReportT(id,tname)
    def genSingleAveReportT(self,id,tname):
        html=self.genSingleAveReportTonly(id,tname)
        fn="gen_"+tname+"_sampleid"+str(id)+".html"
        saveUnicode(fn,html)  
        os.system("start "+fn)
    def genSingleAveReportTonly(self,id,tname):
        #tname="ave" ave2 ave3 aveOld 
        ave=model.getAve(id)
        dw=model.getTableHead1()
        global fileloader,env
        t=fileloader.load(env,"t_"+tname+".html")
        bh=range(1,len(ave.singles)+1)
        return t.render(ave=ave,bh=bh,danwei=dw)        
def main():
    r=Report()
    #r.genAveSingleReport()
    r.genAveReport()
if __name__=="__main__":
    main()
    #print r.getSampleIds()
    #html=r.genAveReport()
    #html=r.genTmpReport()
    #r.genAveSingleReportT("aveSingle")
    #r.genAveSingleReportT("aveSingle2")
    