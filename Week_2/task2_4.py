def hammingD(strP, strD, d):

    hdist = 0

    for nc in range(len(strP)):
        if strP[nc] != strD[nc]:
            hdist += 1
        if hdist > d:
            break

    return hdist

def ApproximatePatternCount(txt, patt, d):
    count = 0

    for i in range(len(txt) - len(patt)+1):
        secc = txt[i:i+len(patt)]
        if hammingD(patt, secc, d) <= d:
            count += 1

    return count

def main():

    patt = 'TTTCTAG'
    txt = 'AGCAGCCTGTTCGGCCGCACCGAGCCGGACAGTAATAACGAAATAGTCAGTTTTATCGGCCTTTTGTGTTATTTTACTTGTGTGGTTGTTGGTTGCCAGCAGGCCATTCCACGGTGGTCGCTTTGAAAAGAATCCCAAGGAACCGGCAAGCTCCCTTGTTAGCCCATACGGAAAAAAGTAGGGGTGGGTATACTTGGTTAGAATTCGAACTGTGTCCCACTAAGGGGACGTCACGCCGAATCATTTTCTAGCGGTCCGAGCTCGTGATTTCAGACGCTTCGCTAAAAGTGGGCTGGATGACGTATGATTGTACGGACAATATCAACATGGCTC'
    d = 3

    count = ApproximatePatternCount(txt, patt, d)

    print(count)

main()