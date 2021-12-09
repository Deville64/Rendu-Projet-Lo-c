#Exercice 1

def display(a , b):
    a = round(a)
    b = round(b)
    string = ""

    while a < b:
        a+=1
        if a%2 == 1:
            string = string + str(a) + " "

    print(string)

#display( 1, 8)


#Exercice 2

def game(x, y):
    import random

    computer = random.randint(x, y)
    count = 0
    test = False
    x = int(input("Devine un nombre : "))

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


#Exercice 6

def pascal(row):
    pascal = [[1],[1,1]]
    print(pascal[0])
    print(pascal[1])
    
    for i in range(2,row):
        pascal.append([1])
        for j in range(1, i):
            pascal[i].append(pascal[i-1][j-1] + pascal[i-1][j])
        pascal[i].append(1)
        print(pascal[i])

    print(f'Le max de la ligne {row} est {max(pascal[-1])}')

#pascal(9)


#Exercice 7

def translate(mot):
    word = {"souris": "mouse", "ordinateur": "computer", "miel": "honey"}
    for key, value in word.items():
        if mot == key:
            return print(value)
        elif mot == value:
            return print(key)

#translate("ordinateur")


#Exercice 8
def text():
    title = "test"
    f =open( title + ".txt", "x")
    


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
    f =open( "school_work.txt", "x")

    for i in range(2,31):
        count = 1
        while count < 21:
            if count == 20:
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

def triple_space(old_file, new_file, old, new):
    file = open(old_file + ".txt", "r+")
    f =open( new_file + ".txt", "x")
    txt = file.readlines()
    sentence = ''

    for line in txt:
        count = 0
        while(count < len(line)):
                if line[count] == old:
                    sentence += new
                else:
                    sentence += line[count]
                count += 1
                
        line = sentence
        f.seek(0)
        f.writelines(line)
            
    file.close()
    f.close()

#triple_space("test", "copie", " ", "   ")

def mix_lines(file_a, file_b, new_file):
    file = open(new_file + ".txt", "x")
    f_a = open(file_a + ".txt", "r+")
    f_b = open(file_b + ".txt", "r+")
    sentence = ''

    txt_a = f_a.readlines()
    txt_b = f_b.readlines()

    count = 0
    while count < len(txt_a):
        if count%2 == 0:  
            sentence += txt_a[count]
            count+=1
        elif count%2 == 1:
            sentence+= txt_b[count]
            count+=1

    print(sentence)
    file.writelines(sentence)
    file.close()
    f_a.close()
    f_b.close()

#mix_lines("exo8_a", "exo8_b", "fichier_c")


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

def create_big_brother(data):
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

    send = data.update(dico)
    return send
        
def read_big_brother(dico):
    name = input("Quel personne cherchez-vous ? : ")
    print(f"Nom : {str(name)} - âge : {dico[str(name)]['age']} ans - sexe : {dico[str(name)]['taille']}m")


def save_big_brother(dico):
    file = open("big_brother.txt", "x")
    sentence = ''

    for i in dico:
        sentence += i + ": \n" + '    Age: ' + dico[i]['age'] + '\n' + '    Sexe: ' + dico[i]['sexe'] + '\n' + '    Taille: ' + dico[i]['taille'] + '\n'
    
    file.writelines(sentence)
    file.close()
    print("Fichier enregistré")

def big_brother(data):
    x = input("Désirez-vous chercher quelqu'un ? [y/n]")
    if x == "y":
        read_big_brother(data)
    x = input("Désirez-vous ficher des personnes ? [y/n]")
    if x == "y":
        create_big_brother(data)
    x = input("Voulez-vous enregistrer les data ? [y/n]")
    if x == "y":
        save_big_brother(data)


test_dico = {'loic': {'age': '27', 'sexe': 'M', 'taille': '1.9'}, 'paul': {'age': '20', 'sexe': 'M', 'taille': '1.7'}, 'solene': {'age': '30', 'sexe': 'F', 'taille': '1.55'}}

#big_brother(test_dico)