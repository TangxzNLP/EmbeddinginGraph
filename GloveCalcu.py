import io
import csv
import numpy as np
import re
import time

csv_reader = csv.reader(open("/home/txz/txz/labor/Code/set1.csv"))
numcsv = np.array(list(csv_reader)).shape[0] - 1


###Created by DanielTang @2019.01.07
###class fo calcu sim of two word
###input parameter of two words to be processed by task wordsim353 

###calcu similarity of two vector
def cos_sim(vector_a, vector_b):
    vector_a = np.mat(vector_a)
    vector_b = np.mat(vector_b)
    num = float(vector_a * vector_b.T)
    denom = np.linalg.norm(vector_a) * np.linalg.norm(vector_b)
    cos = num / denom
    sim = (0.5 + 0.5 * cos) * 10.0
    return sim


###find string in someone txt and show the line number of this string in txt
def ShowLineNum(link, str):
    with io.open(link, "r", encoding='utf-8') as f:
        # clear the file the txt related to fh-->output.txt
        # fh.truncate();
        num = 0
        for line in f:
            # If the word reply occurs in this line ,print the line
            if line.find(str.lower()+'\n') == -1 or (len(str) + 1) != len(line):
                num = num + 1
            else:
                break
        return num


###Store the Num th line of file datalink to file filelink
def StoreDataToFile(datalink, filelink, num1):
    with io.open(datalink) as fh:
        with io.open(filelink, "w", encoding='utf-8') as SearchResult:
            linenum1 = 0
            SearchResult.truncate();
            for line in fh:
                if (linenum1 < num1):
                    linenum1 = linenum1 + 1
                else:
                    SearchResult.write(line)
                    break


###Main function
numS1 = 0
numS2 = 0
datalinkString = "/home/txz/txz/labor/Code/SCBGO_py/GloveString.txt"
datalinkNum = "/home/txz/txz/labor/Code/GloveNum.txt"
datalinkStore = "/home/txz/txz/labor/Code/SCBGO_py/SearchResult.txt"
###get str1,str2 from wordsim.txt
f = open(r"/home/txz/txz/labor/Code/SCBGO_py/wordsim.txt")
line = f.readline()
data_liststr = []
while line:
    str1 = list(map(str, line.split()))
    data_liststr.append(str1)
    line = f.readline()
f.close()

fresult=open("/home/txz/txz/labor/Code/SCBGO_py/wordsimresult.txt", "w")
vector1=[0 for i in range(numcsv)]
vector2=[0 for i in range(numcsv)]
for i in range(numcsv):
    str1 = data_liststr[i][0]
    str2 = data_liststr[i][1]
    print str1,str2
    numS1 = ShowLineNum(datalinkString, str1)
    numS2 = ShowLineNum(datalinkString, str2)
    print numS1, numS2
    StoreDataToFile(datalinkNum, datalinkStore, numS1)
    ####Read file SearchResultline list to array
    f1 = open(r"/home/txz/txz/labor/Code/SCBGO_py/SearchResult.txt")
    line1 = f1.readline()
    data_list1 = []
    while line1:
        num1 = list(map(float,line1.split()))
        data_list1.append(num1)
        line1 = f1.readline()
    f1.close()
    data_array1 = np.array(data_list1)
    print data_array1


    StoreDataToFile(datalinkNum, datalinkStore, numS2)
    f2 = open(r"/home/txz/txz/labor/Code/SCBGO_py/SearchResult.txt")
    line2 = f2.readline()
    data_list2 = []
    while line2:
        num1 = list(map(float,line2.split()))
        data_list2.append(num1)
        line2 = f2.readline()
    f2.close()
    data_array2 = np.array(data_list2)
    print data_array2 
    vector1[i]=data_array1
    vector2[i]=data_array2
    print vector1[i]
    print vector2[i]
    sim=cos_sim(vector1[i],vector2[i])
    fresult.write(str(sim)+'\n')
    print sim  	
fresult.close()
