from typing import Dict
import json as _json

def get_all_data() -> Dict:
    with open("taille.json", "r") as data_file:
        data = _json.load(data_file)
    
    return data

def get_donner_nbre(nbre: int) -> Dict:
    dats = get_all_data()
    try:
        donner_nbre = dats[nbre]
        return donner_nbre
    except KeyError:
        return "Ce notre n'est pas correcte"