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

    for i in range(len(txt)-k):
        secc = txt[i:(i+k)]

        if secc in freqChecker:
            freqChecker[secc] += 1
        else:
            freqChecker[secc] = 1

    print(sorted(freqChecker.items(), key=lambda kv:kv[1]))

def main():

    fl = open("dataset_2_10.txt", "r")
    txt = open("dataset_3_2.txt", "r").readline()
    k = 6

    FrequentWordsII(txt, k)

    for i in flst:
        print(i + " ")

main()