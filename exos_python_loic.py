#Exercice 1

def display(a , b):
    a = round(a)
    b = round(b)

    while a < b:
        a+=1
        print(a)

#display( 1, 5)


#Exercice 2

def game(x, y):
    import random

    computer = random.randint(x, y)
    count = 0
    test = False
    x = int(input())

    if  x > 100:
        print('Tu as choisi un chiffre plus grand que 100')
    elif x < 0 :
        print('Tu as choisi un chiffre plus petit que 0')
    else:
        while test == False:
            if computer<x:
                print('Trop grand !')
                count+=1
                x = int(input())
            elif computer>x:
                print('Trop petit !')
                count+=1
                x = int(input())
            elif computer == x:
                print(f'Bien joué ! Cela vous à pris {count} essais')
                test = True

#game(0, 100)


#Exercice 3

def biggest(size, extract):
    import random
    list = []
    count_size = 0
    count_extract = 0
    biggest = []

    while count_size < size:
        nb = random.randint(0, 100)
        list.append(nb)
        count_size+=1

    while count_extract < extract:
        nb = max(list)
        list.remove(nb)
        biggest.append(nb)
        count_extract+=1

    print(biggest)

#biggest(100, 10)


#Exercice 4
test = [1, 2, 9, 4, 58, 98, 3]

def custom_sort(list):
    size = len(list)
    new_list = []
    count = 0
    
    while count < size:
        biggest = 0
        for nb in list:
            if nb > biggest :
                biggest = nb

        list.remove(biggest)
        new_list.append(biggest)
        count+=1

    print(new_list)

#custom_sort(test)

#Exercice 5
x = 3430061596791935255

def convert_time(seconds):
    year = seconds // (12*30.5*24*60*60)
    seconds %= (12*30.5*24*60*60)
    month = seconds // (30.5*24*60*60)
    seconds %= (30.5*24*60*60)
    days = seconds // (24*60*60)
    seconds %= (24*60*60)
    hour = seconds // (60*60)
    seconds %= (60*60)
    minutes = seconds // 60
    seconds %= 60
      
    print(f" {x} correspondent à : {round(year)} années {round(month)} mois {round(days)} jours {round(hour)} heures {round(minutes)} minutes {round(seconds)} secondes")
      
#convert_time(x)

def convert_distance(miles):
    km= miles*1.609
    ms= km/3.6
    print(f"La vitesse est de {round(km, 2)} km/h ou {round(ms,2)} m/s")

#convert_distance(121)

#Exercice 7
word = {"souris": "mouse", "ordinateur": "computer", "miel": "honey"}

def translate(mot):
    for key, value in word.items():
        if mot == key:
            return print(value)
        elif mot == value:
            return print(key)

#translate("computer")

#Exercice 8
def text():
    print("Donner un nom à votre fichier")
    x = input()
    title = x
    f =open( x + ".txt", "x")
    


    print("Ecrivez votre texte")
    f = open(title + ".txt", "w")
        
    empty = False
    while empty == False:
        x= input()
        f.write(x + '\n')
        f.close

        if x == '':
            empty = True
    
    print("voulez vous Afficher le contenu ? [y/n]")
    x = input()
    if x == "y":
        f = open(title + ".txt", "r")
        return print(f.read())

#text()

def school_work():
    print("Donner un nom à votre fichier")
    x = input()
    title = x
    f =open( x + ".txt", "x")

    for i in range(2,31):
        count = 1
        while count < 21:
            if count == 10:
                result = i*count
                text = f"{i}x{count}={result} \n"

                f.write(text + '\n')
                f.close
                count+=1
            else:
                result = i*count
                text = f"{i}x{count}={result} \n"

                f.write(text)
                f.close
                count+=1

#school_work()

#Exercice 9

def note():
    dico = {}
    empty_key = False
    count_note = 0
    max_note = 0
    lowest_note = 20
    total = 0

    while empty_key == False:
        key = input('Entrer le nom : ')

        if key == '':
            empty_key = True
            break

        value = input('Entrer la note : ')
        dico[key] = value

        if max_note < int(value):
            max_note = int(value)
        if lowest_note > int(value) :
            lowest_note = int(value)

        total += int(value)
        count_note+=1
        print(f"Vous avez enregistré {count_note} notes")
        

    print(dico)
    print(f"La meilleur note est de  {max_note}")
    print(f"La moins bonne note est de  {lowest_note}")
    print(f"La moyenne est de {total/count_note}")

#note()

#Exercice 10

def create_big_brother():
    dico = {}
            
    empty = False
    while empty == False:
        name= input("Nom : ")
        if name == '':
            empty = True
            break
        dico[name] = {}

        age= input("Age : ") 
        dico[name]["age"] = age

        sex= input("Sexe [F/M] : ") 
        dico[name]["sexe"] = sex

        size= input("Taille : ") 
        dico[name]["taille"] = size

    send = dico
    return send
        
def read_big_brother(dico):
    name = input("Quel personne cherchez-vous ? : ")
    print(f"Nom : {str(name)} - âge : {dico[str(name)]['age']} ans - sexe : {dico[str(name)]['taille']}m")

#read_big_brother(create_big_brother())

