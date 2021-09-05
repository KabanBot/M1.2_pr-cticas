nombre= input("Entra Tu frase: ")
frase=(nombre.replace("Y","")).split()
acronimo=""
for word in frase: acronimo=acronimo + word[0].upper()
print("Su Acronimo es: ",acronimo)