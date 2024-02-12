import csv
import os
def Ajouter():
    try:
        mylist1 = []
        n = int(input("Enter the number of articles: "))
        while n != 0:
            mydic = {}
            mydic["Reference"] = int(input("Enter the reference of the article: "))
            mydic["Designation"] = input("Enter the designation of the article: ")
            categorie = ""
            while categorie.lower() not in ["mobilier", "nettoyage", "patriciere", "electronic"]:
                categorie = input("Enter the category of your article: ")
            mydic["categorie"] = categorie
            mydic["prix"] = float(input("Enter the price of the article: "))
            mydic["stock"] = int(input("Enter the stock: "))
            mylist1.append(mydic)
            n -= 1
        filename = "products.csv"
        file_exists = os.path.exists(filename)

        with open(filename, mode=file_exists and 'a' or 'w', newline='') as csvfile:
            fieldnames = ["Reference", "Designation", "categorie", "prix", "stock"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if not file_exists:
                writer.writeheader()

            for el in mylist1:
                writer.writerow(el)
    except Exception as e:
        print(f"Error: {e}")
def Chercher(reference):
    try:
        filename = "products.csv"
        with open(filename, mode='r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if reference == int(row["Reference"]):
                    print(row)
                    return
            print("No article found with this reference")
    except Exception as e:
        print(f"Error: {e}")
def List_par_catego(categorie):
    try:
        filename = "products.csv"
        with open(filename, mode='r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            mycatego = [row for row in reader if row["categorie"].lower() == categorie.lower()]

            if not mycatego:
                print("No articles in this category!")
                return
            else:
                print(mycatego)
    except FileNotFoundError:
        print("No articles!")
    except Exception as e:
        print(f"Error: {e}")
def Afficher():
    try:
        filename = "products.csv"
        with open(filename, mode='r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("No articles!")
def Inventairephysique():
    try:
        filename = "products.csv"
        with open(filename, mode='r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            total_des_articles = 0
            Stock_mobilier = 0
            Stock_patricier = 0
            Stock_nettoyage = 0
            Stock_electronic = 0
            for row in reader:
                if row["categorie"].lower() == "mobilier":
                    total_des_articles += int(row["stock"])
                    Stock_mobilier += int(row["stock"])
                if row["categorie"].lower() == "nettoyage":
                    total_des_articles += int(row["stock"])
                    Stock_nettoyage += int(row["stock"])
                if row["categorie"].lower() == "patriciere":
                    total_des_articles += int(row["stock"])
                    Stock_patricier += int(row["stock"])
                if row["categorie"].lower() == "electronic":
                    total_des_articles += int(row["stock"])
                    Stock_electronic += int(row["stock"])
            print("###################INVENTAIREPHYSIQUE###############################")
            print(f"Stock_mobilier : {Stock_mobilier} Article")
            print(f"Stock_patricier : {Stock_patricier} Article")
            print(f"Stock_nettoyage : {Stock_nettoyage} Article")
            print(f"Stock_electronic : {Stock_electronic} Article")
            print(f"Total of Stocks : {total_des_articles} Article")
    except FileNotFoundError:
        print("No articles!")
    except Exception as e:
        print(f"Error: {e}")
def InventaireComptable():
    try:
        filename = "products.csv"
        with open(filename, mode='r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            Prixtotal_des_articles = 0
            Prix_des_mobilier = 0
            Prix_des_patricier = 0
            Prix_des_nettoyage = 0
            Prix_des_electronic = 0
            for row in reader:
                if row["categorie"].lower() == "mobilier":
                    Prixtotal_des_articles += (int(row["stock"]) * float(row["prix"]))
                    Prix_des_mobilier += (int(row["stock"]) * float(row["prix"]))
                if row["categorie"].lower() == "patriciere":
                    Prixtotal_des_articles += (int(row["stock"]) * float(row["prix"]))
                    Prix_des_patricier += (int(row["stock"]) * float(row["prix"]))
                if row["categorie"].lower() == "electronic":
                    Prixtotal_des_articles += (int(row["stock"]) * float(row["prix"]))
                    Prix_des_electronic += (int(row["stock"]) * float(row["prix"]))
                if row["categorie"].lower() == "nettoyage":
                    Prixtotal_des_articles += (int(row["stock"]) * float(row["prix"]))
                    Prix_des_nettoyage += (int(row["stock"]) * float(row["prix"]))
            print("###################INVENTAIREComptable###############################")
            print(f"Prix_des_mobilier : {Prix_des_mobilier} DH")
            print(f"Prix_des_patricier : {Prix_des_patricier} DH")
            print(f"Prix_des_electronic : {Prix_des_electronic} DH")
            print(f"Prix_des_nettoyage : {Prix_des_nettoyage} DH")
            print(f"Prixtotal_des_articles : {Prixtotal_des_articles} DH")
    except FileNotFoundError:
        print("No articles!")
    except Exception as e:
        print(f"Error: {e}")
def Modifier(reference):
    try:
        filename = "products.csv"
        with open(filename, mode='r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            mylist = list(reader)
        found = False
        for row in mylist:
            if int(row["Reference"]) == reference:
                found = True
                new_ref = ""
                while type(new_ref)!=int:
                    new_ref = int(input("Enter new Reference: "))

                row["Reference"] = new_ref
                break
        if found:
            with open(filename, mode='w', newline='') as csvfile:
                fieldnames = ["Reference", "Designation", "categorie", "prix", "stock"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(mylist)
        else:
            print("No article with your reference")
    except FileNotFoundError:
        print("No articles!")
    except Exception as e:
        print(f"Error: {e}")
Modifier(222)


