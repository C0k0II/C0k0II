from graph import *

windowSize(600,600)
brushColor(72,67,222)
rectangle(0,0,400,87)

brushColor(38, 214, 15)
rectangle(0,87,400,550)

brushColor(117,71,1)
rectangle(0,87,400,300)
x=0
y=87
while x<=374:
    moveTo(x,87)
    if y >87 :
        y=87;
    else:
        y=300;
    lineTo(x,y)
    x+=25

run()
