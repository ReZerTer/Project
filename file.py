from random import randint
import random
import os
import sys
zasady ='the rules are as follows: lets choose the positions where our ships will stand and alternately shoot on the board from A to I, from 9 to 1. 81 of the pool board, if any player manages to hit the ship, it shoots again. we place the ships horizontally or vertically, we can have them from 10 to 1 masts (number of grids occupied good luck'
lista=['a1','a2','a3','a4','a5','a6','a7','a8','a9','b1','b2','b3','b4','b5','b6','b7','b8','b9','c1','c2','c3','c4','c5','c6','c7','c8','c9','d1','d2','d3','d4','d5','d6','d7','d8','d9','e1','e2','e3','e4','e5','e6','e7','e8','e9','f1','f2','f3','f4','f5','f6','f7','f8','f9','g1','g2','g3','g4','g5','g6','g7','g8','g9','h1','h2','h3','h4','h5','h6','h7','h8','h9','i1','i2','i3','i4','i5','i6','i7','i8','i9',]
choicce = ['a1','a2','a3','a4','a5','a6','a7','a8','a9','b1','b2','b3','b4','b5','b6','b7','b8','b9','c1','c2','c3','c4','c5','c6','c7','c8','c9','d1','d2','d3','d4','d5','d6','d7','d8','d9','e1','e2','e3','e4','e5','e6','e7','e8','e9','f1','f2','f3','f4','f5','f6','f7','f8','f9','g1','g2','g3','g4','g5','g6','g7','g8','g9','h1','h2','h3','h4','h5','h6','h7','h8','h9','i1','i2','i3','i4','i5','i6','i7','i8','i9',]
def randomsheep(x):
    a=[]
    b=[]
    a.append(lista[randint(0,80)])
    b.append(randint(1,4))
    #drawing of places for the 4th masted
    shheps = []
    shheps.append(a[0])
    number = lista.index(a[0])
    if b[0]==1:
        if number<((x-1)*9):
            shheps.clear()
            shheps.append(a[0])
            number = lista.index(a[0])
            b[0]= 2       
        else:
            for i in range(x-1):
                number = number-9
                shheps.append(lista[number]) 
    if b[0]==2:
        letter1 = shheps[0]
        letter1 = letter1[1]
        letter1 = int(letter1)
        if letter1 >(10-x):
            shheps.clear()
            shheps.append(a[0])
            number = lista.index(a[0])
            b[0]= 3
        else:
            for i in range(x-1):
                number = number+1
                shheps.append(lista[number])
    if b[0]==3:
        letter1 = shheps[0]
        letter1 = letter1[1]
        letter1 = int(letter1)
        if letter1 <x:
            shheps.clear()
            shheps.append(a[0])
            number = lista.index(a[0])
            b[0]= 4
        else:
            for i in range(x-1):
                number = number-1
                shheps.append(lista[number])
    if b[0]==4:
        if number>(((10-x)*9)-1):
            shheps.clear()
            shheps.append(a[0])
            number = lista.index(a[0])
            b[0]= 0 
        else:
            for i in range(x-1):
                number = number+9
                shheps.append(lista[number])
    if b[0]==0:
        for i in range(x-1):
            number = number-9
            shheps.append(lista[number])
    return shheps


def losowanie():
    ilestatkow = []
    points = 20
    while points != 0:
        a= randint(1,9)
        if points-a <0:
            continue
        ilestatkow.append(a)
        points = points-a
    return ilestatkow


def podawanie():
    ilestatkow = []
    points = 20
    while points != 0:
        a = int(input())
        if points-a <0:
            print("Zla wartoscl przekroczyles 20 punktow")
            continue
        elif a > 9:
            print('najwikszy masztowic moze miec 9')
            continue
        ilestatkow.append(a)
        points = points-a
    return ilestatkow
def czyjestok(f):
    dlug = len(lista)
    for i in range(dlug):
        if lista[i] == f:
            return True
    return False

def szczytanieshepa(x):
    ile = len(x)
    liste = []
    todo = []
    print('podaj wartosc w notacji literacyfra np a7')
    for i in range(ile):
        while True:
            for w in range(x[i]):
                while True:
                    lo = input("wartosc: ")
                    if czyjestok(lo):
                        todo.append(lo)
                        break
                    else:
                        print('nniepraaawdlwa waartosc(musi byc z przedziaalu a1-i9 staatki stojace obok siebie)')
                        continue
            if czykolosiebie(todo):
                if czylista(liste, todo):
                    print('kolejny masztowiec')
                    liste.append(todo)
                    todo = []
                    break
                else:
                    print('podajesz warosci zarezerwowane dla juz istniejacego staku, podaj jeszcze raz dobrze')
                    todo = []
                    continue
            else:
                print('podane warosci nie stoja kolo siebie, podaj jeszcze raz dobrze')
    return liste

def czykolosiebie(statek):
    if czy_litera_taka_sama(statek, 0) or czy_litera_taka_sama(statek, 1):
        return True
    else:
        return False 
def czy_litera_taka_sama(lista, n):
    pierwsza_litera = None
    for element in lista:
        if pierwsza_litera is None:
            pierwsza_litera = element[n]
        elif element[n] != pierwsza_litera:
            return False
    return True

def czylista(list1, list2):
    for sub_list1 in list1:
        for element in sub_list1:
            for sub_list2 in list2:
                if element in sub_list2:
                    return False
    return True

def listewka(x, y):
    for sub_x in x:
        for element in sub_x:
            if element == y:
                return True
    return False

def mechnizmgry(czl, pc):
    strzeloneczl = []
    strzelonepc = []
    pudlopc = []

    def strzalpc():
        target = random.choice(choicce)
        choicce.remove(target)
        return target

    print('pdaj pole ktroe atakujesz w znanym systemie lub wybirz opcje gry od 1 do 5/ ? -wysietl opcje gry')
    while True:
        inpueat = input(':')
        if czyjestok(inpueat):
            if listewka(pc, inpueat):
                if czyjuzstrzelono(inpueat, strzelonepc):
                    print('trafony')
                    strzelonepc.append(inpueat)
                    if zattopiony(pc, strzelonepc, inpueat):
                        print('zatopiony')
                    if wygrana(strzelonepc):
                        print('grauluje wygrales')
                        break
                    continue
                else:
                    print('juz ustrzeliles to pole')
            else:
                print('pudlo')
                pudlopc.append(inpueat)
                while True:
                    stral = strzalpc()
                    print('komputer strzela: ' + stral)
                    if listewka(czl, stral):
                        print('trafiony')
                        strzeloneczl.append(stral)
                        if zattopiony(czl, strzeloneczl, stral):
                            print('zatopiony')
                        if wygrana(strzeloneczl):
                            print('computer wygral')
                            exit() 
                        continue
                    else:
                        break
                continue
            
        elif inpueat == '?':
            print('1 - wysiwtl zasady gry')
            print('2 - wyswietl moje pole')
            print('3 - wyswietl atakowane pole przeciwnika')
            print('4 - wyjdz z gry')
            print('5 - zresteuj gre')
        elif inpueat == '1':
            print(zasady)
        elif inpueat == '2':
            wyswietl_statki(lista, czl)
        elif inpueat == '3':
            print('pole przeciwnika -(nieznane), O-(pudlo), X-(traafione)')
            wyswietl_plansze(lista, strzelonepc, pudlopc)
        elif inpueat == '4':
            break
        elif inpueat == '5':
            reset_program()
        else:
            print('nieprawidlowa wartosc')

def reset_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)






def czyjuzstrzelono(x, y):
    for element in y:
        if element == x:
            return False
    return True
def what_elemnt(x, z):
    nie = 0
    for sub_x in x:
        for element in sub_x:
            if element  == z:
                return nie
        nie +=1

def czy_wszystkie_elementy(a, b):
    return all(element in b for element in a)

def zattopiony(x, y, z):
    ktury = what_elemnt(x, z)
    utpiony = x[ktury]
    return czy_wszystkie_elementy(utpiony, y)



def wygrana(y):
    dlug = len(y)
    if dlug == 20:
        return True
    else:
        return False
    
def wyswietl_plansze(pola, trafione, nietrafione):
    plansza = ''
    for pole in pola:
        if pole in trafione:
            plansza += ' X '
        elif pole in nietrafione:
            plansza += ' O '
        else:
            plansza += ' - '

        if pole.endswith('9'):
            plansza += '\n'

    print(plansza)


def scal_listy(listy):
    scalona_lista = []
    for lista in listy:
        scalona_lista.extend(lista)
    return scalona_lista

def wyswietl_statki(pola, trafione):
    trafione = scal_listy(trafione)
    plansza = ''
    for pole in pola:
        if pole in trafione:
            plansza += ' S '
        else:
            plansza += ' - '

        if pole.endswith('9'):
            plansza += '\n'

    print(plansza)
