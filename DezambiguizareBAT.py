# Se dau doua fisiere ce contin text explicativ pentru un sens al cuvantului ambiguu cu ajutorul carora se determina sensul cuvantului "bat" din propozitia utilizatorului.


import nltk
import codecs
from nltk.tokenize import PunktSentenceTokenizer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer
from nltk.corpus import wordnet
from tkinter import *
from PIL import ImageTk, Image

root = Tk()

# 1.Se sterg StopWords
# 2.Stemming
# 3.Se fac tokenuri

def Stem_Lem(propozitie):

    propozitie_filtrata = []
    lematizez = WordNetLemmatizer()
    stematizez = PorterStemmer()

    StopWords = set(stopwords.words("english"))
    cuvinte = word_tokenize(propozitie)

    for cuvant in cuvinte:
        if cuvant not in StopWords and cuvant != "bat" and cuvant != "Bat" and cuvant != "bats" and cuvant != "Bats":
            propozitie_filtrata.append(lematizez.lemmatize(stematizez.stem(cuvant)))
            for i in Creare_Sinonime(cuvant):
                propozitie_filtrata.append(i)
    return propozitie_filtrata

# Adaugam sinonime

def Creare_Sinonime(cuvant):
    sinonime = []

    for sinonim in wordnet.synsets(cuvant):
        for i in sinonim.lemmas():
            sinonime.append(i.name())

    return sinonime

# Verificam similaritatea cuvintelor

def Verificare_Similaritate(cuvant1, cuvant2):

    cuvant1 = cuvant1 + ".n.01"
    cuvant2 = cuvant2 + ".n.01"
    try:
        cuvant1 = wordnet.synset(cuvant1)
        cuvant2 = wordnet.synset(cuvant2)

        return cuvant1.wup_similarity(cuvant2)

    except:
        return 0

def Filtru(propozitie):

    propozitie_filtrata = []
    lematizez = WordNetLemmatizer()
    StopWords = set(stopwords.words("english"))
    cuvinte = word_tokenize(propozitie)

    for cuvant in cuvinte:
        if cuvant not in StopWords and cuvant != "bat" and cuvant != "Bat" and cuvant != "bats" and cuvant != "Bats":
            propozitie_filtrata.append(lematizez.lemmatize(cuvant))
    return propozitie_filtrata

def Actionare_Buton_1():

    Animal_txt = codecs.open("Animal.txt", 'r', 'utf-8')
    propozitie1 = Animal_txt.read().lower()
    Obiect_txt = codecs.open("Obiect.txt", 'r', "utf-8")
    propozitie2 = Obiect_txt.read().lower()

    propozitie3 = textBox_1.get().lower()

    propozitie_filtrata1 = []
    propozitie_filtrata2 = []
    propozitie_filtrata3 = []

    count1 = 0;
    count2 = 0;
    similaritate_propozitii31 = 0
    similaritate_propozitii32 = 0

    propozitie_filtrata1 = Filtru(propozitie1)
    propozitie_filtrata2 = Filtru(propozitie2)
    propozitie_filtrata3 = Filtru(propozitie3)

    textBox_3.config(state="normal")
    textBox_3.delete(0, 'end')
    textBox_3.insert(0, "Tokenii: ")
    textBox_3.insert(9, propozitie_filtrata3)
    textBox_3.config(state="disabled")

    for i in propozitie_filtrata3:
        for j in propozitie_filtrata1:
            count1 = count1 + 1
            similaritate_propozitii31 = similaritate_propozitii31 + Verificare_Similaritate(i, j)

        for j in propozitie_filtrata2:
            count2 = count2 + 1
            similaritate_propozitii32 = similaritate_propozitii32 + Verificare_Similaritate(i, j)

    propozitie_filtrata1 = []
    propozitie_filtrata2 = []
    propozitie_filtrata3 = []

    propozitie_filtrata1 = Stem_Lem(propozitie1)
    propozitie_filtrata2 = Stem_Lem(propozitie2)
    propozitie_filtrata3 = Stem_Lem(propozitie3)

    textBox_4.config(state="normal")
    textBox_4.delete('1.0', END)
    textBox_4.insert(INSERT, "Leme si sinonime: " + "\n" + "\n")
    textBox_4.insert(INSERT, propozitie_filtrata3)
    textBox_4.config(state="disabled")

    prop1_count = 0
    prop2_count = 0

    for i in propozitie_filtrata3:

        for j in propozitie_filtrata1:
            if(i == j):
                prop1_count = prop1_count + 1

        for j in propozitie_filtrata2:
            if(i == j):
                prop2_count = prop2_count + 1

    textBox_5.config(state="normal")
    textBox_5.delete('1.0', END)
    textBox_5.insert(INSERT, "Scor similaritate Animal = " + str(similaritate_propozitii31) + "\n" + "Scor similaritate Obiect = " + str(similaritate_propozitii32))
    textBox_5.config(state="disabled")

    textBox_6.config(state="normal")
    textBox_6.delete('1.0', END)
    textBox_6.insert(INSERT, "Nr cuvinet gasite in fisierul Animal = " + str(prop1_count) + "\n" + "Nr cuvinte gasite in fisierul Obiect = " + str(prop2_count))
    textBox_6.config(state="disabled")

    if((prop1_count + similaritate_propozitii31) > (prop2_count + similaritate_propozitii32)):
        textBox_2.config(state="normal")
        textBox_2.delete(0, 'end')
        textBox_2.insert(0,"Animal")
        textBox_2.config(state="disabled")
    else:
        textBox_2.config(state="normal")
        textBox_2.delete(0, 'end')
        textBox_2.insert(0,"Obiect")
        textBox_2.config(state="disabled")

    #print ("\nGATA")


#Interfata Grafica GUI

root.title('Dezambiguizarea cuvantului "Bat"')

#Propozitia de dezambiguizat
textBox_1 = Entry(root, width=30, font = "Arial 44 bold",justify="center",bg="#262626",fg="#ff9300",disabledbackground="#262626",disabledforeground="#ff9300",highlightcolor="#ff9300",highlightthickness=3,bd=0)
textBox_1.grid(row=0,column = 0)
textBox_1.grid(columnspan=2)

#Buton Dezambiguizare
buton_1 = Button(root, text="Incepe Dezambiguizarea", command=Actionare_Buton_1, width=20, font = "Times 20 bold",justify="center",bg="#262626",fg="#ff9300",disabledforeground="#262626",highlightbackground="#262626",highlightcolor="#262626",highlightthickness=5,bd=0,activebackground="#262626",activeforeground="red")
buton_1.grid(row=1,column = 0)
buton_1.grid(columnspan=2)

#Rezultatul - Sensul corect - Animal/Obiect
textBox_2 = Entry(root, width=8, font = "Arial 44 bold",justify="center",bg="#262626",fg="#ff9300",disabledbackground="#262626",disabledforeground="#ff9300",highlightcolor="#ff9300",highlightthickness=3,bd=0)
textBox_2.grid(row=2,column=0)
textBox_2.config(state="disabled")

#Imagine rezultat
path = "Animal-Obiect.jpg"
img = ImageTk.PhotoImage(Image.open(path))
panel = Label(root,image = img)
panel.grid(row=3,column=0)

#Prop filtrata
textBox_3 = Entry(root, width=33, font = "Arial 20 bold",justify="center",bg="#262626",fg="#ff9300",disabledbackground="#262626",disabledforeground="#ff9300",highlightcolor="#ff9300",highlightthickness=3,bd=0)
textBox_3.grid(row=2,column=1)
textBox_3.config(state="disabled")

#Prop Stem_Lem
textBox_4 = Text(root, height = 10, width = 45, font = "Arial 15 bold",bg="#262626",fg="#ff9300",highlightcolor="#ff9300",highlightthickness=3,bd=0)
textBox_4.grid(row=3,column=1)
textBox_4.config(state="disabled")

#Scor similaritate
textBox_5 = Text(root, height = 2, width = 45, font = "Arial 15 bold",bg="#262626",fg="#ff9300",highlightcolor="#ff9300",highlightthickness=3,bd=0)
textBox_5.grid(row=4,column=0)
textBox_5.config(state="disabled")

#Nr cuv gasite
textBox_6 = Text(root, height = 2, width = 45, font = "Arial 15 bold",bg="#262626",fg="#ff9300",highlightcolor="#ff9300",highlightthickness=3,bd=0)
textBox_6.grid(row=4,column=1)
textBox_6.config(state="disabled")

#spatiu
spatiu = Label(root, height = 1, width = 50)
spatiu.grid(row=5)
spatiu.grid(columnspan=2)

root.mainloop()