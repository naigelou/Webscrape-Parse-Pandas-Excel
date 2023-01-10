def parseri(lista:list):
    """Ottaa listan scrapetusta datasta ja tekee niistä mukavan luettavaa :)"""
    pisteet = []
    Listadone = []
    numerot = ["1","2","3","4","5","6","7","8","9","0"]
    numeroissa = False
    stringlista= str(lista)
    for i in stringlista:
        if i in numerot:
            numeroissa = True
            pisteet.append(i)
        if i not in numerot and numeroissa == True:
            pisteet.append(',')
            numeroissa = False
    liitos = ' '.join(pisteet)
    Listadone.append(liitos)
    PistelistaDonez = liitos.split(',')
    if len(PistelistaDonez) > 30:
        del PistelistaDonez[-1]
    
    return PistelistaDonez
