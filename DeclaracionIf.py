#IF STATEMENT:Programar aveces implica revisar una serie de condiciones y decidir que acción tomar
#dependiendo de esas condiciones


billetes = ['veinte','cincuenta','cien','docientos','quinientos','mil']
for billete in billetes:
    if billete == 'cincuenta':    #Si el valor es el que le pido 
        print(billete.upper())    #Hara esto
    else:                         #de lo contrario 
        print(billete.title())    #hace esto

#Conditional Test:es una expresión que puede ser evaluada como True o False así se decide cuando se 
#debe ejecutar el código de la declaración if, si es True se ejecuta lo que diga el if, si es False
#ignora el codigo que indica la declaración if.

#Checking for Equality:cuando el valor de una variable es igual al valor de interes.

billetes = 'veinte'    #establece el valor de billetes a 'veinte'
billetes == 'veinte'   #¿Es el valor de billetes igual a 'veinte'

#La evaluación de igualdad es sensible a minimos cambios

billete = 'mil'
billete == 'Mil'

billete= 'Cien'
billete.lower() == 'cien'  #aplicar el metodo no cambia el valor de la variable solo compara 

#Revisando inigualdad: cuando se quiere saber cuando dos valores NO son iguales se usa ! not.

sabor_pedido = 'hongos'

if sabor_pedido != ' peperoni':    #Compara el valor de 'peperoni' con 'hongos'
    print('Aguanta los hongos!')   #Si el valor NO es igual ejecuta esto 

#Numerical comparisons:

edad = 27
edad == 28

#También se puede ver si no son iguales

respuesta = 28
if respuesta != 45: #si respuesta NO es 28 entonces
    print('Esa no es la respuesta correcta.Intenta de nuevo!') #Como 28 != 45 es cierto y se ejecuta

#Se pueden hacer otras comparaciones como mayor que,menor que, mayor o igual que.

edad = 35
edad > 27 #Mayor que 
edad < 27 #Menor que 
edad >= 27 #Mayor igual que 
edad <= 27 #Menor igual que 

#Cada comparacion matematica puede usarse en una declaración if así detectas
#condiciones de interes

#Checking Multiple conditions:Las keywords pueden ayudar a revisar cuando una condición se cumple 
# una u otra no, o cuando ambas son ciertas.

edad_0 = 22
edad_1= 19
edad_0 >= 21 and edad_1 >= 21 #Como no se cumplen las dos condiciones resulta en false
edad_1 =23
(edad_0 >=21) and (edad_1 >= 21) #Los parentesis solo ayudadn a leer mejor el código

#Using or to check multiple conditions: ya sea que ambas o el test individual pase.
#False si ambas no se cumplen

edad_0 = 22
edad_1 = 18
edad_0 >= 21 or edad_1 >= 21 #Solo se cumple 22 > 21 (edad_0 >= 21)

edad_0 = 18
edad_0 >= 21 or edad_1 >= 21  #Aquí ninguna de las dos se cumple 

#Cheking wheter a value is In a list: es importante revisar si el valor esta en la lista 

sabores_pedidos = ['hongos','peperoni','hawaiana','carnes']
'hongos' in sabores_pedidos

'mexicana' in sabores_pedidos #Así se puede saber que valores estan en la lista

#Cheking wheter a value is Not in a List: aveces es importante saber que valores NO estan 

usuarios_baneados = ['Alejandra','Federico','Estefania','Alma']
usuario = 'Maria'

if usuario not in usuarios_baneados:                            #Si no esta 
    print(usuario.title() + ',a esta persona si le puedo hablar.') #Haz esto

#BOOLEAN EXPRESSIONS:es otro nombre para un test condicional un valor boolean es True o False
#Son para llevarles la pista a ciertas condiciones.

juego_activo = True
puede_editar = False

#Proveen una forma eficiente de rastrear el esstado de un programa o condición particular.

#If Statements :decides cual usar segun el numero de condiciones que necesites.
#Simple if statements: la declaracion if más simple tiene un test y una accion.
#    if test_condicional:
#        haz algo

edad = 18
if edad >= 18:
    print('Eres apto para votar!')
    print('Ya sacaste tu credencial?')  #Se puede hacer lo mismo que en un for loop

#If-else statements:a menudo se querra hacer una accion cuando un test condicional pasa y otra en 
#los demas casos.La declaracion else permite definir una acción o conjunto de acciones que son 
#ejecutadas cuando el test falla

edad = 18
if edad <= 17:                          #aquí hace el test
    print('Puedes votar')
    print('Haz registrado tu voto?')
else:                                   #si no pasa el test hace esto
    print('Lo siento, no eres apto para votar')
    print('Por favor registra tu voto cuando cumplas 18!')

#The if-elif-else Chain: seguido revisaras mas de dos posibles situaciones

edad =11
if edad < 4:
    print('Tu admisión cuesta $0 (es gratis!)')
elif  edad < 18:
    print('Tu admisión cuesta $100')
else:
    print('Tu pagas $200')

    #Para hacer el codigo más conciso se añade el precio dentro de la cadena
edad = 18
if edad < 4:
    price = 0    #Así es más fácil cambiar los valores 
elif edad < 18:
    price = 100
else:
    price = 200
print('Tu admisión cuesta $' + str(price) + ".")      #solo cambiamos esto

#Using Multiple elif Blocks: se pueden usar tantas condicionales elif 

edad = 18
if edad < 4:
    price = 0       #Así es más fácil cambiar los valores 
elif edad < 18:
    price = 100
elif edad < 65:
    price = 50
else:
    price = 200
print('Tu admisión cuesta $' + str(price) + ".")    #solo cambiamos esto 

#Testing multiple conditions: La cadena if-elif-else es apropiada cuando 
#necesitamos que un test de una condicion especifica se cumpla e ignore los demás
#Sin embargo para revisar todas las condiciones de interes.Esta tecnica sirve
#para cuando una condición pueda ser True.

sabor_pedido = ['hongos','extra queso']

if 'hongos' in sabor_pedido:
    print('Añade hongos.')

if 'pepperoni' in sabor_pedido:
    print('Añade pepperoni.')

if 'extra queso' in sabor_pedido:
    print('Añade extra queso.')
        
print( "\nAcabamos de hacer tu pizza!")    

#Using if statement with list: Se pueden ver valores especiales que necesitan
#ser tratados diferente que otros valores en la lista.

     #Si se acabaron los pimientos

sabores_disponibles = ['hongos','pimiento','queso extra']

for sabor_pedido in sabores_disponibles:
    if sabor_pedido == 'pimiento':
        print('Lo sentimos, no tenemos pimientos por el momento.')
    else:
        print('Añade ' + sabor_pedido + '.')
    
print('\nAcabamos tu pizza!')

#Cheking that a list is not empty:Se manda un mensaje de aviso si queda vacia

sabores_pedidos = []

if sabores_pedidos:
    for sabor_pedido in sabores_pedidos:
        print( 'Añade'+ sabor_pedido +'.')
    print('\nAcabamos y tu pizza')  
else:
    print('Seguro que quieres una pizza simple?')
    
#Usando multiples listas:Cuando alguien pide algo que no hay 

sabores_disponibles = ['hongos','olivos','pimientos','pepperoni','hawaiana']

sabores_pedidos = ['hongos','papas fritas','extra queso']

for sabor_pedido in sabores_pedidos:
    if sabor_pedido in sabores_disponibles:  #Si esta lo añades
        print('Añade ' + sabor_pedido +'.')   
    else:                                    #Para lo demás haz esto 
        print('Lo sentimos,no tenemos ' + sabor_pedido + '.')
    
print('\nAcabamos de hacer tu pizza!')
    