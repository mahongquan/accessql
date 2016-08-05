# -*- coding: utf-8 -*-
import PyRTF
import sys
import model
import os
import win32com.client
from getpath import getpath
initpath=getpath()
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename=initpath+'/myapp.log')
logging.debug('A debug message')
logging.info('Some information')
logging.warning('A shot across the bows')
logging.debug('in reportrtf')
from  comerror import *
def OpenFile( name ) :
    return file( '%s.rtf' % name, 'w' )
def getFont(nm):
    nm=nm.encode("gb2312")
    r=""
    for unichar in nm:
        point = ord(unichar)
        if point < 128:
            r=r+unichar
        else:
            r=r+"\\'%x" % point
    return PyRTF.Font(r,"nil",134,2,'02010600030101010101')
def MakeExample3(aves) :
    doc     = PyRTF.Document()
    ss      = doc.StyleSheet
    ht=getFont(u"黑体")#PyRTF.Font(r"\'ba\'da\'cc\'e5",'nil',134,2,'02010600030101010101')
    st=getFont(u"宋体")#PyRTF.Font(r"\'cb\'ce\'cc\'e5",'nil',134,2,'02010600030101010101')
    ss.Fonts.append(ht)
    ss.Fonts.append(st)
    
    section = PyRTF.Section()
    doc.Sections.append( section )
    para_props = PyRTF.ParagraphPS( alignment=PyRTF.ParagraphPS.CENTER )
    # p = PyRTF.Paragraph( PyRTF.UNICODE(u'红外碳硫分析检验记录',size=32,font=ht),para_props)
    # section.append( p )
    
    text_props = PyRTF.TextPropertySet()
    text_props.SetFont(ht)
    text_props.SetSize(32)
    u=PyRTF.Unicode(u'红外碳硫分析检验记录', text_props )
    p = PyRTF.Paragraph(u,para_props)
    section.append( p )
    
    p1 = PyRTF.Paragraph("")
    section.append(p1)
    # 
    table = PyRTF.Table( 720 *3 ,
                   720 *1,
                   int(720 *2.5),
                   int(720 *2.5),
                   #TabPS.DEFAULT_WIDTH * kd,
                   720 *5 ,alignment=PyRTF.TabPS.CENTER)
    thin_edge  = PyRTF.BorderPS( width=20, style=PyRTF.BorderPS.SINGLE )
    thick_edge = PyRTF.BorderPS( width=30, style=PyRTF.BorderPS.SINGLE )
    thin_frame1  = PyRTF.FramePS( thin_edge,  thin_edge,  thin_edge,  thin_edge )
    thick_frame1 = PyRTF.FramePS( thick_edge,  thin_edge,  thin_edge,  thin_edge)
    curFrame=thick_frame1
    c1 = PyRTF.Cell(PyRTF.Paragraph(u"名称") ,curFrame)
    c1.SetSpan(2)
    c3 = PyRTF.Cell( PyRTF.Paragraph(u"C%" ) ,curFrame)
    c4 = PyRTF.Cell( PyRTF.Paragraph(u"S%" ) ,curFrame)
    #c5 = Cell( Paragraph( str(s.user) ) )
    c6 = PyRTF.Cell( PyRTF.Paragraph(u"分析时间") ,curFrame)
    table.AddRow( c1, c3,c4,c6 )
    from PyRTF import Cell,Paragraph,ParagraphPS
    for ave in aves:
        i=0
        for s in ave.singles:
            if i==0:
                curFrame=thick_frame1
            else:
                curFrame=thin_frame1
            if len(ave.singles)>1:
                c1 = Cell( Paragraph( s.name) ,curFrame)
                c2 = Cell( Paragraph( str(s.anaxuhao )  ) ,curFrame)
                c3 = Cell( Paragraph( "%.5f" % s.c ) ,curFrame)
                c4 = Cell( Paragraph( "%.5f" % s.s ) ,curFrame)
                #c5 = Cell( Paragraph( str(s.user) ) )
                c6 = Cell( Paragraph( str(s.mdate) ) ,curFrame)
                table.AddRow( c1, c2, c3,c4,c6 )
            else:
                c1 = Cell( Paragraph( s.name) ,curFrame)
                c1.SetSpan(2)
                c3 = Cell( Paragraph( "%.5f" % s.c ) ,curFrame)
                c4 = Cell( Paragraph( "%.5f" % s.s ) ,curFrame)
                #c5 = Cell( Paragraph( str(s.user) ) )
                c6 = Cell( Paragraph( str(s.mdate) ) ,curFrame)
                table.AddRow( c1, c3,c4,c6 )
            i=i+1
        curFrame=thin_frame1
        if len(ave.singles)>1:
            c1 = Cell( Paragraph( u"平均值",ParagraphPS( alignment=ParagraphPS.RIGHT)),curFrame )
            c1.SetSpan(2)
            #c2 = Cell( Paragraph("") )
            c3 = Cell( Paragraph( "%.5f" % ave.c ),curFrame )
            c4 = Cell( Paragraph( "%.5f" % ave.s ),curFrame )
            #c5 = Cell( Paragraph( str(s.user) ) )
            c6 = Cell( Paragraph( "" ) ,curFrame)
            table.AddRow( c1,  c3,c4,c6 )
            c1 = Cell( Paragraph( u"标准偏差",ParagraphPS( alignment=ParagraphPS.RIGHT)) ,curFrame)
            c1.SetSpan(2)
            #c2 = Cell( Paragraph("") )
            c3 = Cell( Paragraph( "%.5f" % ave.cstd ) ,curFrame)
            c4 = Cell( Paragraph( "%.5f" % ave.sstd ),curFrame )
            #c5 = Cell( Paragraph( str(s.user) ) )
            c6 = Cell( Paragraph( "" ),curFrame )
            table.AddRow( c1,  c3,c4,c6 )
    
    section.append( table )
    return doc
def main():
    aves=model.getAves()    
    doc3 = MakeExample3(aves=aves)
    DR = PyRTF.Renderer()
    DR.Write( doc3, OpenFile(initpath+'/gen_SingleAve' ) )
    logging.debug('after write')
    cmd=r'"%s%s.rtf"' %(initpath,'gen_SingleAve')
    #start "I:\Aptana Studio 3 Workspace\ncs_report\src\gen_singleave.rtf"
    #os.system(cmd)
    os.spawnl(os.P_NOWAIT,os.environ['COMSPEC'],"/C  "+cmd)
if __name__=="__main__":
    main()
    #print getFont(u"黑体")