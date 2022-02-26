

from ast import YieldFrom
import csv
import json
import yaml
import xmltodict
from natureFichier import NatureFichier
from DictionnaireToXml import DictionnaireToXml
from DictionnaireToCsv import DictionnaireToCsv
from DictionnaireToYML import dictionnaireToYml
from DictionnaireToJson import DictionnaireToJson


fichier = input("Veuillez entrer le fichier que vous souhaitez convertir : ")

liste = ["xml", "csv", "json", "yml"]

rendu = NatureFichier(fichier)

if rendu == 1:
    liste = liste.remove('xml')
    with open('fichier.xml', 'r') as file:
        file = xmltodict.parse(file.read())
        files = json.load(json.dumps(file))
else:
    if rendu == 2:
        liste = liste.remove('csv')
        Donnee ={}
        with open('Donnee.csv', 'r') as file:
            line = file.read()
            section = line.split('\n')
            for i in section:
                el = i.split(',')
                Donnee[ el[0] ] = int ( el[1] )
    else:
        if rendu == 3:
            liste = liste.remove('yaml','yml')
            with open('yaml_file.yaml') as yaml_file:
                yaml_to_dict = yaml.safe_load(yaml_file)
        else:
            liste = liste.remove('json')
            with open('json_file.json', 'r') as json_file:
                json_to_dict = json.load(json_file)

print(f"1. Conversion vers {liste[0]}")
print(f"2. Conversion vers {liste[1]}")
print(f"3. Conversion vers {liste[2]}")
print("Tapez 0 pour quitter.")
choix = input("Faites votre choix : ")
if choix == 1:
    DictionnaireToXml(fichier)
else:
    if choix == 2:
        DictionnaireToCsv(fichier)
    else:
        if choix == 3:
            dictionnaireToYml(fichier)
        else:
            if choix == '4':
                DictionnaireToJson(fichier)