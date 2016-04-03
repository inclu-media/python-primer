suspects = {
    'Miha': ["TGCAGGAACTTC", "AAAACCTCA", "GCCAGTGCCG", "GGGAGGTGGC", "GCCACGG"],
    'Ziga': ["TGCAGGAACTTC", "AAAACCTCA", "TTAGCTATCGC", "AAGTAGTGAC", "ACCACAA"],
    'Matej': ["TGCAGGAACTTC", "AAAACCTCA", "CCAGCAATCGC", "TTGTGGTGGC", "AGGCCTCA"]
}

filename = "sample.txt"

sample = open(filename).read()

for suspect in suspects.keys():  # loop through the suspects
    print ("Analysing %s ..." % suspect)
    guilty = True
    for x in xrange(0, 4):  # loop through the 5 sequences for each suspect
        print("Looking for %s ..." % suspects[suspect][x])
        if sample.find(suspects[suspect][x]) == -1:
            guilty = False
            print("%s is not guilty" % suspect)
            break
    if guilty:
        print("%s is guilty! Hang him!" % suspect)
        break





