cuenta=float(input("De cuanto es la cuenta: "))
print("Seleccione un numero")
total=0
propina=int(input("Cuanto propina quiere dar 1:18% 2:20% 3:25% : "))
if propina==1: 
    total=cuenta*.18 
    print("El total de la propina es: ")
    print(total) 
    print("El total a pagar es: ")
    
elif propina==2:
    total=cuenta*.20
    print("El total de la propina es: ")
    print(total) 
    print("El total a pagar es: ")

elif propina==3:
    total=cuenta*.25
    print("El total de la propina es: ")
    print(total) 
    print("El total a pagar es: ")
  
totalc=total+cuenta   
print("Su total es de: ","$ ",totalc)

personas=int(input("Cuantas personas son maximo 4: "))

if personas >4: print("No se puede de mas la mesa nada mas tiene 4 sillas")
elif personas==1: 
    print("Solo en decimas")
    Cliente1= float(input('Yo voy a pagar el: '))
    tot1 = totalc * Cliente1
    print ('Factura total: $',totalc)
    print('Pago cliente 1: ',Cliente1*100,'%', ' Pago: $',tot1)
    
elif personas==2: 
    print("Solo en decimas")
    Cliente1= float(input('Yo voy a pagar el: '))
    tot1 = totalc * Cliente1
    Cliente2= float(input('Yo voy a pagar el: '))
    tot2 = totalc * Cliente2
    print ('Factura total: $',totalc)
    print('Pago cliente 1: ',Cliente1*100,'%', ' Pago: $',tot1)
    print('Pago cliente 2: ',Cliente2*100,'%', ' pago: $',tot2)
    
elif personas==3: 
    print("Solo en decimas")
    Cliente1= float(input('Yo voy a pagar el: '))
    tot1 = totalc * Cliente1
    Cliente2= float(input('Yo voy a pagar el: '))
    tot2 = totalc * Cliente2
    Cliente3= float(input('Yo voy a pagar el: '))
    tot3 = totalc * Cliente3
    print ('Factura total: $',totalc)
    print('Pago cliente 1: ',Cliente1*100,'%', ' Pago: $',tot1)
    print('Pago cliente 2: ',Cliente2*100,'%', ' pago: $',tot2)
    print('Pago cliente 3: ',Cliente3*100,'%', ' pago: $',tot3)
    
elif personas==4: 
    print("Solo en decimas")
    Cliente1= float(input('Yo voy a pagar el: '))
    tot1 = totalc * Cliente1
    Cliente2= float(input('Yo voy a pagar el: '))
    tot2 = totalc * Cliente2
    Cliente3= float(input('Yo voy a pagar el: '))
    tot3 = totalc * Cliente3
    Cliente4= float(input('Yo voy a pagar el: '))
    tot4 = totalc * Cliente4
    print ('Factura total: $',totalc)
    print('Pago cliente 1: ',Cliente1*100,'%', ' Pago: $',tot1)
    print('Pago cliente 2: ',Cliente2*100,'%', ' pago: $',tot2)
    print('Pago cliente 3: ',Cliente3*100,'%', ' pago: $',tot3)
    print('Pago cliente 4: ',Cliente4*100,'%', ' pago: $',tot4)

