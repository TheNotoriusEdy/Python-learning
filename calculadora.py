print ("Bienvenido a la calculadora con Match Case.")
num1=int(input("Ingresa el número 1: "))
num2=int(input("Ingresa el número 2: "))
print ("¿Que desea realizar?")
print ("1-Suma")
print ("2-Resta")
print ("3-Multiplicación")
print ("4-División")
opcion=int(input("Ingresa la opción a realizar: "))
match opcion:
    case 1:
        suma=num1+num2
        print (f"{num1} + {num2} = {suma}")
    case 2:
        resta=num1-num2
        print (f"{num1} - {num2} = {resta}")
    case 3: 
        multi=num1*num2
        print (f"{num1} x {num2} = {multi}")
    case 4:
        divi=num1//num2
        print (f"{num1} / {num2} = {divi}")
    case _:
        print ("ERROR. Ingrese una opción valida del 1-4.")