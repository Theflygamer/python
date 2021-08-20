import random
# for in range hvor mange a den terning du vil have 
# nummerdice hvilken terning det er 
#random.randint den gør dit slag random som hvis det var en rigtigt terning
# hvis du vil ændre verdien på dem så det her du skal gøre det ((se eksemple))
# hvis du kun vil have 1 eller 2 terninger sååå slet en block se efter // det en block
for _ in range(1):
    #                        !((HER))!
    nummerdice = random.randint(1,6) 
    print ("du slog "+ str (nummerdice) + "\n")

for _ in range(1):
    nummerdice2 = random.randint(6,12) 
    print ("du slog "+ str (nummerdice2) + "\n")
#//
for _ in range(1):
    nummerdice3 = random.randint(12,18) 
    print ("du slog "+ str (nummerdice3) + "\n")
#//
for _ in range(1):
    nummerdice4 = random.randint(18,24) 
    print ("du slog "+ str (nummerdice4) + "\n")

for _ in range(1):
    nummerdice5 = random.randint(-30,30) 
    print ("du slog "+ str (nummerdice5) + "\n")

alt = [nummerdice+nummerdice2+nummerdice3+nummerdice4+nummerdice5];

print("du slog i alt " + str(alt))