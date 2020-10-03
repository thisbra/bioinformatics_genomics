def amino_frq(txt):

    lstamn = {"ala": 0, "arg": 0, "asn": 0, "asp": 0, "cys": 0, "gln": 0,
              "glu": 0, "gly": 0, "his": 0, "ile": 0, "leu": 0, "lys": 0,
              "met": 0, "phe": 0, "pro": 0, "ser": 0, "thr": 0, "trp": 0,
              "tyr": 0, "val": 0, "stop": 0}

    # alanine - ala - A
    # arginine - arg - R
    # asparagine - asn - N
    # aspartic
    # acid - asp - D
    # cysteine - cys - C
    # glutamine - gln - Q
    # glutamic
    # acid - glu - E
    # glycine - gly - G
    # histidine - his - H
    # isoleucine - ile - I
    # leucine - leu - L
    # lysine - lys - K
    # methionine - met - M
    # phenylalanine - phe - F
    # proline - pro - P
    # serine - ser - S
    # threonine - thr - T
    # tryptophan - trp - W
    # tyrosine - tyr - Y
    # valine - val - V

    stopon = True

    for i in range(len(txt)-2):
        amn = txt[i:(i+3)]

        if stopon == True:
            if amn == "ATG":
                lstamn["met"] += 1
                stopon = False

        else:
            if amn == "ATG":
                lstamn["met"] += 1

            elif (amn == "TAA" or amn == "TAG" or amn == "TGA"):
                stopon = True
                lstamn["stop"] += 1

            elif (amn[0:2] == "GG"):
                lstamn["gly"] += 1

            elif (amn == "GAG" or amn == "GAA"):
                lstamn["glu"] += 1

            elif (amn == "GAC" or amn == "GAT"):
                lstamn["asp"] += 1

            elif (amn[0:2] == "GC"):
                lstamn["ala"] += 1

            elif (amn[0:2] == "GT"):
                lstamn["val"] += 1

            elif (amn == "AGG" or amn == "AGA"):
                lstamn["arg"] += 1

            elif (amn == "AGC" or amn == "AGT"):
                lstamn["ser"] += 1

            elif (amn == "AAG" or amn == "AAA"):
                lstamn["lys"] += 1

            elif (amn == "AAC" or amn == "AAT"):
                lstamn["asn"] += 1

            elif (amn[0:2] == "AC"):
                lstamn["thr"] += 1

            elif (amn == "ATA" or amn == "ATC" or amn == "ATT"):
                lstamn["ile"] += 1

            elif (amn[0:2] == "CG"):
                lstamn["arg"] += 1

            elif (amn == "CAG" or amn == "CAA"):
                lstamn["gln"] += 1

            elif (amn == "CAT" or amn == "CAU"):
                lstamn["his"] += 1

            elif (amn[0:2] == "CC"):
                lstamn["pro"] += 1

            elif (amn[0:2] == "CT"):
                lstamn["leu"] += 1

            elif (amn == "TGG"):
                lstamn["trp"] += 1

            elif (amn == "TGT" or amn == "TGC"):
                lstamn["cys"] += 1

            elif (amn == "TAT" or amn == "TAC"):
                lstamn["tyr"] += 1

            elif (amn[0:2] == "TC"):
                lstamn["ser"] += 1

            elif (amn == "TTG" or amn == "TTA"):
                lstamn["leu"] += 1

            elif (amn == "TTT" or amn == "TTC"):
                lstamn["phe"] += 1

    print(lstamn)

def main():

    fl = open("vibrio_colerae.txt.txt", "r")

    txt = fl.read()
    amino_frq(txt)

    fl.close()

main()