def convertidor():
    palabra = input("Coloca tu palabra aqui mero: ") 
    palabramin = palabra.lower() 
    lista = list(palabramin) 
    return lista

def quitarcaracter(quitar): 
    exepcion = [" ", "-", ".", ",", ":", ";", "!", "?", "'", "\""] 
    for caracter in exepcion: 
        if caracter in quitar: 
            quitar.remove(caracter) 
            return quitarcaracter(quitar)
    return quitar 

def checar(lista):
    alrvez= lista[::-1] 
    if alrvez == lista: 
        return "Si es palindromo" 
    else: 
        return "No es palindromo" 

def main(): 
    original = convertidor()  
    original = quitarcaracter(original) 
    verificar = checar(original)
    print(verificar)

main() 