import time

def FrequentWordsWtMismatch(txt, k, d):

    for i in range(len(txt) - k+1):
        secc = txt[i:i+k]
        permutations = Permutations(secc, d)


def Permutations(secc, d):
    permutations = []

    for l in secc:
        if l == 'A':



def main():
    start = time.time()

    txt = 'AAGAG'
    k = 3
    d = 1

    FrequentWordsWtMismatch(txt, k, d)

    stop = time.time()
    print(stop-start)
main()