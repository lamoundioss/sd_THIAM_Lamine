

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

listes = ["xml", "csv", "json", "yml"]

rendu = NatureFichier(fichier)

if rendu == 1:
    liste = listes.remove('xml')
    with open(fichier, 'r') as file:
        file = xmltodict.parse(file.read())
        fichier = json.loads(json.dumps(file))
else:
    if rendu == 2:
        liste = listes.remove('csv')
        dict_from_csv = []
        with open(fichier, 'r') as file:
            line = csv.reader(file, delimiter = ";")
            lecture = list(line)

            for i in range(len(lecture)):
                if i != 0:
                    dicte = dict()
                    for j in range(len(lecture[0])):
                        dicte[lecture[0][j]] = lecture[i][j]
                    dict_from_csv.append(dicte)
        fichier = dict_from_csv
            
    else:
        if rendu == 3:
            liste = listes.remove('yml')
            with open(fichier) as yaml_file:
                yaml_to_dict = yaml.safe_load(yaml_file)
        else:
            if rendu == 4:
                liste = listes.remove('json')
                with open(fichier, 'r') as json_file:
                    json_to_dict = json.load(json_file)
print(listes)
print(listes[0])
print(f"{listes[0]}. Conversion vers {listes[0]}")
print(f"{listes[1]}. Conversion vers {listes[1]}")
print(f"{listes[2]}. Conversion vers {listes[2]}")
print("Tapez 0 pour quitter.")
choix = input("Faites votre choix : ")
if choix == 'xml':
    DictionnaireToXml(fichier)
else:
    if choix == 'csv':
        DictionnaireToCsv(fichier)
    else:
        if choix == 'yml':
            dictionnaireToYml(fichier)
        else:
            if choix == 'json':
                DictionnaireToJson(fichier)