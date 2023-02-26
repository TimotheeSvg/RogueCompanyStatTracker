from tracemalloc import clear_traces
from ClassStat import statRogue
import os
from Glob import Mapliste

clear = lambda: os.system('cls')



def menu(option = 0):
    if(option == 0):
        print(
            "0 - Ajouter une game\n"
            "1 - Voir L'historique\n"
            "2 - Stat\n"
            "3 - Quitter\n")
        choixmenu = input("Que voulez vous faire ?\n")
        if choixmenu.isdigit():
            choixmenu = int(choixmenu)
            if(choixmenu == 0):
                ajouterPartie()
            elif(choixmenu == 1):
                historique()
            elif(choixmenu == 2):
                stat()
            else:
                quit()
        else:
            clear()
            print("Saisie incorrecte, veuillez refaire")
            menu(option)


def ajouterPartie():
    clear()
    #Création de l'objet et de l'id
    nouvellePartie = statRogue()
    print("Enregistrement d'une nouvelle partie : " + str(nouvellePartie.GameID) + "\n\n")
    #Demande des information supplémentaire
    #   1 - Map
    #   2 - Score
    #   3 - Disco

    #1 Map
    print("=== Map ===")
    for i, element in enumerate(Mapliste):
        print(str(i) + " - " + str(element))
    inputMap = input("\nMap : ")
    if inputMap.isdigit():
        inputMap = int(inputMap) 
        if 0 <= inputMap and inputMap <= len(Mapliste) - 1:
            nouvellePartie.Map = inputMap
        else:
            print("Saisie incorrecte, veuillez refaire")
            quit()
    else:
        print("Saisie incorrecte, veuillez refaire")
        quit()
    #2 Score
    # Score équipe
    print("\n=== Score ===")
    inputScoreEquipe = input("Score équipe : ")
    if inputScoreEquipe.isdigit(): 
        inputScoreEquipe = int(inputScoreEquipe)
        if 0 <= inputScoreEquipe and inputScoreEquipe <= 7:
            nouvellePartie.ScoreA = inputScoreEquipe
        else:
            print("Saisie incorrecte, veuillez refaire")
            quit()
    else:
        print("Saisie incorrecte, veuillez refaire")
        quit()

    # Score ennemi
    inputScoreEnnemi = input("Score Ennemi : ")
    if inputScoreEnnemi.isdigit():
        inputScoreEnnemi = int(inputScoreEnnemi)
        if 0 <= inputScoreEnnemi and inputScoreEnnemi <= 7:
            nouvellePartie.ScoreE = inputScoreEnnemi
        else:
            print("Saisie incorrecte, veuillez refaire")
            quit()
    else:
        print("Saisie incorrecte, veuillez refaire")
        quit()
    #3 Disco
    print("\n=== Deconnexion ===")
    Disconnected = input("\n4v4 ? (1: OUI, 0: NON) : ")
    if Disconnected.isdigit():
        Disconnected = int(Disconnected)
        if Disconnected == 1:
            opt = 0
        elif Disconnected == 0:
            opt = ajoutOption()
        else:
            print("Saisie incorrecte, veuillez refaire")
            quit()
        nouvellePartie.option = opt
    else:
        print("Saisie incorrecte, veuillez refaire")
        quit()   

    input("Confirmer ?")
    nouvellePartie.ajouterPartie()


def historique():
    print("of")

def stat():
    print("of")

def ajoutOption():
    print("1 - 4v3\n"
    "2 - 3v4\n")
    opt = input("Format : ")
    if opt.isdigit(): 
        opt = int(opt)
    if 0 <= opt and opt <= 2:
        return opt
    else:
        print("Saisie incorrecte, veuillez refaire")
        quit()       





clear()
menu()