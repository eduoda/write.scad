#!/usr/bin/python
chars=range(33,126+1)+[128]+range(130,140+1)+[142]+range(145,156+1)+range(158,159+1)+range(161,172+1)+range(174,255+1)

print 'function atoi(a)='
for n in chars:
  if chr(n)=="\"" or chr(n)=="\\":
    c="\\"+chr(n)
  else:
    c=chr(n)
  print '(a=="'+c+'")?'+str(n)+":"
print '0;'