import sqlalchemy
import codecs
import datetime
from sqlalchemy import create_engine
from getpath import getpath
initpath=getpath()
engine = create_engine('access:///'+initpath+'data.mdb', echo=False)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey,Float,DateTime,Boolean,Unicode
from sqlalchemy.orm import relation, backref
import mytime
from  comerror import *
from export2 import saveUnicode
Base = declarative_base()
class Tmpid(Base):
    __tablename__ = 'tmpid'
    
    sampleid = Column(Integer, primary_key=True)
def insertTmpId(id):
    #print dir(session)
    try:
        t=Tmpid()
        t.sampleid=id
        session.add(t)
        session.flush()
        session.commit()
    except sqlalchemy.exc.IntegrityError,e:
        session.rollback()
    except sqlalchemy.exc.InvalidRequestError,e:
        session.rollback()
def clearAll():
    s1 = session.query(Tmpid).all()    
    for s in s1:
        session.delete(s)
    session.commit()
class Program(Base):
    __tablename__ = 'program'
    
    id = Column(Integer, primary_key=True)
    tablehead1 = Column(String)
class Sample(Base):
    __tablename__ = 'sample'

    id = Column(Integer, primary_key=True)
    anaxuhao= Column(Integer)
    name = Column(String)
    c=Column(Float)
    s=Column(Float)
    mdate=Column(DateTime)
    user = Column(String)
    sampleid = Column(Integer, ForeignKey('sampleave.sampleid'))
    
    #ave= relation(SampleAve, backref=backref('singles'),order_by=anaxuhao)
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Sample('%s') c=%f s=%f>" % (self.name,self.c,self.s)    
class SampleAve(Base):
    __tablename__ = 'sampleave'

    sampleid = Column(Integer, primary_key=True)
    name = Column(String)
    c=Column(Float)
    s=Column(Float)
    cstd=Column(Float)
    sstd=Column(Float)
    num = Column(Integer)
    mdate=Column(DateTime)
    user = Column(String)
    #singles= relationship(Sample, backref=backref('addresses', order_by=id))
    singles = relation(Sample, order_by=Sample.anaxuhao, backref="ave")
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<SampleAve('%s') c=%f s=%f>" % (self.name,self.c,self.s) 
class Method(Base):
    __tablename__ = 'method'

    id = Column(Integer)
    user = Column(Unicode, primary_key=True)
    name = Column(Unicode, primary_key=True)
    power=Column(Float)
    cswitch=Column(Float)
    sswitch=Column(Float)
    sampletime = Column(Integer)
    flushtime = Column(Integer)
    powertime = Column(Integer)
    wlc=Column(Float)
    wls=Column(Float)
    jieqi=Column(Boolean)
    def __repr__(self):
        return "Method('%s')" % (self.name) 
class CurveXishu(Base):
    __tablename__ = 'curvexishu'

    methodid = Column(Integer, primary_key=True)
    ele = Column(String, primary_key=True)
    x0=Column(Float)
    x1=Column(Float)
    r=Column(Float)
    linexishu = Column(Float)
    blankarea = Column(Float)
    must00= Column(Boolean)
    bjsp=Column(Float)
    panju=Column(Float)

    def __repr__(self):
        return "CurveXishu(%d,%s)" % (self.methodid,self.ele) 
class CurveData(Base):
    __tablename__ = 'curvedata'

    id = Column(Integer, primary_key=True)
    methodid = Column(Integer)
    ele=Column(String)
    eleArea=Column(Float)
    weight=Column(Float)
    sampleid = Column(Float)
    quan = Column(Float)
    wlweight= Column(Float)
    calcconc=Column(Float)
    standardid=Column(Integer)

    def __repr__(self):
        return "CurveDate(%d,%s)" % (self.methodid,self.ele) 
class Standard(Base):
    __tablename__ = 'standard'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    cconc=Column(Float)
    sconc=Column(Float)
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return "<Standard('%s') c=%f s=%f>" % (self.name,self.cconc,self.sconc)  
    def __unicode__(self):
        return "<Standard('%s') c=%f s=%f>" % (self.name,self.cconc,self.sconc)  
class Chanel(Base):
    __tablename__ = 'chanel'

    id = Column(Integer, primary_key=True)
    chanel= Column(Integer)
    enable=Column(Boolean)
    color=Column(Integer)
    title=Column(Unicode)
    def __init__(self, name):
        self.title = name
    def __repr__(self):
        return "<Chanel('%s') channel=%d>" % (self.title,self.chanel)  
    def __unicode__(self):
        return "<Chanel('%s') channel=%d>" % (self.title,self.chanel)  
class User(Base):
    __tablename__ = 'muser'

    id = Column(Integer)
    mname= Column(Unicode,primary_key=True)
    mpassword=Column(Boolean)
    methodid=Column(Integer)
    def __init__(self, name):
        self.mname = name
    def __repr__(self):
        return "<User('%s')>" % (self.mname)  
    def __unicode__(self):
        return "<User('%s')>" % (self.mname)          
def getSampleIds():
    s1 = session.query(Tmpid).all()    
    ids=[]
    for s in s1:
        ids.append(s.sampleid)
    return ids
def getAveToday():
    print dir(datetime)
    #bdate=
    tfrom=mytime.todaybegin()
    s1 = session.query(SampleAve).filter(SampleAve.mdate>tfrom).filter(SampleAve.mdate<mytime.todaybegin()).all()
    return s1
def getAveBetween(tfrom,tto):
    s1 = session.query(SampleAve).filter(SampleAve.mdate>tfrom).filter(SampleAve.mdate<tto).all()
    return s1    
def getAve(id):    
    s1 = session.query(SampleAve).filter_by(sampleid=id).first()
    return s1
def getAveAll():
    aves = session.query(SampleAve).all()
    return aves
def getTableHead1():    
    s1 = session.query(Program).filter_by(id=1).first()
    return s1.tablehead1
def getAves():
    ids=getSampleIds()    
    aves=[]
    for id in ids:
        ave = session.query(SampleAve).filter_by(sampleid=id).first()
        if ave<>None:
            aves.append(ave)
    return aves    
metadata = Base.metadata        
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()
if __name__=="__main__":
    # s1 = session.query(SampleAve).filter_by(name='h:0.63').first()
    # print s1
    # print s1.singles
    # print dir(s1.singles)
    #print getTableHead1()
    #print getSampleIds()
    #print getAveToday()
    # aves=getAves()
    # ss=aves[0].singles
    # for s in ss:
        # print s.anaxuhao
    try:
        p=""
        for s in session.query(User).all():
            p=p+unicode(s)+"\n"
        saveUnicode("out.txt",p)
    except sqlalchemy.exc.DBAPIError,e:
        n=None
        exec("n='''"+e.message+"'''")
        print n