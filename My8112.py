# -*- coding: gbk -*-
from p8112 import *
from ctypes import *
import operator
# Public Function BitSetChar(Number As Byte, ByVal Bit As Byte) As Byte
  # If Bit = 7 Then
    # Number = &H80 Or Number
  # ElseIf Bit < 7 Then
    # Number = (2 ^ Bit) Or Number
  # End If
  # BitSetChar = Number
# End Function

 
# '*----------------------------------------------------------*
# '* Name       : BitClear                                    *
# '*----------------------------------------------------------*
# '* Purpose    : Clears a given Bit in Number                *
# '*----------------------------------------------------------*
# Public Function BitClearChar(Number As Byte, ByVal Bit As Byte) As Byte
  # If Bit = 7 Then
    # Number = &H7F And Number
  # ElseIf Bit < 7 Then
    # Number = ((2 ^ Bit) Xor &HFF) And Number
  # End If

  # BitClearChar = Number
# End Function
vlvs={}
vlvs["开关炉"]=1
vlvs["六通阀"]=2
vlvs["封顶"]=4
vlvs["加样"]=3
vlvs["投样"]=5
vlvs["节气"]=7
def BitSetChar(Number,Bit):
	if(Bit==7):
		Number=operator.or_(0x80,Number.value)
	elif Bit< 7:
		Number = operator.or_(2** Bit,  Number.value)
	return c_ubyte(Number)

def BitClearChar(Number,Bit):
	if(Bit==7):
		Number= operator.and_(0x7F ,Number.value)
	elif Bit< 7:
		Number = operator.and_(operator.xor(2** Bit,0xFF),Number.value)
	return c_ubyte(Number)
class My8112:
	def handleDigit(self,vlv,bool):
		if bool:
			self.openVLV(vlv)
		else:
			self.closeVLV(vlv)
	def closeAll(self):
		self.b1=c_ubyte(0)
		self.b2=c_ubyte(0)
		self.closeVLV(0)
	def __init__(self):
		self.b1=c_ubyte(0)
		self.b2=c_ubyte(0)
		self.link()
	def link(self):
		 self.card = W_812_Initial(0, 576)
		 print "card=",self.card
	def unlink(self):
		if (self.card >= 0):
			print "release"#
	def newDA(self,chanel , v):
		result = W_812_DA(chanel, v)
	def getchanelVolt(self,chanel):
		l=c_int()
		print W_812_AD_Set_Channel(chanel)
		print W_812_AD_Aquire(byref(l))
		return l.value / 4095.0 * 20 -10
	def closeVLV(self,v):
		if (v >= 0 and v <= 7):
			self.b1= BitClearChar(self.b1, v)
			W_812_DO(0, self.b1)
		elif v >= 8 and v <= 15:
			self.b2 = BitClearChar(self.b2, v - 8)
			W_812_DO(1, self.b2)
	def openVLV(self,v):
		if (v >= 0 and v <= 7):
			self.b1= BitSetChar(self.b1, v)
			print W_812_DO(0, self.b1)
		elif v >= 8 and v <= 15:
			self.b2 = BitSetChar(self.b2, v - 8)
			print W_812_DO(1, self.b2)
		self.printByte()
	def printByte(self):
		print self.b1,self.b2
def main():		
	m=My8112()
	m.link()		 
	#m.newDA(0,0)
	print m.getchanelVolt(2)
	m.unlink()
def testByte():
	m=My8112()
	m.link()
	m.openVLV(vlvs["开关炉"])
	m.openVLV(vlvs["加样"])
	m.closeAll()
	m.unlink()
	# for i in range(8):
		# print i
		# m.openVLV(i)
		# m.printByte()
		# m.closeVLV(i)
		# m.printByte()
	# pass
if __name__=="__main__":
	#main()
	testByte()