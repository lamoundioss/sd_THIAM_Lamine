
def NatureFichier(fichier):
    fichier = input("Veuillez donner un fichier.")
    fichier = fichier.split(".")

    extension = fichier[-1]

    if extension == "xml":
        print("Ceux-ci est un fichier xml.")
        Test = 1
    else:
        if extension == "csv":
            print("C'est un fichier csv")
            Test = 2
        else:
            if extension == "yml":
                print("C'est un fichier yml")
                Test = 3
            else:
                if extension == "json":
                    print("C'est un fichier json.")
                    Test = 4
                else:
                    print("Fichier non valide.")
                    Test = 0
    return Test
