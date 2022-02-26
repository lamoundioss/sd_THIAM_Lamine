

from xml.etree.ElementTree import Element, tostring
import xmltodict    
import dict2xml

def DictionnaireToXml(dictionnary):
    with open('fichier.xml', "a") as file:
        file = dict2xml(dictionnary)
    
#x = "tete"
#mon_dico = {"nom": "Durand", "prenom": "Christophe", "date de naissance": "29/02/1981"}

#f = print(DictionnaireToXml(x, mon_dico))
#print(tostring(f))