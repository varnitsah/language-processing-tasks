from sys import argv
from math import log10
import os
import re
path=argv[1]

list=[]
negative = {}
positive = {}
deceptive = {}
truthful = {}

for root, dirs, files in os.walk(path, topdown=False):
    for name in files:
        p=os.path.join(root,name)
        if p.endswith('.txt'):
            list.append(p)

with open("nbmodel.txt", "r") as ins:
        i=0
        #1 for Neg_dec, 2 for Neg_tru, 3 for Pos_dec, 4 for Pos_tru
        for line in ins:
            if line[0] == '<':
                i=i+1
                words=line.split()
                continue
            else:
                if i==1:
                    words=line.split()
                    negative[words[0]] = int(words[1])
                    continue
                if i==2:
                    words=line.split()
                    positive[words[0]] = int(words[1])
                    continue
                if i==3:
                    words=line.split()
                    deceptive[words[0]] = int(words[1])
                    continue
                if i==4:
                    words=line.split()
                    truthful[words[0]] = int(words[1])
                    continue

def classify(filename):
    tfile = open(filename,"r")
    words=tfile.read()
    freq={}
    words=re.sub(r'\W+', ' ', words)
    words = ''.join(i for i in words if not i.isdigit())
    words=words.lower().split()
    for i in words:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1
    neg_sum = 0
    pos_sum = 0
    dec_sum = 0
    tru_sum = 0
    arg_n = 0
    arg_p = 0
    arg_d = 0
    arg_t = 0
    for i in freq:
        if i not in negative:
            a=0
        else:
            a=negative[i]
        nd_p_t_c = (a + 1) / ( sum( negative.values() ) + len(vocab) )
        neg_sum += log10(nd_p_t_c)

        if i not in positive:
            b=0
        else:
            b=positive[i]
        nt_p_t_c = (b + 1) / ( sum( positive.values() ) + len(vocab) )
        pos_sum += log10(nt_p_t_c)

        if i not in deceptive:
            c=0
        else:
            c=deceptive[i]
        pd_p_t_c = (c + 1) / ( sum( deceptive.values() ) + len(vocab) )
        dec_sum += log10(pd_p_t_c)

        if i not in truthful:
            d=0
        else:
            d=truthful[i]
        pt_p_t_c = (d + 1) / ( sum( truthful.values() ) + len(vocab) )
        tru_sum += log10(pt_p_t_c)
    arg_n= 0.5 + neg_sum
    arg_p= 0.5 + pos_sum
    arg_d= 0.5 + dec_sum
    arg_t= 0.5 + tru_sum

    argmax_pn = max(arg_n,arg_p)
    argmax_dt = max(arg_d,arg_t)

    if argmax_dt == arg_d:
        fileout.write("deceptive ")
    if argmax_dt == arg_t:
        fileout.write("truthful ")

    if argmax_pn == arg_n:
        fileout.write("negative " + filename+ "\n")
    if argmax_pn == arg_p:
        fileout.write("positive " + filename+"\n")

fileout =open("nboutput.txt","w")
vocab=negative.copy()
vocab.update(positive)
vocab.update(deceptive)
vocab.update(truthful)
for testfile in list:
    classify(testfile)
fileout.close()
