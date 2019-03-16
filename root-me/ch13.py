#!/bin/python


f = open("ch13.txt", "r")

sec = []
secRst = -1
secStr = ""
cvtStr = ""
rstStr = ""

while True:
        aLine = f.readline()
        if aLine == "":
                break;
        sec.append(int(aLine.split(" ")[3].split(":")[-1]))

for i in range(0,len(sec)):
        if i == len(sec)-1:
                break
        secRst = sec[i+1]-sec[i]
        if secRst < 0:
                secRst+=60
        if (i%4 == 0):
                secStr = secStr + "\n"
        secStr = secStr + str(secRst)

secStr = secStr.split("\n")

for k in range(1, len(secStr)):
        for i in range(0,3):
                if secStr[k][i] == "0":
                        cvtStr = cvtStr + "00"
                elif secStr[k][i] == "2":
                        cvtStr = cvtStr + "01"
                elif secStr[k][i] == "4":
                        cvtStr = cvtStr + "10"
                elif secStr[k][i] == "6":
                        cvtStr = cvtStr + "11"
        if k != len(secStr)-1:
                if secStr[k][3] == "2":
                        cvtStr = cvtStr + "0"
                elif secStr[k][3] == "4":
                        cvtStr = cvtStr + "1"
                cvtStr = cvtStr + "\n"

cvtStr = cvtStr.split("\n")
for i in range(0, len(cvtStr)):
        rstStr = rstStr + chr(int(cvtStr[i],2))

print rstStr
f.close()
