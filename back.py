import operator
class Calc:
    
    operators = {"/": operator.div, "*": operator.mul, 
            "-": operator.sub, "+": operator.add}
    
    operatorString = "/*-+="
    def clear(self):
        self.operatortext = ""
        self.topOperandtext = ""
        self.bottomOperandtext = ""
    def __init__(self):
        self.operatortext = ""
        self.topOperandtext = ""
        self.bottomOperandtext = ""
    def key(self,event):
        char = event.keyChar
        if char.isdigit():
            self.handleDigit(char)
        elif char == ".":
            self.decimalPressed(event)
        elif char in self.operatorString:
            self.handleOperator(char)
            
        elif char == "\n":
            self.clear(event)
        else:
            return
        event.consume()
    
    def handleDigit(self, digitChar):
        self.bottomOperandtext+= digitChar
        
    def decimalPressed(self):
        if not '.' in self.bottomOperandtext:
            self.bottomOperandtext += '.'
   
    def handleOperator(self, opChar):
        if self.operatortext:
            opFunc = self.operators[self.operatortext]
            topNum = float(self.topOperandtext)
            bottomNum = float(self.bottomOperandtext)
            result = opFunc(topNum, bottomNum)
            self.topOperandtext = str(result)
            self.bottomOperandtext = ""
        elif self.bottomOperandtext:
            self.topOperandtext = self.bottomOperandtext
            self.bottomOperandtext = ""
        self.displayOperator(opChar)
            
    def displayOperator(self, opChar):   
        if not self.calculationStarted(): 
            return
        if opChar == "=":
            self.operatortext = ""
        else:
            self.operatortext = opChar
            
    def calculationStarted(self):
        return self.topOperandtext or self.bottomOperandtext

                
