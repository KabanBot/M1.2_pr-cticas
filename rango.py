import random
numero=random.randrange(1,50)
x= int(input("Dame un numero del 1 al 50: "))
print(numero)  
while x != numero:  
    if x>50 or x<0:print("No mijo Solo los numeros dentro del rango")
    elif x<numero: x = int(input("Mas pa arriba Dame un numero del 1 al 50: "))
    elif x>numero: x = int(input("Mas pabajo Dame un numero del 1 al 50: "))
else:print("Felicidades vro eres el campeon congratulaciones")
