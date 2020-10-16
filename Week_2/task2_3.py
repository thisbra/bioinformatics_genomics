def hammingD(strP, strD, d):

    hdist = 0

    for nc in range(len(strP)):
        if strP[nc] != strD[nc]:
            hdist += 1
        if hdist > d:
            break

    return hdist

def checkPatt(patt, dna, d):

    pos = []

    for n in range(len(dna)-len(patt)+1):
        strd = dna[n:(n+len(patt))]

        if d >= hammingD(strd, patt, d):
            pos.append(n)

    return pos

def main():

    patt = 'AA'
    dna = 'TACGCATTACAAAGCACA'
    d = 1

    # fl = open('dataset_9_4.txt', 'r')
    #
    # patt = fl.readline().strip('\n')
    # dna = fl.readline()
    # d = int(fl.readline())

    positions = checkPatt(patt, dna, d)

    print(*positions)


main()