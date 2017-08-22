import sys
import codecs
import collections
import time
import operator


def main():
    pTagDict = collections.defaultdict(list)
    dictW = collections.defaultdict(list)
    tagPr = {}

    with open("hmmmodel.txt", "r") as hmm:
        flag = 0
        for line in hmm:
            if flag == 0:
                if line[0] == '\n':
                    flag = 1
                    continue
                a = line.split(" ")
                tagPr[a[0]] = float(a[1].rstrip("\n").rstrip(" "))
            if flag == 1:
                if line[0] == '\n':
                    flag = 2
                    continue
                a = line.rstrip("\n").rstrip(" ").split(" ")
                pTagDict[a[0]] = a[1:]
            if flag == 2:
                a = line.rstrip("\n").rstrip(" ").split(" ")
                dictW[a[0]] = a[1:]

    mp = max(tagPr.values())
    mpt = " "
    previoustag = "START"
    out = open("hmmoutput.txt", "w")
    with codecs.open(sys.argv[1], 'r', encoding='utf8') as f:
        for line in f:
            words = line.rstrip("\n").split(" ")
            string = " "
            for word in words:
                maxPr = 0
                predTag = " "
                product = 0
                if word not in dictW:
                    l1 = pTagDict[previoustag]
                    temp = {}
                    for i in l1:
                        pos = i.rfind('/')
                        tagN = i[0:pos]
                        proV = float(i[pos + 1:].rstrip(" "))
                        temp[tagN] = proV
                    predTag = max(temp.items(), key=operator.itemgetter(1))[0]
                    maxPr = temp[predTag]
                    previoustag =predTag
                else:
                    for tag in dictW[word]:
                        l1 = pTagDict[previoustag]
                        for i in l1:
                            pos = tag.rfind("/")
                            tN = tag[0:pos]
                            pV = float(tag[pos + 1:])
                        product = pV * tagPr[tN]
                        if product > maxPr:
                            maxPr = product
                            predTag = tN
                string = string + word.rstrip("\n") + "/" + predTag + " "
            string = string.rstrip(" ").lstrip(" ") + "\n"
            out.write(string)


start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))
