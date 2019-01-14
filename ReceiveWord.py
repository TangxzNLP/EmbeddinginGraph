# FileName  :ReceiveWord.py
# Created at:2019/1/14  10:32 @Hust
# Autor     :Daniel Tang
import io
import csv
import numpy as np
import os
import sys
import subprocess
from subprocess import PIPE
import time
import re
getpathmainlink="/home/txz/txz/labor/Code/TripleBit/GetPath/"
makelink="/home/txz/txz/labor/Code/TripleBit/"
hlink="/home/txz/txz/labor/Code/TripleBit/bin/lrelease"
wordaddress="/home/txz/txz/labor/Code/"
wordlink="/home/txz/txz/labor/Code/tang.txt"
basiccodestr="string firstStr = \"http://dbpedia.org/resource/"
# Just for example: executegetpath(homelink,"./getPath")
def executegetpath(homelink, commandexe ):
    originpath = subprocess.check_output('pwd',shell = True)
    os.chdir(homelink)
    p = subprocess.Popen(commandexe, shell=True)
    # Status;Started process id;Group process id:p.poll();p.pid;os.getpgid(p.pid)
    time.sleep(5)
    p.kill()
    os.chdir(originpath.strip('\n'))
# modify something-->string of filename in rows_th in filelink
def modifyfile( filelink , filename , rows , string):
    datalink=filelink+filename
    f=open(datalink.strip('\n'),'r+')
    line = f.readlines()
    line[rows] = string+'\n'
    f = open(filelink+filename,'w+')
    f.writelines(line)
    f.close()
# show line number of string in file of link
def showlinenum(filelink , filename , string):
    link = filelink+filename
    with io.open(link, "r", encoding='utf-8') as f:
        num = 0
        for line in f:
            # If the word reply occurs in this line ,print the line
            if line.find(string) == -1:
                num = num + 1
            else:
                break
        return num
def storedatatofile( filelink , filename , num):
    datalink = filelink+filename
    with io.open(datalink) as fh:
        linenum=0
        for line in fh:
            if(linenum<num):
                linenum=linenum+1
            else:
                print(line)
                break
strToReplace="string firstStr"
modifystr="Sex"
finalcodestr=basiccodestr+modifystr+"\""+";"
modifyfile(getpathmainlink , "main.cpp" , showlinenum(getpathmainlink , "main.cpp" , strToReplace) , finalcodestr)
executegetpath(makelink,"make")
executegetpath(hlink,"./getPath")
# wordfile=open(wordlink)
# print(len(wordfile.readlines()))
# wordfile.close()
# modifyfile(wordaddress , "tang.txt" , 2 , "justfor test")