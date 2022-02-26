

import csv


def DictionnaireToCsv(dictionnaire):
    
    with open('dicte.csv','w') as files:
        writer = csv.writer(files)
        for key, value in dictionnaire.items():
            dicte = writer.writerow([key, value])
    
    return dicte


dct = {'Name': 'John', 'Age': '23', 'Country': 'USA'}




mon_dico = {"nom": "Durand", "prenom": "Christophe", "date de naissance": "29/02/1981"}


print(DictionnaireToCsv(mon_dico))