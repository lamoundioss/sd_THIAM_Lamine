

import yaml
x = {
        "nom": "Durand",
        "famille":{
            "ecole": "mnt",
            "babacar":[1,2,3,4]
        },
        "prenom": "Christophe", 
        "date de naissance": "29/02/1981"
     }

def dictionnaireToYml(x):
    with open('fichier_yaml1.yaml', 'a') as f:
        
        fichier_csv = yaml.dump(x, f)
        return fichier_csv

print(dictionnaireToYml(x))

