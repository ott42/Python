arvud = [10, 61, 2, 14, 42, 24, 7, 5] #muutuja arvud, range'i arvud

def arvude_jarjend(arv): #defineerib arvude järjendi
    summa = 0 #summa on 0
    for n in arv: # kui n on arv:
        summa += n #summale lisatakse n
        print(summa) #väljastab summa

if arvud == []: #kui arvud on võrdsed nulliga
    print(0) # väljastab arvu 0
print(arvude_jarjend(arvud)) #väljastab arvude järjendi ning arvud