from file import *
def start():
    return
print('Lets play some sheeps game')
print(zasady)
print('You have 20 points at your disposal. You can use 1 for each mast')
while True:
    what = input('chcesz losowac jakie masz statki (1) czy wybrac samemu (2) ')
    if what == '1' or what == '2':
        if int(what) == 1:
            sheep = losowanie()
            print('wyloswoales statki o masztach:')
            print(sheep)

        elif int(what) == 2:
            sheep = podawanie()
        break
    else:
        print('nieprawidlowa wartosc')



lista = []
while True:
    what = input('chesz aby poozycje statkow wyloswal komputer 1 czy chesz wybrac je sam 2: ')
    if what == '1' or what == '2':
        if int(what) == 1:
            for i in sheep:
                while True:
                    zed = randomsheep(i)
                    if czylista(lista, zed):
                        lista.append(zed)
                        break
                    else:
                        continue
        elif int(what) == 2:
            lista = szczytanieshepa(sheep)
        break
    else:
        print('nieprawidlowa wartosc')


#losowania komputra 
listacompa = []
sheepcompaa = losowanie()
for i in sheepcompaa:
        while True:
            zed = randomsheep(i)
            if czylista(listacompa, zed):
                listacompa.append(zed)
                break
            else:
                continue


mechnizmgry(lista, listacompa)