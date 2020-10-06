def clump(genome, nkmers, lwindow, ntclump):

    clumps = []
    cont = 0
    soma = 0

    while soma < len(genome):
        if (len(genome) - lwindow) >= lwindow:
            soma = soma + lwindow
            secc = genome[(lwindow*cont):soma]

            clumps.append(genome[(lwindow*cont):soma])
            cont += 1
        else:

            clumps.append(genome[(soma-len(genome)):])
            secc = genome[(soma - len(genome)):]
            soma = soma + lwindow


    return clumps

def main():

    genome = "CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA"
    nkmers = 5
    lwindow = 70
    ntclump = 4

    print(clump(genome, nkmers, lwindow, ntclump))

main()