import operator as op
import math as mat
from fractions import *
CONSTS = {"pi":mat.pi,
          "e":mat.e}

BINOPS = {"+":op.add,
          "-":op.sub,
          "*":op.mul,
          "^":op.pow,
          "/":op.div}

UNOPS = {"!":mat.factorial,
         "sin":mat.sin,
         "cos":mat.cos,
         "tan":mat.tan,
         "acos":mat.acos,
         "asin":mat.asin,
         "atan":mat.atan,
         "abs":mat.fabs,
         "deg":mat.degrees,
         "rad":mat.radians,
         "sqrt":mat.sqrt,
         "#":lambda x: -x,
         "%":lambda x: x / 100.0
} 
         
         
def isBinOp(num):
  return num in list(BINOPS.keys())

def isUnOp(num):
  return num in list(UNOPS.keys())

def isConst(num):
  return num in list(CONSTS.keys())

def isFloat(num):
  try:
    float(num)
    return True
  except:
    return False

def rpn_eval(string):
  stack = []
  tokens = string.split(" ")
  for token in tokens:
    if isFloat(token):
      stack.append(token)
    elif isConst(token):
      stack.append(float(CONSTS[token]))
    elif isUnOp(token):
      stack.append(UNOPS[token](float(stack.pop())))
    elif isBinOp(token):
      a = float(stack.pop())
      b = float(stack.pop())
      stack.append(BINOPS[token](b,a))
      
  if tokens[len(tokens)-1] == "frac":
    frac = Fraction(stack[0]).limit_denominator(1000)
    numer,denom = frac.numerator, frac.denominator
    print "%d/%d" %(numer,denom)
  return stack[0]
  
string = "---"  
while string not in ["", "quit"]:
  string = raw_input(">> ")
  if string not in ["", "quit"]:
	  answer = rpn_eval(string)
	  CONSTS["ans"] = answer
	  print answer
