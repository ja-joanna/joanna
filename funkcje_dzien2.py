#zadanie 1
def C_to_F(tempC):
    tempF = (float(tempC)*1.8) + 32
    return tempF
wynik = C_to_F(input("stopnie Celcjusza: "))
print(wynik)


#zadanie 2
def F_to_C(tempF):
    tempC = (float(tempF)-32)/1.8
    return tempC
wynik = F_to_C(input("stopnie Fahrenheita: "))
print(wynik)



#zadanie 3
import math
def pole_kola(r):
    P = math.pi*(float(r)**2)
    return P
wynik = pole_kola(input("promień: "))
print(wynik)

#zadanie 4
def ktora_cyfra(liczba):
    pierwsza_cyfra = str(liczba)[0]
    ostatnia_cyfra = str(liczba)[-1:]
    return "pierwsza cyfra = ",pierwsza_cyfra, "ostatnia cyfra = ", ostatnia_cyfra
wynik = ktora_cyfra(input("Podaj liczbę = "))
print(wynik)



#zadanie 5
def square_shape(leng,width):
        print ("+","- "*leng,"+")
        for _ in range(width-2):
            print ("| ","  "*leng,"|")
        print ("+","- "*leng,"+")
square_shape(int(input("długość: ")), int(input("szerokość: ")))


#zadanie 6
def bin_to_dec(bin):
    dec = int(bin, 2)
    return dec
wynik = bin_to_dec(str(input("Podaj liczbę = ")))
print("decimal = ", wynik)


#zadanie 7
def sprawdz_czy_parzysta(liczba)
    if (float(liczba) % 2 == 0):
        print("liczba parzysta")
    else:
        print("liczba nieparzysta")


#zadanie 8
def podzielna_1(liczba)
    if (float(liczba) % 3 == 0 or float(liczba) % 5 == 0 or float(liczba) % 7 == 0 ):
        print("liczba podzielna przez 3 lub 5 lub 7")
    else:
        print("liczba niepodzielna przez 3 lub 5 lub 7")


def podzielna_2(liczba)
    if (float(liczba) % 3 == 0 and float(liczba) % 5 == 0 and float(liczba) % 7 == 0 ):
        print("liczba podzielna przez 3, 5 i 7")
    else:
        print("liczba niepodzielna przez 3, 5 i 7")


#zadanie 9
def podzielna_3(liczba)
    if (float(liczba) % 3 == 0):
        print("liczba podzielna przez 3")
    elif (float(liczba) % 5 == 0):
        print ("liczba podzielna przez 5")
    else:
        print("liczba niepodzielna przez 3 i 5")

#zadanie 10
data=input("Podaj rok: ")
def rok_przestepny(data):
    if(int(data) % 4 == 0 and int(data) % 100 != 0 or int(data) % 400 == 0):
        print("rok przestępny")
    else:
        print("rok zwykły")
rok_przestepny(data)




