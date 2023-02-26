import csv
import os
import time
from datetime import datetime
enregistrementListe=[
    "Map",
    "ScoreA",
    "ScoreE",
    "Elim",
    "Down",
    "Degat",
    "Gagner",
    "Mj"

]

Mapliste = [
    "Breach",
    "Hollows",
    "Lockdown",
    "Vice",
    "Hight Castle",
    "Skyfell",
    "Favelas",
    "Windward",
    "Canals",
    "Icarus",
    "Factory",
    "Palace",
    "Meltdown",
    "Wanted",
    "Retour au Menu"
]

clear = lambda: os.system('cls')

def ecrireDonnee(info):
    date = datetime.now()
    date = date.strftime("%H:%M-%d/%m")
    info.append(date)
    with open("stat.csv", 'a', newline="\n") as csvfile:
        f = csv.writer(csvfile, delimiter = ",")
        f.writerow(info)

def menu():
    HisotriqueGame()
    print("\n\n1 - Ajouter une game")
    print("2 - Voir mes stats")
    print("3 - Voir l'historique d'une map")
    print("4 - Historique complet")
    print("5 - Quitter\n")

    choix = int(input("Que faire ?"))
    if(choix == 1):
        menumap()
    elif(choix == 2):
        afficherStat()
    elif(choix == 3):
        afficherStatPrecise()
    elif(choix == 4):
        toutHisotriqueGame()
    else:
        print("Vous avez quitté")
        clear()
        quit()

def menuRetour():
    print("\n\n1 - Retour au menu")
    print("2 - Quitter\n")

    choix = int(input("Que faire ?"))
    if(choix == 1):
        menu()
    else:
        print("Vous avez quitté")
        clear()
        quit()
    
def menumap():
    clear()
    for i, element in enumerate(Mapliste):
        print(str(i) + " - " + str(element))
    Map = int(input("\nChoix : "))

    if(int(Map) == len(Mapliste) - 1):
        menu()

    elif( int(Map) > len(Mapliste)):
        print("Mauvaise Map réessayer")
        time.sleep(1)
        menumap()
    else:   
        clear()
        print("Enregistrement d'une partie sur la map : " + str(Mapliste[Map]))
        ScoreAllier = int(input("Score de l'équipe : "))
        ScoreEnnemi = int(input("Score des adversaires : "))
        ElimPerso = int(input("Elim Perso : "))
        DownPerso = int(input("Down Perso : "))
        DegatPerso =  int(input("Degat Perso : "))
        MJ_ = int(input("MJ : "))
        if(ScoreAllier > ScoreEnnemi):
            Gagne = 1
        else:
            Gagne = 0

        info = [
            Map,ScoreAllier,ScoreEnnemi,ElimPerso,DownPerso,DegatPerso,Gagne,MJ_
        ]
        ecrireDonnee(info)
        clear()
        print("\n\n#####   Résumer   #####\n\n"
        "Map : " + str(Mapliste[Map]) + " \n"
        "score: " + str(ScoreAllier) + "-" + str(ScoreEnnemi) + " \n"
        "Elim: " + str(ElimPerso) + "\n"
        "Down: " + str(DownPerso) +"\n" 
        "Dégats: " + str(DegatPerso) + "\n"
        "Dégats round: " + str(round(int(DegatPerso)/(int(ScoreAllier) + int(ScoreEnnemi)),2)))

        print("MJ : Oui\n" if MJ_ == 1 else "MJ : Non\n")
        menuRetour()

def HisotriqueGame():
    clear()
    tabHistorique = []
    with open("stat.csv", 'r', newline="\n") as csvfile:
        objt = csv.reader(csvfile)
        for line in objt:
            tabHistorique.append(line)
    tabHistorique = tabHistorique[len(tabHistorique) - 3:]
    for element in tabHistorique:
        date = element[8].split("-")
        print("===" + str(Mapliste[int(element[0])]) + "===    Le "+ date[1] +" à "+ date[0] +"\n"
        "Score: " + str(element[1]) + "-" + str(element[2]) + " \nPerso: " + str(element[3])+ " - " + str(element[4])+ "\n"
        "Dégats: " + str(element[5]) + " - " +str(round(int(element[5])/(int(element[1])+int(element[2])),2)))
        print("MJ : Oui\n" if int(element[7]) == 1 else "MJ : Non\n")

def toutHisotriqueGame():
    clear()
    tabHistorique = []
    with open("stat.csv", 'r', newline="\n") as csvfile:
        objt = csv.reader(csvfile)
        for line in objt:
            tabHistorique.append(line)
    for element in tabHistorique:
        date = element[8].split("-")
        print("=== " + str(Mapliste[int(element[0])]) + " ===    Le "+ date[1] +" à "+ date[0] +"\n"
        "Score: " + str(element[1]) + "-" + str(element[2]) + " \n"
        "Perso: " + str(element[3])+ " - " + str(element[4])+ "\n"
        "Dégats: " + str(element[5]) + " - " +str(round(int(element[5])/(int(element[1])+int(element[2])),2)))
        print("MJ : Oui\n" if int(element[7]) == 1 else "MJ : Non\n")
    menuRetour()

def afficherStat():
    clear()

    cmpt = 0
    elim = 0
    down = 0
    degat = 0
    victoire = 0
    MJcount = 0
    degatTotal = 0
    mancheTotal = 0
    tabtempline = []
    tabmap = []
    tabmapsort = []
    with open("stat.csv", 'r', newline="\n") as csvfile:
        objt = csv.reader(csvfile)
        for line in objt:
            tabtempelement = []
            for element in line:
                if(element.isdigit()):
                    tabtempelement.append(int(element))
                else:
                    tabtempelement.append(element)
            tabtempline.append(tabtempelement)
    
    for i in range(len(Mapliste) - 1):
        for element in tabtempline:
            if(element[0] == i):
                tabmap.append(element)
        tabmapsort.append(tabmap)
        tabmap = []
    
    for element in tabtempline:
        degatTotal += element[5]
        mancheTotal += element[1] + element[2]
        elim += element[3]
        down += element[4]
        degat += element[5]
        victoire += element[6]
        MJcount += element[7]
        cmpt += 1
    
    elim = elim/cmpt
    down = down/cmpt
    degat = degat/cmpt
    victoire = round(victoire/cmpt*100,2)
    MJcount = round(MJcount/cmpt*100,2)
    degatMoyenRound = degatTotal / mancheTotal


    for i, element in enumerate(tabmapsort):
        if(len(element) != 0):
            
            print("                     #### " + str(Mapliste[i]) +" ####" )
            print("partie jouées : "+ str(len(element)))
            print("Victoire : " + str(calculMoyenneVictoire(element,6)) + "%" )
            print("Eliminaiton : " + str(calculMoyenne(element, 3)))
            print("Down : " + str(calculMoyenne(element, 4)))
            print("Dégats par partie: " + str(calculMoyenne(element, 5)))
            print("Dégats par round: " + str(round(calculmoyenneDegatRound(element),2)))
            print("MJ : " + str(calculMoyenneVictoire(element, 7)) + "%")
            

            print("\n")
    print("======= GLOBAL ========")
    print("Nombre de Partie : " + str(len(tabtempline)))
    print("Elimination: " + str(round(elim,2)))
    print("Down: " + str(round(down,2)))
    print("Dégat moyen par partie: " + str(round(degat,2)))
    print("Dégats moyen par round: " + str(round(degatMoyenRound,2)))
    print("victoire: " + str(victoire) + "%")
    print("MJ moyen : " + str(MJcount) + "%")
    menuRetour()
            
def afficherStatPrecise():
    clear()
    for i, element in enumerate(Mapliste):
        print(str(i) + " - " + str(element))
    Map = int(input("\nChoix : "))

    clear()
    print(str(Mapliste[int(Map)])+"\n\n")
    
    tabtempline = []
    with open("stat.csv", 'r', newline="\n") as csvfile:
        objt = csv.reader(csvfile)
        for line in objt:
            tabtempelement = []
            if int(line[0]) == int(Map):
                for element in line:
                    if element.isdigit():
                        tabtempelement.append(int(element))
                    else:
                        tabtempelement.append(element)
                tabtempline.append(tabtempelement)

    for element in tabtempline:
        date = element[8].split("-")
        print("====== Le "+ date[1] +" à "+ date[0] +"   \nScore: " + str(element[1]) + "-" + str(element[2]) + " \n"
        "Perso: " + str(element[3])+ " - " + str(element[4])+ "\n"
        "Dégats: " + str(element[5]) + " - " +str(round(int(element[5])/(int(element[1])+int(element[2])),2)))
        print("MJ : Oui\n======\n" if int(element[7]) == 1 else "MJ : Non\n======\n")
    menuRetour()

def calculMoyenne(tab, i):
    cal = 0
    for element in tab:
        cal += element[i]
    return round(cal/len(tab), 2)

def calculMoyenneVictoire(tab,i):
    cal = 0
    for element in tab:
        cal += element[i]
    return round(cal/len(tab)*100,2)

def calculmoyenneDegatRound(tab):
    cal = 0
    deg = 0
    for element in tab:
        cal += element[1] + element[2]
        deg += element[5]
    cal = deg/cal
    return round(cal,2)
################################################
################################################
def main():
    if((open("stat.csv", 'r')) is False):
        open("stat.csv", 'x')
    menu()
main()