

import csv


def DictionnaireToCsv(toCSV):
    toCSV = list(toCSV)
    keys = toCSV[0].keys() 
    with open('people.csv', 'w', newline='') as output_file: 
        dict_writer = csv.DictWriter(output_file, keys) 
        dict_writer.writeheader() 
        dict_writer.writerows(toCSV)
    
    #with open('dicte.csv','w') as files:
    #    writer = csv.writer(files)
    #    for key, value in dictionnaire.items():
    #        dicte = writer.writerow([key, value])
    
    #return dicte


#dct = {'Name': 'John', 'Age': '23', 'Country': 'USA'}


#toCSV = [{'name':'bob','age':25,'weight':200}, {'name':'jim','age':31,'weight':180}]


#mon_dico = {"nom": "Durand", "prenom": "Christophe", "date de naissance": "29/02/1981"}


#print(DictionnaireToCsv(toCSV))