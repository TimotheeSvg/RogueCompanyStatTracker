from PIL import Image
from pytesseract import pytesseract
import glob
import time
import csv
import os
import random
from datetime import datetime
from random import randint
import Glob

clear = lambda: os.system('cls')


class statRogue:
    
    pathstatHistorique = "Stat/@P@xdez.csv"
    pathHistoriqueGame = "Game/GameHistorique.csv"
    pathScreenshot = ""
    pathRogne = ""
    NamePlayer = []
    textToTab = []
    ScoreA = 0
    ScoreE = 0
    GameID = 0
    Jour = datetime.now().strftime("%x")
    Heure = datetime.now().strftime("%X")
    Map = 0
    option = 0
    MapListe = Glob.Mapliste
    
    def __init__(self):

        #self.pathImageGame = self.fileFinder()
        self.GameID = self.createIdGame()
        #self.pathImageGameRogne = self.rogne()
        #self.listImageRogne = self.colorManagement()
        #self.textTotal = self.imageToText()
        #for element in self.textTotal:
            #self.textToTab.append(self.parsingStat(element))
    
        #print("tab des resultat : ")
        #print(self.textToTab)
        #print("La liste des joueurs : ")
        #print(self.NamePlayer)

    def ajouterPartie(self):
        clear()
        #Choix du fichier de la photo
        print("Choix du fichier :")
        self.pathScreenshot = self.fileFinder()
        #Rogne la photo voulu Récupération du path rogne
        print("Rogne")
        self.pathRogne = self.rogne()
        #Color des photos path rogne
        print("couleur")
        self.colorManagement()
        #Image to text
        print("text")
        self.tabText = self.imageToText()
        self.enregistrerDonnée()

    
    def parsingStat(self, phr):
        tabvalue = []
        value = ""
        for i,element in enumerate(phr):
            if element == " " and phr[i +1].isdigit():
                tabvalue.append(value)
                value = ""
            else:
                value += element
        
        tabvalue.append(value)
        return tabvalue

    def enregistrerDonnée(self):

        for i,element in enumerate(self.tabText):
            if(element[0].find("#MJ/#") != -1):
                self.tabText[i][0] = element[0].strip("#MJ/#")
                self.tabText[i].append(1)
            else:
                self.tabText[i].append(0)
            self.tabText[i].append(self.GameID)
            self.NamePlayer.append(self.tabText[i][0])

        for info in self.tabText:
            with open("Players/"+ info[0]+".csv", 'a', newline="\n") as csvfile:
                f = csv.writer(csvfile, delimiter = ",")
                f.writerow(info)
        
        Gameinfo = [
                self.GameID,
                self.Map,
                self.ScoreA,
                self.ScoreE,
                self.option,
                self.Jour,
                self.Heure,
                self.NamePlayer
            ]
        with open("GameHistorique/Data.csv", 'w', newline="\n") as csvfile:
                f = csv.writer(csvfile, delimiter = ",")
                f.writerow(Gameinfo)

        ##TODOO 
        #Demander Resumer de la partie à enregistrer avant
        #enregistrement de la photo général dans un historique
        #Appelle destructeur Suppression de toute les données photo etc

            


    def fileFinder(self):
        cmp = 0
        list_ = glob.glob("../../../Users/Moi/Videos/Radeon ReLive/Rogue Company/*.png") 
        for element in list_:
            #nomDesScreen.append(element[54:])
            print(str(cmp)+ " - " + str(element[54:]))
            cmp +=1
        choix = int(input("choix : "))
        # for element in list_:
        #     os.remove(element)
        # list_ = glob.glob("../../../Users/Moi/Videos/Radeon ReLive/Rogue Company/*.png") 
        return list_[choix]


    def replaceError(self, phrase):
        error = [
            " W ",
            " WF ",
            " % ",
            "\n",
            " Q ",
            " a ",
            " ia) "
            " EE "
            ]
        replace = [
            " #MJ/# ",
            " #MJ/# ",
            " #MJ/# ",
            " ",
            " 0 ",
            " 0 ",
            " 0 ",
            " 9 "
        ]
        for i,element in enumerate(error):
            if element in phrase:
                phrase = phrase.replace(element, replace[i])
        return phrase

    def colorManagement(self):
        list_ = glob.glob(self.pathRogne + '/*.png')
        for element in list_:
            im = Image.open(element)
            (l,h) = im.size
            newImage = Image.new('L', (l,h))
            for x in range(l):
                for y in range(h):
                    # print("pixel : " + str(x) + " ," + str(y))
                    r,g,b,a = im.getpixel((x,y))
                    value = int(r*299/1000 + g*585/1000 + b*114/1000)
                    value = 0 if value > 126 else 255
                    newImage.putpixel((x,y), value)
            newImage.save(element)

    def imageToText(self):
        list_ = glob.glob(self.pathRogne + "/*.png")
        text = []
        path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        for element in list_:
            img = Image.open(element)
            pytesseract.tesseract_cmd = path_to_tesseract
            phr2 = pytesseract.image_to_string(img)
            phr2 = self.replaceError(phr2)
            phr2 = self.parsingStat(phr2.strip())
            text.append(phr2)
        return text

    def rogne(self): 

        self.pathRogne = "Game/Game"+str(self.GameID)
        os.makedirs(self.pathRogne)
        tabTaille = self.gestionOption()

        im = Image.open(self.pathScreenshot)
        player = 0
        equipe = 0
        for element in tabTaille:
            # Define box inside image
            left = element[0]
            top = element[1]
            width = element[2]
            height = element[3]

            # Create Box
            box = (left, top, left+width, top+height)
            # Crop Image
            area = im.crop(box)
            #Create name
            name = self.pathRogne + "/Player" + str(player)+ ".png"
                # Save Image
            area.save(name, "PNG")
            player +=1

        return self.pathRogne

    def gestionOption(self):
        #0 - 4v4
        #1 - 4v3
        #2 - 3v4
        if(self.option == 0):
            tabTaille = [
                [462,305,1087,41],
                [462,350,1087,41],
                [462,396,1087,41],
                [462,442,1087,41],

                [462,539,1087,41],
                [462,584,1087,41],
                [462,630,1087,41],
                [462,676,1087,41]
            ]
        elif self.option == 1:
            tabTaille = [
                [462,305,1087,41],
                [462,350,1087,41],
                [462,396,1087,41],
                [462,442,1087,41],

                [462,539,1087,41],
                [462,584,1087,41],
                [462,630,1087,41],
            ]
        elif self.option == 2:
            tabTaille = [
                [462,305,1087,41],
                [462,350,1087,41],
                [462,396,1087,41],

                
                [462,492,1087,41],
                [462,538,1087,41],
                [462,584,1087,41],
                [462,630,1087,41]
            ]
        
        return tabTaille

    def createIdGame(self):
        req = str(randint(1,100)) + str(randint(1,100)) + str(randint(1,100))

        #TODOO Tchek les ID mit pour ne pas avoir de doublon
        return req




sts = statRogue()



