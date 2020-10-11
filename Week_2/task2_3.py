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

    for n in range(len(dna)-len(patt)):
        strD = dna[n:(n+len(patt))]

        if d >= hammingD(strD, patt, d):
            pos.append(n)

    return pos

def main():

    # patt = 'ATTCTGGA'
    # dna = 'CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT'
    # d = 3

    fl = open('dataset_t3.txt', 'r')
    lst = fl.readlines()

    patt = lst[1]
    dna = lst[2]
    d = int(lst[3])

    positions = checkPatt(patt, dna, d)

    print(*positions)

main()