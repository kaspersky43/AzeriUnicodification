# -*- coding: utf-8 -*-
import csv, re, time, sys, codecs
from collections import Counter

delimiter = ','

def words(text): return re.findall(r'\S+', text)

def convert_to_ascii(text): #unicode to ascii
    ltc = 'çəğıöşüÇƏĞİÖŞÜ'
    ltf = 'cegiosuCEGIOSU'
    ltc = ltc.decode('utf-8-sig')
    text = text.decode('utf-8-sig')
    for t in text:
        i = 0
        for c in ltc:
            if(t == c):
                o = text.find(t)
                t = ltf[i]
                text = text[:o] + t + text[o+1:]
            i += 1
    return text


f = open('azj-train.txt','r+').read()
f2 = open('dictionary.txt','wb')

i = 0
for word in words(f):
    word2 = convert_to_ascii(word)
    f2.write(word)
    word = word.decode('utf-8-sig')
    f2.write(delimiter)
    print i
    word2 = word2.encode('utf-8-sig')
    f2.write(word2)
    f2.write("\n")
    i += 1
f2.close()
