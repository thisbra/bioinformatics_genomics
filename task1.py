import math

def Text(txt, patt, i):

    secc = txt[i:(i+len(patt))]

    return secc

def PatternCount(txt, patt):
    count = 0
    print("PATTERN: " + patt)
    index = []

    for i in range(len(txt) - (len(patt)-1)):

        secc = Text(txt, patt, i)
        if secc == patt:
            count += 1
            index.append(math.floor((i * 100) / len(txt)))

    volta = [count, index]
    return volta

def main():
    fl = open("vibrio_colerae.txt.txt")         # GENOME OF YOUR CHOICE
    txt = fl.readline()

    patt = "CGATCGAC"     # INSERT GENE

    mapa = "/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_"

    volta = PatternCount(txt, patt)

    count = volta[0]
    index = volta[1]

    for i in index:
        mapa = mapa[:i] + '*' + mapa[i:]

    print(mapa)

    print(str(count) + " INCIDENCIAS")

main()
