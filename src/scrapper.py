from typing import List
import requests as _requests
import bs4 as _bs4
from bs4 import BeautifulSoup
from requests import get
#import pandas as pd

def _generation_url(nbre: int) -> str:
    #for i in range(1, nbre, 50):
    url='https://www.imdb.com/search/title/?release_date=2017-01-01,2017-12-31&sort=num_votes,desc&start='+str(nbre)+'&ref_=adv_nxt'
    return url

def _get_page(url: str) -> _bs4.BeautifulSoup:
    page= _requests.get(url)
    soup=_bs4.BeautifulSoup(page.content, "html.parser")
    return soup

def affichage(nbre: int) -> List[str]:
    url = _generation_url(nbre)
    page = _get_page(url)
    DivList=[]
    GrandDiv = page.findAll('div', class_ = 'lister-item mode-advanced')
    for div in GrandDiv:
        Num= div.find('span', class_="lister-item-index unbold text-primary").text
        Nom= div.find('img', class_="loadlate")
        Noms=Nom['alt']
        Annees= div.find('span', class_="lister-item-year text-muted unbold").text
        #certificate= div.find('span', class_="certificate")
        #runtime=div.find('span', class_="runtime")
        genre=div.find('span', class_="genre").text.strip('\n\t')
        rating= div.find('strong').text
        #metascores= div.find('span', class_="metascore favorable")
        votes=div.find('p', class_="sort-num_votes-visible").text.strip('\n\t').split('|')
        vote = votes[0].split(':')[1]
        gross = votes[-1].split(':')[1]
        obj = {
            'Num': Num,
            'Nom': Noms,
            'Annees': Annees.strip("()"),
            #'certificate': certificate,
            #'runtime': runtime,
            'genre': genre,
            'rating': rating,
            #'metascores': metascores,
            'votes': vote.strip("\n"),
            'gross': gross.strip('\n')
        }     
        DivList.append(obj)

    #print(DivList)
    return DivList

#affichage(51)
