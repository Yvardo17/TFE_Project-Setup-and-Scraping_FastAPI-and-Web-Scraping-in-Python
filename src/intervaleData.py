from typing import Iterator, Dict
import scrapper as _scrapper
import json as _json

def defInterval() -> Dict:
    Interval = dict()
    taille = dict()

    for i in range(1, 4000, 50):
        #print(i)
        Interval[i] = i
        
    #print(Interval)

    if i not in Interval:
        print("le pas d'incrimentation est de 50, alors trouver un nombre")

    taille[i] = _scrapper.affichage(i)
    return(taille)

#defInterval()

if __name__=="__main__":
    taille = defInterval()
    with open("taille.json", "w") as taille_file:
        _json.dump(taille, taille_file, ensure_ascii=False)