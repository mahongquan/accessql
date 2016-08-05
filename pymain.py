import sys
sys.path.insert(0,"library.zip")
from getpath import getpath
initpath=getpath()
sys.path.insert(0,initpath+"\Lib")
from mymain import main
main()