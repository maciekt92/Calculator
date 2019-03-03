print ("kalkulator")

flaga = True

while flaga:
    a = int(input("Podaj pierwsza liczbe"))
    b = int(input("Podaj druga liczbe"))

    odp = input("podaj instrukcje suma/roznica/iloczyn/iloraz")
    if odp == "suma":
        c= a+b
        print ("wynik")
        print (c)
    elif odp == "roznica":
        c= a-b
        print ("wynik")
        print (c)
    elif odp == "iloczyn":
        c= a*b
        print ("wynik")
        print (c)
    elif odp == "iloraz":
        c = a/b
        print ("wynik")
        print (c)
    else:
        print("zla instrukcja")
        
    print("czy chcesz wylaczyc")
    decyzja = input("Wpisz False aby zakonczyc")
    if decyzja != False:
        flaga = True
