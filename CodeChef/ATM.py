#!/usr/bin/python
#ATM

input = raw_input()
x = int(input[0:input.find(' ')])
y = float(input[input.find(' ')+1:])
if (x%5 != 0) or (x >= y-.5):
  print y
else:
  print format(y - x - .5, '.2f') 
