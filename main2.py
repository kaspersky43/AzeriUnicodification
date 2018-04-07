# -*- coding: utf-8 -*-

import csv, re, time, sys, codecs

delimiter = ','
            
def correction(word, unidict, asciidict):
    try:
        i = asciidict.index(word)
        return unidict[i].decode('utf-8-sig')
    except:
        return word

lines = open('dictionary.txt').readlines()
with open('input-test.csv','r+') as csvinput:
    with open('output.csv','w') as csvoutput:
        reader = csvinput.readlines()
        
        unidict = []
        asciidict = []
        i = 0
        for line in lines:
            #print i
            line = line.strip().split(delimiter)
            unidict.append(line[0])
            line[1] = line[1].replace('\xef\xbb\xbf','')
            asciidict.append(line[1])
            i += 1
        
        reader[0] = reader[0].replace('\xef\xbb\xbf','').strip()
        row = reader[0]
        csvoutput.write(row[0])
        csvoutput.write(delimiter)
        csvoutput.write(row[1])
        csvoutput.write('\n')

        i2 = 0
        for row in reader[1:]:
            row = row.strip().split(delimiter)
            row[1] = row[1][1:len(row[1])-1]
            row[1] = correction(row[1].decode("utf-8-sig"),unidict,asciidict)
            row.append(row[1]) 
            row.remove(row[1])
            csvoutput.write(row[0])
            csvoutput.write(delimiter)
            csvoutput.write(row[1].encode('utf-8'))
            csvoutput.write('\n')
            print i2
            i2 += 1
