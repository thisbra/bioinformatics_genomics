def findPattern(patt ,gnm):

    positions = []

    for i in range(len(gnm) - len(patt)):
        if patt == gnm[i:(i+len(patt))]:
            positions.append(i)

    return positions

def main():

    fl = open("dataset_3_5.txt", "r")

    patt = fl.readline().strip()
    gnm = fl.readline()

    positions = findPattern(patt, gnm)

    esc = open("resposta.txt", "w")

    for n in positions:
        esc.write(str(n) + " ")

    esc.close()
    fl.close()

main()