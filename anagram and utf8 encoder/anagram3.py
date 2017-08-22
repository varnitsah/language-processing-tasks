#Varnit Sah 9083888794
#vsah@usc.edu

from sys import argv
str = argv[1]
list1= []

def permute(rstr, prefix):
    n = len(rstr)
    if (n == 0):
        list1.append(prefix)
    else:
        i=0
        while i < n :
            permute(rstr[0:i] + rstr[i+1:n], prefix + rstr[i])
            i =i + 1

target="anagram_"+str+".txt"

permute(str,"")
list1.sort()
file=open("anagram_out.txt","w")
for elem in list1:
    file.write(elem)
    file.write("\n")
