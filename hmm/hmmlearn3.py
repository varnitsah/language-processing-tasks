import sys
import codecs
import time
import collections


def main():
    dictW = collections.defaultdict(list)
    pTagDict = collections.defaultdict(list)
    tagDict = {}
    with codecs.open(sys.argv[1], 'r', encoding='utf8') as f:
        for line in f:
            wordTagDuo = line.split(" ")
            previoustag = "START"

            for i in wordTagDuo:
                pos = i.rfind('/')
                text = i[0:pos]
                tag = i[pos + 1:].strip('\n')
                if tag in tagDict:
                    tagDict[tag] += 1
                else:
                    tagDict[tag] = 1
                dictW[text].append(tag)

                if previoustag == "START":
                    pTagDict[previoustag].append(tag)
                    previoustag = tag
                    continue
                pTagDict[previoustag].append(tag)
                previoustag = tag

    # dictW has words as keys and the values as a list of tags
    # tagDict has keys=tags and values= list of words
    # prevTags has keys = words and values = previoustags_prob(tag|prevtag)
    out = open("hmmmodel.txt", "w")
    tagDict["UNK"] = 1
    N1 = sum(tagDict.values())
    D1 = len(tagDict)
    for i in tagDict:
        tagDict[i] = (tagDict[i] + 1) / (N1 + D1)
        out.write(i + " " + str(tagDict[i]) + "\n")
    out.write("\n")

    for i in pTagDict:
        counter = collections.Counter(pTagDict[i])
        N = sum(counter.values())
        out.write(i + " ")
        for elem in counter:
            counter[elem] = counter[elem] / N
            out.write(elem + "/" + str(counter[elem]) + " ")
        out.write("\n")
    out.write("\n")

    for i in dictW:
        counter = collections.Counter(dictW[i])
        N = sum(counter.values())
        out.write(i + " ")
        for elem in counter:
            counter[elem] = counter[elem] / N
            out.write(elem + "/" + str(counter[elem]) + " ")
        out.write("\n")

# CALL TO MAIN
start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))
