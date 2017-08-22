from sys import argv
from math import log10
import os
import re
path=argv[1]



list=[]

neg_dec = {}
neg_tru = {}
pos_dec = {}
pos_tru = {}
lc=[]

def readModel(model):
    with open("nbmodel.txt", "r") as ins:
        i=0
        #1 for Neg_dec, 2 for Neg_tru, 3 for Pos_dec, 4 for Pos_tru
        for line in ins:
            if line[0] == '<':
                i=i+1
                words=line.split()
                lc.append(int(words[1]))
                continue
            else:
                if i==1:
                    words=line.split()
                    if len(words[0])<4 or int(words[1])>100:
                        continue
                    neg_dec[words[0]] = int(words[1])
                    continue
                if i==2:
                    words=line.split()
                    if len(words[0])<4 or int(words[1])>100:
                        continue
                    neg_tru[words[0]] = int(words[1])
                    continue
                if i==3:
                    words=line.split()
                    if len(words[0])<4 or int(words[1])>100:
                        continue
                    pos_dec[words[0]] = int(words[1])
                    continue
                if i==4:
                    words=line.split()
                    if len(words[0])<4 or int(words[1])>100:
                        continue
                    pos_tru[words[0]] = int(words[1])
                    continue


for root, dirs, files in os.walk(path, topdown=False):
    for name in files:
        p=os.path.join(root,name)
        if p.endswith('.txt'):
            list.append(p)

# print(neg_dec)
# print(neg_tru)
# print(pos_dec)
# print(pos_tru)

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
    nd_sum=0
    nt_sum=0
    pd_sum=0
    pt_sum=0
    arg0=0
    arg1=0
    arg2=0
    arg3=0
    for i in freq:
        if i not in neg_dec:
            a=0
        else:
            a=neg_dec[i]
        nd_p_t_c = (a + 1) / ( sum( neg_dec.values() ) + len(vocab) )
        nd_sum += log10(nd_p_t_c)

        if i not in neg_tru:
            b=0
        else:
            b=neg_tru[i]
        nt_p_t_c = (b + 1) / ( sum( neg_tru.values() ) + len(vocab) )
        nt_sum += log10(nt_p_t_c)

        if i not in pos_dec:
            c=0
        else:
            c=pos_dec[i]
        pd_p_t_c = (c + 1) / ( sum( pos_dec.values() ) + len(vocab) )
        pd_sum += log10(pd_p_t_c)

        if i not in pos_tru:
            d=0
        else:
            d=pos_tru[i]
        pt_p_t_c = (d + 1) / ( sum( pos_tru.values() ) + len(vocab) )
        pt_sum += log10(pt_p_t_c)
    arg0= log10(lc[0]/(lc[0]+lc[1]+lc[2]+lc[3])) + nd_sum
    arg1= log10(lc[1]/(lc[0]+lc[1]+lc[2]+lc[3])) + nt_sum
    arg2= log10(lc[2]/(lc[0]+lc[1]+lc[2]+lc[3])) + pd_sum
    arg3= log10(lc[3]/(lc[0]+lc[1]+lc[2]+lc[3])) + pt_sum
    argmax=max(arg0,arg1,arg2,arg3)

    if argmax==arg0:
        fileout.write("deceptive negative " + filename+ "\n")
    if argmax==arg1:
        fileout.write("truthful negative " + filename+"\n")
    if argmax==arg2:
        fileout.write("deceptive positive " + filename+"\n")
    if argmax==arg3:
        fileout.write("truthful positive " + filename+"\n")

readModel("nbmodel.txt")
fileout =open("nboutput.txt","w")
vocab=neg_dec.copy()
vocab.update(neg_tru)
vocab.update(pos_dec)
vocab.update(pos_tru)
for testfile in list:
    classify(testfile)
fileout.close()
# classify(list[0])
# print(len(neg_dec))
# print(len(neg_tru))
# print(len(pos_dec))
# print(len(pos_tru))