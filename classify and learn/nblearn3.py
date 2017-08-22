from sys import argv
import os
import re

path=argv[1]
list=[]
nt=[]
nd=[]
pt=[]
pd=[]

negative_truthful={}
negative_deceptive={}
positive_truthful={}
positive_deceptive={}

for root, dirs, files in os.walk(path, topdown=False):
    for name in files:
        p=os.path.join(root,name)
        if p.endswith('.txt'):
            list.append(p)

ndc=0
ntc=0
pdc=0
ptc=0
for i in list:
    if "README.TXT" in i:
        continue
    if "negative" in i:
        if "deceptive" in i:
            ndc+=1
            nd.append(i)
        if "truthful" in i:
            nt.append(i)
            ntc+=1
    if "positive" in i:
        if "deceptive" in i:
            pd.append(i)
            pdc+=1
        if "truthful" in i:
            pt.append(i)
            ptc+=1

#Negative_Deceptive
for iter in nd:
    fin = open(iter,"r")
    words=fin.read()
    words=re.sub(r'\W+', ' ', words)
    words = ''.join(i for i in words if not i.isdigit())
    words=words.lower().split()
    for i in words:
        if i not in negative_deceptive:
            negative_deceptive[i] = 1
        else:
            negative_deceptive[i] += 1
    fin.close()

#Negative_Truthful
for iter in nt:
    fin = open(iter,"r")
    words=fin.read()
    words=re.sub(r'\W+', ' ', words)
    words = ''.join(i for i in words if not i.isdigit())
    words=words.lower().split()
    for i in words:
        if i not in negative_truthful:
            negative_truthful[i] = 1
        else:
            negative_truthful[i] += 1
    fin.close()

#Positive_Deceptive
for iter in pd:
    fin = open(iter,"r")
    words=fin.read()
    words=re.sub(r'\W+', ' ', words)
    words = ''.join(i for i in words if not i.isdigit())
    words=words.lower().split()
    for i in words:
        if i not in positive_deceptive:
            positive_deceptive[i] = 1
        else:
            positive_deceptive[i] += 1
    fin.close()

#Positive_Truthful
for iter in pt:
    fin = open(iter,"r")
    words=fin.read()
    words=re.sub(r'\W+', ' ', words)
    words = ''.join(i for i in words if not i.isdigit())
    words=words.lower().split()
    for i in words:
        if i not in positive_truthful:
            positive_truthful[i] = 1
        else:
            positive_truthful[i] += 1
    fin.close()

fout=open("nbmodel.txt","w")

fout.write("<Negative_Deceptive> " + str(ndc) + "\n")
for i in negative_deceptive:
    fout.write(i + " " + str(negative_deceptive[i]) + "\n")

fout.write("<Negative_Truthful> " + str(ntc) + "\n")
for i in negative_truthful:
    fout.write(i + " " + str(negative_truthful[i]) + "\n")
fout.write("<Positive_Deceptive> " + str(pdc) + "\n")

for i in positive_deceptive:
    fout.write(i + " " + str(positive_deceptive[i]) + "\n")

fout.write("<Positive_Truthful> " + str(ptc) + "\n")
for i in positive_truthful:
    fout.write(i + " " + str(positive_truthful[i]) + "\n")