#!/usr/bin/env python
#Boa:App:BoaApp
#from wxPython.wx import *
#from report import main as themain
import sys
import logging
import logging.config
from getpath import getpath
initpath=getpath()
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename=initpath+'/myapp.log')
logging.debug('A debug message')
logging.info('Some information')
logging.warning('A shot across the bows')

#logging.config.fileConfig(initpath+"/logging.conf")
# # create logger
# logger = logging.getLogger("simple_example")
# logger.setLevel(logging.DEBUG)
# # create console handler and set level to debug
# ch = logging.StreamHandler()
# ch.setLevel(logging.DEBUG)
# # create formatter
# formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
# # add formatter to ch
# ch.setFormatter(formatter)
# # add ch to logger
# logger.addHandler(ch)

# # "application" code
# logger.debug("debug message")
# logger.info("info message")
# logger.warn("warn message")
# logger.error("error message")
# logger.critical("critical message")
logging.debug(sys.argv)
#['J:\\usb\\usb-art\\CS_src\\pymain.exe', 'excel', 'rpt']
def main():
    if len(sys.argv)>=2:
        if sys.argv[1]=="excel":
            from reportExcel import main as themain
        elif sys.argv[1]=="pdf":
            from reportPdf import main as themain
        elif sys.argv[1]=="rtf":
            from reportRtf import main as themain
        else:
            from report import main as themain
    else:
        from report import main as themain
    themain()
if __name__=="__main__":
    main()