# Author: wangfang

col = 1
while col <= 9:
    line = 1
    while col >= line:
        print("%d*%d=%d\t" %(line,col,line*col),end="" )
        line += 1
    print("")
    col += 1


