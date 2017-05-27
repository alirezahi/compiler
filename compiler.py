from check import *

dir = open('test.txt','r')
commabool,commaRes,commaToken = commaCheck(dir)
if commabool:
    print('yay')
else:
    if commaRes == '0':
        print('Error : Comma hasn\'t been closed somewhere')
    else:
        print('Error : Comma Not Expected in line '+commaRes+' after '+commaToken)