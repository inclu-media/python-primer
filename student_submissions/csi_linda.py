
'''
DNA_file = open ("DNA_file.txt").read ()

Take extra care not to include extra, unnecessary white spaces.
That makes the code harder to read. PyCharm shows a yellow wavy line if it doesn't like your formatting.
'''

DNA_file = open("dna.txt").read()



#Hair color:
hair_black = "CCAGCAATCGC"
hair_brown = "GCCAGTGCCG"
hair_carrot = "TTAGCTATCGC"
#Facial shape:
face_square = "GCCACGG"
face_round = "ACCACAA"
face_oval = "AGGCCTCA"
#Eye color:
eye_blue = "TTGTGGTGGC"
eye_green = "GGGAGGTGGC"
eye_brown = "AAGTAGTGAC"
#Gender
sex_female = "TGAAGGACCTTC"
sex_male = "TGCAGGAACTTC"
#Race:
race_white = "AAAACCTCA"
race_black = "CGACTACAG"
race_asian = "CGCGGGCCG"

"""Suspects characteristics:
Ziga: Gender: Male, Race: White, Hair color: Orange, Eye color: Brown, Face shape: Round
Matej:Gender: Male, Race: White, Hair color: Black, Eye color: Blue, Face shape: Oval
Miha:Gender: Male,Race: White,Hair color: Brown,Eye color: Green,Face shape: Square
"""

if DNA_file.find(hair_black) > -1:
    print ("hair_black!")
elif DNA_file.find(hair_brown) > -1:
    print ("hair_brown!")
else:
    print ("hair_carrot!")

if DNA_file.find(face_square) > -1:
    print ("face_square!")
elif DNA_file.find(face_round) > -1:
    print ("face_round!")
else:
    print ("face_oval!")

if DNA_file.find(eye_blue) > -1:
    print ("eye_blue!")
elif DNA_file.find(eye_green) > -1:
    print ("eye_green!")
else:
    print ("eye_brown!")

if DNA_file.find(sex_female) > -1:
    print ("sex_female!")
else:
    print ("sex_male!")

if DNA_file.find(race_white) > -1:
    print ("rrace_white!")
elif DNA_file.find(race_black) > -1:
    print ("race_black!")
else:
    print ("race_asian!")