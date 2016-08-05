import sys
import model
import os
from pyjon.reports import ReportFactory
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from getpath import getpath
initpath=getpath()
pdfmetrics.registerFont(TTFont('hei',os.environ["WINDIR"]+'\\Fonts\\SIMHEI.TTF'))
pdfmetrics.registerFont(TTFont('kai',os.environ["WINDIR"]+'\\Fonts\\simkai.TTF'))
class Report:
    def genAveSingleReport(self):
        tname="aveSingle2"#"aveSingle2"
        self.genAveSingleReportT(tname)
    def genAveSingleReportT(self,tname):
        self.genAveSingleReportTonly(tname)
        os.system("start "+"gen_"+tname+".pdf")
    def genAveSingleReportTonly(self,tname):
        aves=model.getAves()
        template = initpath+tname+'.xml'
        factory = ReportFactory()
        factory.render_template(
                template_file=template,
                aves=aves)
        # print dir(factory)
        factory.render_document("gen_"+tname+".pdf")
        factory.cleanup()
    def genOneAveReport(self):
        tname="OneAve"#ave2 ave3 aveOld 
        #tname="table"
        self.genOneAveReportT(id,tname)
    def genOneAveReportT(self,id,tname):
        aves=model.getAves()
        template = initpath+tname+'.xml'
        factory = ReportFactory()
        #bh=range(1,len(ave.singles)+1)
        factory.render_template(
                template_file=template,
                aves=aves)
        factory.render_document("gen_"+tname+".pdf")
        factory.cleanup()
        os.system("start "+"gen_"+tname+".pdf")
def genAveSingleReport():
    r=Report()
    r.genAveSingleReportT("aveSingle")
def main():
    r=Report()
    r.genOneAveReport()
if __name__=="__main__":
    main()
    #genAveSingleReport()
    