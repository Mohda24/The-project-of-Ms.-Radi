import json
import os
def Ajouter():
    try:
        mylist1=[]
        n=int(input("Enter the number of articles: "))
        while n!=0:
            mydic={}
            mydic["Reference"]=int(input("Enter the reference of the article: "))
            mydic["Designation"]=input("Enter the designation of the article: ")
            categorie=""
            while categorie.lower() not in ["mobilier","nettoyage","patriciere","electronic"]:
                categorie=input("Enter the category of your article: ")
            mydic["categorie"]=categorie
            mydic["prix"]=float(input("Enter the price of the article: "))
            mydic["stock"]=int(input("Enter the stock: "))
            mylist1.append(mydic)
            n-=1
        if os.path.exists("products.json"):
            with open("products.json","r") as myfile:
                mylist=json.load(myfile)
        else:
            mylist=[]
        for el in mylist1:
            mylist.append(el)
        with open("products.json","w") as myfile:
            json.dump(mylist,myfile,indent=2)
    except Exception as e:
        print(f"Error: {e}")

def Chercher(reference):
    try:
        with open("products.json","r") as myfile:
            mylist=json.load(myfile)
            for el in mylist:
                if reference==el["Reference"]:
                     print(el)
                     return
            print("ne trouve pas article avec cette reference")
    except Exception as e:
        print(f"Error : {e}")
def List_par_catego(categorie):
    mycatego=[]
    if categorie.lower() in ["mobilier","nettoyage","patriciere","electronic"]:
        try:
            with open("products.json","r") as myfile:
                mylist=json.load(myfile)
                for el in mylist:
                    if el["categorie"].lower()== categorie.lower():
                        mycatego.append(el)
                if not mycatego:
                    print("pas des article de cette categorie!!")
                    return
                else:
                    print(mycatego)
        except FileNotFoundError:
            print("pas des articles!!!")
    else:
        print("entrer correct Categorie!!!!")
def Afficher():
    try:
        with open("products.json","r") as myfile:
            mylist=json.load(myfile)
            print(mylist)
    except:
        print("pas des articles!!")

def Inventairephysique():
    try:
        with open("products.json","r") as myfile:
            mylist=json.load(myfile)
            total_des_articles=0
            Stock_mobilier=0
            Stock_patricier=0
            Stock_nettoyage=0
            Stock_electronic=0
            for el in mylist:
                if el["categorie"].lower()=="mobilier":
                  total_des_articles+=el["stock"]
                  Stock_mobilier+=el["stock"]
                if el["categorie"].lower()=="nettoyage":
                  total_des_articles+=el["stock"]
                  Stock_mobilier+=el["stock"]
                if el["categorie"].lower()=="patriciere":
                  total_des_articles+=el["stock"]
                  Stock_mobilier+=el["stock"]
                if el["categorie"].lower()=="electronic":
                  total_des_articles+=el["stock"]
                  Stock_mobilier+=el["stock"]
            print("###################INVENTAIREPHYSIQUE###############################")
            print(f"Stock_mobilier : {Stock_mobilier} Article")
            print(f"Stock_patricier : {Stock_patricier} Article")
            print(f"Stock_nettoyage : {Stock_nettoyage} Article")
            print(f"Stock_electronic : {Stock_electronic} Article")
            print(f"Total of Stocks : {total_des_articles} Article")
    except:
        print("pas des articles!!!!")

def InventaireComptable():
    try:
        with open("products.json","r") as myfile:
            mylist=json.load(myfile)
            Prixtotal_des_articles=0
            Prix_des_mobilier=0
            Prix_des_patricier=0
            Prix_des_nettoyage=0
            Prix_des_electronic=0
            for el in mylist:
                if el["categorie"].lower()=="mobilier":
                  Prixtotal_des_articles+= (el["stock"]*el["prix"])
                  Prix_des_mobilier+= (el["stock"]*el["prix"])
                if el["categorie"].lower()=="patriciere":
                  Prixtotal_des_articles+= (el["stock"]*el["prix"])
                  Prix_des_patricier+= (el["stock"]*el["prix"])
                if el["categorie"].lower()=="electronic":
                  Prixtotal_des_articles+= (el["stock"]*el["prix"])
                  Prix_des_electronic+= (el["stock"]*el["prix"])
                if el["categorie"].lower()=="nettoyage":
                  Prixtotal_des_articles+= (el["stock"]*el["prix"])
                  Prix_des_nettoyage+= (el["stock"]*el["prix"])

            print("###################INVENTAIREComptable###############################")
            print(f"Prix_des_mobilier : {Prix_des_mobilier} DH")
            print(f"Prix_des_patricier : {Prix_des_patricier} DH")
            print(f"Prix_des_electronic : {Prix_des_electronic} DH")
            print(f"Prix_des_nettoyage {Prix_des_nettoyage} DH")
            print(f"Prixtotal_des_articles : {Prixtotal_des_articles} DH")
    except:
        print("pas des articles!!!!")
def Modifier(reference):
    try:
        with open("products.json","r") as myfile:
            mylist=json.load(myfile)
        found=False
        for el in mylist:
            if el["Reference"]==reference:
                found=True
                new_ref=""
                while type(new_ref)!=int:
                    new_ref=int(input("entrer new Reference : "))
                el["Reference"]=new_ref
        if found:
            with open("products.json","w") as myfile:
                json.dump(mylist,myfile,indent=2)
        else:
            print("pas article avec votre reference")
    except:
        print("pas drs articles!!")
Modifier(2)

