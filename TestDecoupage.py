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


def replaceError(phrase):
    error = [
        " W ",
        "\n",
        " Q ",
        " a ",
        " ia) "
        ]
    replace = [
        " ",
        "",
        " 0 ",
        " 0 ",
        " 0 "
    ]
    for i,element in enumerate(error):
        if element in phrase:
            phrase = phrase.replace(element, replace[i])
    return phrase

def colorManagement(path):
   
    im = Image.open(path)
    (l,h) = im.size
    newImage = Image.new('L', (l,h))
    for x in range(l):
        for y in range(h):
            # print("pixel : " + str(x) + " ," + str(y))
            r,g,b,a = im.getpixel((x,y))
            value = int(r*299/1000 + g*585/1000 + b*114/1000)
            value = 0 if value > 126 else 255
            newImage.putpixel((x,y), value)
    newImage.save(path+"color")

def imageToText(path):
    list_ = glob.glob(path + '/Score*.png')
    text = []
    path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    for element in list_:
        img = Image.open(element)
        pytesseract.tesseract_cmd = path_to_tesseract
        phr2 = pytesseract.image_to_string(img)
        phr2 = replaceError(phr2)
        text.append(phr2)
    return text

def rogne(path, tabtaille): 
    im = Image.open(path)
    player = 0
    for element in tabtaille:
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
        name = "Score/Score" + str(player)+ ".png"
            # Save Image
        area.save(name, "PNG")
        player +=1

def colorManagement(path):
    list_ = glob.glob(path + '/Score*.png')
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

    return path




#4v3

#rogner


path = "Score/photo1.png"
initialpath = "Score"
# tabTaille = [
#     [220,320,120,150],
#     [220,530,120,150]
# ]

tabTaille = [
    [220,320,120,400]
]

rogne(path, tabTaille)
print("image rognier")
colorManagement(initialpath)
print("image colorées")
text = imageToText(initialpath)
print("image tarduite : ")
print(text)
