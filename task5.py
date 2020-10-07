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

    freqChecker = {}                                                # CREATES DICT FOR FREQUENCY OF SECCS

    for i in range(len(txt)-k):                                     # CREATES PATTERNS AND K-MERS
        secc = txt[i:(i+k)]

        if secc in freqChecker:
            freqChecker[secc] += 1


        else:
            freqChecker[secc] = 1                                   # IF SECC NOT IN ARRAY, PUTS IT ON IT


    sortshit = sorted(freqChecker.items(), key=lambda x:x[1], reverse=True) # LAMBDA FUNCTION FOR SORTING SECCS BY FRQ

    topValue = sortshit[0][1]                                       # VALUE OF THE MOST FREQUENT ITEM

    frequentPatterns = []                                           # CREATES LIST FOR PUTTING MOST FREQUENT WORDS

    for n in range(len(sortshit)):                                  # RETURNS ONLY THE MOST FREQUENT PATTERNS
        print(sortshit[n][1])
        if sortshit[n][1] == topValue:
            frequentPatterns.append(sortshit[n][0])
        else:
            break


def FrequentWordsIIntClumps(txt, k, ntclumps):

    freqChecker = {}                                                # CREATES DICT FOR FREQUENCY OF SECCS
    tClump = []

    for i in range(len(txt) - k):                                   # CREATES PATTERNS AND K-MERS
        secc = txt[i:(i + k)]

        if secc in freqChecker:
            freqChecker[secc] += 1

            if freqChecker[secc] == ntclumps:                       # IF FREQUENCY REACHES N, GOES INTO LIST
                tClump.append(secc)
            elif freqChecker[secc] > ntclumps:                      # IF FREQUENCY EXCEDS N, SECC IS REMOVED
                tClump.remove(secc)

        else:
            freqChecker[secc] = 1                                   # IF SECC NOT IN ARRAY, PUTS IT ON IT

    print(tClump)
    return tClump

def clump(genome, nkmers, lwindow, ntclump):

    clumps = []                                                 # CREATES EMPTY LIST FOR CLUMPS
    cont = 0                                                    # COUNTS NUMBER OF WINDOWS
    soma = 0                                                    # TRACKS THE SUM OF WINDOWS

    while soma < len(genome):
        if (len(genome) - lwindow) >= lwindow:                  # IF NUMBER OF ITENS IS EQUALS lwindow
            soma = soma + lwindow
            secc = genome[(lwindow*cont):soma]                  # SETS WINDOW ON SECC

            clumps.append(genome[(lwindow*cont):soma])
            cont += 1

        else:                                                   # ELSE TEXT ENDS

            clumps.append(genome[(soma-len(genome)):])
            secc = genome[(soma - len(genome)):]                # SETS WINDOW ON SECC
            soma = soma + lwindow

        clumps.append(FrequentWordsIIntClumps(secc, nkmers, ntclump))

def main():

    # genome = 'CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA'
    # nkmers = 5
    # lwindow = 50
    # ntclump = 4

    fl = open("testTask5.txt", "r")
    lst = fl.read().split()

    genome = lst[0]
    nkmers = int(lst[1])
    lwindow = int(lst[2])
    ntclump = int(lst[3])


    # clumps = clump(genome, nkmers, lwindow, ntclump)
    #
    # for c in clumps:
    #     print(c, end=" ")

main()