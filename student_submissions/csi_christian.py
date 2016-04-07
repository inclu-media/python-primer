dna = open("dna.txt").read()

hair_black = "CCAGCAATCGC"
hair_brown = "GCCAGTGCCG"
hair_carrot = "TTAGCTATCGC"

face_square = "GCCACGG"
face_round = "ACCACAA"
face_oval = "AGGCCTCA"

eye_blue = "TTGTGGTGGC"
eye_green = "GGGAGGTGGC"
eye_brown = "AAGTAGTGAC"

gender_male = "TGCAGGAACTTC"
gender_female = "TGAAGGACCTTC"

race_white = "AAAACCTCA"
race_black = "CGACTACAG"
race_asian = "CGCGGGCCG"


if dna.find(hair_black) > -1:
    print "The hair color is black"
elif dna.find(hair_brown) > -1:
    print "The hair color is brown"
elif dna.find(hair_carrot) > -1:
    print "the hair color is carrot"
else:
    print "no match found"

if dna.find(face_square) > -1:
    print "The face is square"
elif dna.find(face_oval) > -1:
    print "The face is oval"
elif dna.find(face_round) > -1:
    print "The face is round"
else:
    print "no match found"

if dna.find(eye_blue) > -1:
    print "The eye color is blue"
elif dna.find(eye_brown) > -1:
    print "The eye_color is brown"
elif dna.find(eye_green) > -1:
    print "The eye color is green"
else:
    print "no match found"

if dna.find(gender_male) > -1:
    print "The gender is male"
elif dna.find(gender_female) > -1:
    print "The gender is female"
else:
    print "no match found"

if dna.find(race_asian) > -1:
    print "The race is asian"
elif dna.find(race_black) > -1:
    print "The race is black"
elif dna.find(race_white) > -1:
    print "The race is white"
else:
    print "no match found"

'''
This only works because python interprets the integer 0 as boolean False, all other integers as True.
The clean solution would be to check each find for > -1:
... dna.find(gender_male) > -1 and dna.find(race_white) > -1 ...
'''

if dna.find(gender_male) and dna.find(race_white) and dna.find(hair_carrot) and dna.find(eye_brown) and dna.find(face_round) > -1:
    print "Ziga ate the ice cream"
elif dna.find(gender_male) and dna.find(race_white) and dna.find(hair_black) and dna.find(eye_blue) and dna.find(face_oval) > -1:
    print "Matej at the ice cream"
elif dna.find(gender_male) and dna.find(race_white) and dna.find(hair_brown) and dna.find(eye_green) and dna.find(face_square) > -1:
    print "Miha ate the ice cream"
else:
    print "DNA does not match"