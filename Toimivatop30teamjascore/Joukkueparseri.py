def joukkueparse(lista:list):
    """Ottaa Joukkue listan ja käy läpi """
    Donelista = []
    for i in range(30):
        #Erittelee listan osiksi ja käy läpi yksitellen.
        joukkuelistaa = lista[i].parent
        joukkue = joukkuelistaa.find('span')
        stringit = joukkue.string
        Donelista.append(stringit)
    return Donelista
