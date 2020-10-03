def findpi(dna):

    rev = ""

    for n in dna:

        if n == "A":
            rev = rev + "T"
        elif n == "T":
            rev = rev + "A"

        if n == "G":
            rev = rev + "C"
        elif n == "C":
            rev = rev + "G"

    rev = rev[::-1]

    return rev

def main():

    fl = open("dataset_3_2.txt")                         # INSERT GENE TO FIND ITS...
    dna = fl.read()                                      # COMPLEMENTARY STRAND

    rev = findpi(dna).strip()
    esc = open("resposta.txt","w")
    esc.write(rev)

    esc.close()
    fl.close()
main()