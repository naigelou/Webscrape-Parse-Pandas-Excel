def intmuuttaja(lista:list) -> list:
    Uuslista = []
    intlista = []
    for i in lista:
        x = i.replace(" ", "")
        Uuslista.append(x)
    for i in Uuslista:
        x = int(i)
        intlista.append(x)
    return intlista