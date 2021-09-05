import random
list1 = random.randrange(1,3)
print ("Bienvenido, vamos a jugar a Piedra, papel o tijera.")
print ("Eligue tu tirada")
x = int( input(" 1. Piedra  2.Papel  3.Tijera: "))
print("Eleccion de la pc")
print(list1)
if x==1 and list1==1: 
    print("Es un empate")
elif x==1 and list1==2: 
    print("La Computadora gana")
elif x==1 and list1==3: 
    print("Tu Ganas")
elif x==2 and list1==2: 
    print("Es un empate")
elif x==2 and list1==3: 
    print("La Computadora gana")
elif x==2 and list1==1: 
    print("Tu Ganas")
elif x==3 and list1==3: 
    print("Es un empate")
elif x==3 and list1==1: 
    print("La Computadora gana")
elif x==3 and list1==2: 
    print("Tu Ganas")