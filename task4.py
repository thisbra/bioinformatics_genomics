def findPattern(patt ,gnm):

    positions = []

    for i in range(len(gnm) - len(patt)):
        if patt == gnm[i:(i+len(patt))]:
            positions.append(i)

    return positions

def main():

    fl = open("vibrio_colerae.txt.txt", "r")

    patt = "CTTGATCAT"
    gnm = fl.read()

    positions = findPattern(patt, gnm)


    for n in positions:
        print(str(n), end=" ")

    fl.close()

main()