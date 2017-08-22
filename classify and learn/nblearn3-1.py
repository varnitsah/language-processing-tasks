from sys import argv
import os
import re

path=argv[1]
list=[]
neg=[]
pos=[]
dec=[]
tru=[]

negative={}
positive={}
deceptive={}
truthful={}

for root, dirs, files in os.walk(path, topdown=False):
    for name in files:
        p=os.path.join(root,name)
        if p.endswith('.txt'):
            list.append(p)

pc=0
nc=0
tc=0
dc=0

for i in list:
    if "README.TXT" in i:
        continue
    if "negative" in i:
        neg.append(i)
        nc+=1
    if "positive" in i:
        pos.append(i)
        pc+=1
    if "truthful" in i:
        tru.append(i)
        tc+=1
    if "deceptive" in i:
        dec.append(i)
        dc+=1

#Negative
for iter in neg:
    fin = open(iter,"r")
    words=fin.read()
    words=re.sub(r'\W+', ' ', words)
    words = ''.join(i for i in words if not i.isdigit())
    words=words.lower().split()
    for i in words:
        if i not in negative:
            negative[i] = 1
        else:
            negative[i] += 1
    fin.close()

# Positive
for iter in pos:
    fin = open(iter,"r")
    words=fin.read()
    words=re.sub(r'\W+', ' ', words)
    words = ''.join(i for i in words if not i.isdigit())
    words=words.lower().split()
    for i in words:
        if i not in positive:
            positive[i] = 1
        else:
            positive[i] += 1
        fin.close()

for iter in tru:
    fin = open(iter,"r")
    words=fin.read()
    words=re.sub(r'\W+', ' ', words)
    words = ''.join(i for i in words if not i.isdigit())
    words=words.lower().split()
    for i in words:
        if i not in truthful:
            truthful[i] = 1
        else:
            truthful[i] += 1
    fin.close()

for iter in dec:
    fin = open(iter,"r")
    words=fin.read()
    words=re.sub(r'\W+', ' ', words)
    words = ''.join(i for i in words if not i.isdigit())
    words=words.lower().split()
    for i in words:
        if i not in deceptive:
            deceptive[i] = 1
        else:
            deceptive[i] += 1
    fin.close()


fout=open("nbmodel.txt","w")

fout.write("<Negative> " + "\n")
for i in negative:
    fout.write(i + " " + str(negative[i]) + "\n")

fout.write("<Positive> " + "\n")
for i in positive:
    fout.write(i + " " + str(positive[i]) + "\n")

fout.write("<Deceptive> " + "\n")
for i in deceptive:
    fout.write(i + " " + str(deceptive[i]) + "\n")

fout.write("<Truthful> " + "\n")
for i in truthful:
    fout.write(i + " " + str(truthful[i]) + "\n")