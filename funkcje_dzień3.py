#zadanie 1
lista = []
lista.append(input("Podaj wartość 1 = "))
lista.append(input("Podaj wartość 2 = "))
lista.append(input("Podaj wartość 3 = "))
a = len(lista)
def lista_w_kwadratach(lista):
    if a>=3:
        print ("+","-"*7,"+","-"*7,"+","-"*7,"+")
        print("|",lista[0][:3],"...","|",lista[1][:3],"...","|",lista[2][:3],"...","|")
        print ("+","-"*7,"+","-"*7,"+","-"*7,"+")

lista_w_kwadratach(lista)

#zadanie 3
x = input("Podaj wysokość trójkąta: ")
def rysuj_trojkat(x):
    for i in range (1,x):
        print (i*"#")

rysuj_trojkat(x)

#zadanie 4
x = int(input("ludzkie lata "))
def psie_lata(x):
    if x <= 2:
        print("psie lata",x*10.5)
    else:
        print("psie lata",21.0+(x-2)*4)

psie_lata(x)