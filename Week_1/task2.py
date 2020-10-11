def Text(txt, i, k):

    secc = txt[i:(i+k)]

    return secc

def PatternCount(txt, patt):
    count = 0
    # print("PATTERN: " + patt)

    for i in range(len(txt) - (len(patt)-1)):

        secc = txt[i:(i+len(patt))]
        if secc == patt:
            count += 1


    return count

def FrequentWords(txt, k):
    frequentPatterns = []
    count = []
    for i in range(len(txt) - k):
        secc = Text(txt, i, k)
        count.append(PatternCount(txt, secc))

    maxCount = 0
    for i in count:
        if i > maxCount:
            maxCount = i


    for i in range(len(txt) - k):
        if count[i] == maxCount:
            frequentPatterns.append(Text(txt, i, k))

    frequentPatterns = list(dict.fromkeys(frequentPatterns))

    return sorted(frequentPatterns)

def FrequentWordsII(txt, k):

    freqChecker = {}
    frequentPatterns = []

    for i in range(len(txt)-k):
        secc = txt[i:(i+k)]

        if secc in freqChecker:
            freqChecker[secc] += 1

        else:
            freqChecker[secc] = 1

    sortshit = sorted(freqChecker.items(), key=lambda x:x[1], reverse=True)

    topValue = sortshit[0][1]

    for n in range(len(sortshit)):
        print(sortshit[n][1])
        if sortshit[n][1] == topValue:
            frequentPatterns.append(sortshit[n][0])
        else:
            break

    return frequentPatterns

def main():

    fl = open("dataset_2_10.txt", "r")
    txt = open("vibrio_colerae.txt.txt", "r").readline()

    print(FrequentWordsII("CGGAGGACTCTAGGTAACGCTTATCAGGTCCATAGGACATTCA", 3))


main()