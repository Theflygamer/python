import random

while True:

    print ("\n GÆT NUMMERT :) hvis du kan")
    print ("\n Du har 9 forsøg goooood LUCK")

    nummer = random.randint (1,30)


    chancer = 0

    print ("\n gæt et tal 1-30")

    while chancer < 9:

        gæt = int(input())

        if gæt ==nummer:
            print("\n du vandt !!!!!")
            break
        elif gæt < nummer:
            print("\n det var for lavt", gæt)

        else:
            print("\n du gættet for højt",gæt)
            

            chancer += 1

            if not chancer <9:
                print("\n du tabt!!!!!!!!! nummret var",nummer)
                
                ans=input("\n vil du spille igen ;) (j=ja    N=nej)")

                if ans != 'j':
                    break

print ("\n Tak for du spillet med :)")

