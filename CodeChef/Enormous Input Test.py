#!/usr/bin/python
#Enormous Input Test

#this method is too slow

first = raw_input()
n = int(first[0:first.find(' ')])
k = int(first[first.find(' ') + 1:])
count = 0
current = 0
while current<n:
  input = raw_input()
  if str(input) == '':
    break
  t = int(input)
  if t%k == 0:
    count = count + 1
  current = current + 1
print count


#a second try

