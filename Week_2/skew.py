def skew(dna):

    skew = 0
    minskew = 0
    minpos = []

    for nc in range(len(dna)):
        if dna[nc] == 'G':
            skew += 1
        elif dna[nc] == 'C':
            skew -= 1

        if skew < minskew:
            minpos.clear()
            minpos.append((nc+1))
            minskew = skew
        elif skew == minskew:
            minpos.append((nc+1))

    return minpos

def main():

    fl = open("dataset_7_6.txt", 'r')
    what = fl.read()

    asw = skew(what)

    for p in asw:
        print(p, end=" ")

main()