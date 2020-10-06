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

        FrequentWords(secc, nkmers)



def main():

    genome = 'CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA'
    nkmers = 5
    lwindow = 50
    ntclump = 4

    clumps = clump(genome, nkmers, lwindow, ntclump)

    for g in clumps:
        print(FrequentWords(g, 5))

main()