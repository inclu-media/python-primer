'''
This import enable Python 3 division:
int / int = float
The '//' operator still calculates int / int = int
'''
from __future__ import division

operators = ["+","-","*","/"]

op1 = raw_input("Operand 1: ")
op2 = raw_input("Operand 2: ")
operator = raw_input("+|-|*|/: ")

if operator not in operators:
    print("Not supported operator %s" % operator)
else:
    res_string = op1 + " " + operator + " " + op2
    res = eval(res_string)
    print(res_string + " = " + str(res))

