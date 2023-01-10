import requests
from bs4 import BeautifulSoup
import time
from Toimivatop30teamjascore.Pisteparseri import parseri
from Toimivatop30teamjascore.intparse import intmuuttaja
from Toimivatop30teamjascore.Joukkueparseri import joukkueparse
import pandas as pd


sivu = 'https://www.hltv.org/ranking/teams/2022/july/25'
scrape = requests.get(sivu)
soup = BeautifulSoup(scrape.text,"html.parser")

vuodet = ['2015','2016','2017','2018','2019','2020','2021','2022']
kuukaudet = ['january','february','march','april','may','june','july','august','september','october','november','december']
writer = pd.ExcelWriter('herewego.xlsx',engine='openpyxl')
#For looppi joka lisää urliin jokaisen päivän,kuukauden ja vuoden.
for vuosi in vuodet:
    for kuukausi in kuukaudet:
        for päivä in range(1,31):
            sivu = f'https://www.hltv.org/ranking/teams/{vuosi}/{kuukausi}/{päivä}'
            paiva = sivu[sivu.find('teams'):]
            paiva = paiva.replace("/","")
            scrape = requests.get(sivu)
            soup = BeautifulSoup(scrape.text,"html.parser")
            joukkue = soup.findAll('span', {'class':'name'})
            pisteet = soup.findAll('span', {'class':'points'})
            #pistevali laittaa scrapen funktioon joka tekee numeroista listan
            try:
                joukkuelista = joukkueparse(joukkue)
            except IndexError:
                continue
            pisteVali = parseri(pisteet)
            #intlista ottaa pistevali listan joka on str muodossa ja ylimääräisä välejä
            #ottaa välit pois ja muuttaa str arvot Int arvoihin.
            intlista = intmuuttaja(pisteVali)

            data = {'Joukkueet': joukkuelista, 'Pisteet' : intlista}
            df = pd.DataFrame(data)  

            # Write the data to the first sheet
            df.to_excel(writer,index=False, sheet_name=paiva)
            print("ennensleep")
            time.sleep(1)
            print("aftersleep")

writer.save()
