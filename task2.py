def Text(txt, patt, i):

    secc = txt[i:(i+len(patt))]

    return secc

def PatternCount(txt, patt):
    count = 0
    print("PATTERN: " + patt)

    for i in range(len(txt) - (len(patt)-1)):

        secc = txt[i:(i+len(patt))]
        if secc == patt:
            count += 1


    return count

def FrequentWords(txt, k):
    FrequentPatterns = []
    count = []
    for i in range(len(txt) - k):
        patt = Text(i, k)
        count[i] = PatternCount(txt, patt)

    maxCount = 0
    for i in count:
        if i > maxCount:
            maxCount = i

    for i in range(len(txt) = k):
        if count[i] == maxCount
            FrequentPatterns.append(Text())


def main():


main()