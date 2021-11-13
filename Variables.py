#Este es un resumen de lo que son las variables y tipos de datos.

print("Hello Python World!")

#Variable almacena un valor 

message = "Hello Python World!"
print(message)

message = "Hello Python Crash Course world!"
print(message)

#Reglas de las variables: contienen solo letras, numeros y lineas bajas no pueden empezar con un número.
#Ejemplo: message_1 -- bien     1_message -- mal
#Los espacios no estan permitidos greeting message (error)
#Evita usar palabras clave de python como nombre de funciones o variables
#Los nombres de las variables deben ser cortos pero descriptivos: name es mejor que  n , student_name mejor que s_n
#Cuidado usando l y O se confunde con 1 y 0

#Common errors: omitir una sola letra causa 

#       message = "Hello Python Crash Course world!"
#       print(mesage)  

#Cuando se define y llama a la variable correctamente no dan errores
mesage = "Hola mundo de Python"
print(mesage)

x , libro = 100 , "The rise of Kyoshi"
print(x, libro)

#Convenciones

nombre_libro = "The Shadow of Kyoshi" #Snake case (subguion)
nombrelibro = "Python Crash Course"  #Camel Case
NombreLibro = "assadasdas" #Pascal Case

PI = 3.1416          #Mayusculas son constantes
MY_NAME = "Bernardo"

#EJERCICIOS:2.1 MENSAJE SIMPLE 
mensaje = "Hola que hace aprendiendo a programar o que hace"
print(mensaje)

#2.2 MENSAJES SIMPLES : se le cambia el valor a la variable
oracion = "Esto es muy divertido de aprender"
print(oracion)

oracion = "Aunque hay cosas aun mas divertidas por hacer"
print(oracion)

#STRINGS es una serie de caracteres.Cualquier cosa dentro de comillas se considera un string y puedes usar '' o ""

"this is a string."
'this is also a string.'

'Le dije a mi amigo "pyhton es mi lenguaje favorito!"'
"El lenguaje 'Python'es llamado así por Monty Python, no la serpiente."
"Uno de las fortalezas de Pyhton es que es diverso y tiene una comunidad que ayuda."

#Cambiar los tipos de letra en string con metodos
#Metodo es una accion que python ejecuta en un pedazo de dato

name = "bernardo flores"
print(name.title())  # (.) el punto le dice a python que ocupe el metodo title()
print(name.upper())
print(name.lower())

#Combinar o concatenar strings

first_name ="bernardo"
last_name = "flores luna"
full_name =first_name +" " + last_name    # python usa + para combinar strings

print(full_name)
print("Hola,"+ full_name.title()+"!")    # Puedes usar concatenacion para componer

message = "Hola,"+ full_name.title()+"!" 
print(message)

#AÑadir espacio con tabs o nuevas lineas

print("Piton")
print("\tPiton")                           #Agrega tab a tu texto
print("Languajes:\nPython\nC\nJavaScript") #Agrega nuevalinea al string
print("Languajes:\n\tPython\n\tC\n\tJavaScript") #Se pueden combinar

#Stripping Whitespace

favorite_language ='python '
favorite_language            #output 'python ' 
favorite_language.rstrip()   #quita el espacio de la derecha solo una vez
favorite_language = favorite_language.rstrip() #remueve el espacio permanent
favorite_language   #queda una nueva variable sin el espacio de sobra

lengua_favorita = ' piton '
lengua_favorita.rstrip() #remueve el espacio de la derecha
lengua_favorita.lstrip() #remueve el espacio de la izq.
lengua_favorita.strip() #remueve el espacio de ambos lados al mismo tiempo

#Avoiding Syntax Errors with Strings: occurs when python doesn't recognize
#a section of your program as valid python code
#Así se usarian la comilla y las dobles comillas correctamente

message = "One of python's strengths is it diverse community."
print(message)

#Si se usan comillas simples para ambos casos python no reconoce donde acaban

#  message = 'One of python's strengths is it diverse community.'
#  print(message)

#EJERCICIOS:2.3 PERSONAL MESSAGE: Guarda el nombre de alguien y crea un mensaje 

nombre = 'bernardo flores'
saludo = 'Hola'+ ' ' + nombre +' buenos días!'
print(saludo)

#2.4 NAME CASES: Guarda el nombre de alguien y cambia a mayus. y minusculas

nombre = 'Bernardo flores luna'
print(nombre.title())
print(nombre.upper())
print(nombre.lower())

myStr = "Bernardo "

print("My name is " + myStr)
print(f"My name is {myStr}")  #Interpretacion de variables
print("My name is {0}".format(myStr))

print(dir(myStr)) #Muestra los metodos que se pueden aplicar a las string y estos son varios
print(myStr.upper())
print(myStr.lower())
print(myStr.swapcase())
print(myStr.capitalize())
print(myStr.replace('Hello', 'bye').upper()) #Metodos encadenados
print(myStr.count('l'))
print(myStr.startswith('H'))
print(myStr.endswith('World'))
print(myStr.split())
print(myStr.split('o'))
print(myStr.find('o'))
print(len(myStr))
print(myStr.index('e'))
print(myStr.isnumeric())
print(myStr[-1])
print(myStr[0])
print(myStr[5])
print(myStr[3])

#2.5 FAMOUS QUOTE: Encuentra una frase de alguien famoso y citala

print('Oscar Velazco Chavez dice,"Tu  mundo interior crea tu mundo exterior"')

#2.6 FAMOUS QUOTE 2: CONCATENACION
persona = 'Oscar Velazco Chavez'
frase = 'dice ,"Tu mundo interior crea tu mundo exterior."'
oracion = persona +' '+ frase
print(oracion)

#2.7 STRIPPING NAMES :Guarda el nombre de una persona y quita los espacios
nombre_persona = ' Manuel Foca Melosa '
print(nombre_persona)
print('\t Manuel Foca Melosa ' )
print('\n Manuel Foca Melosa ' )
print(nombre_persona.lstrip())
print(nombre_persona.rstrip())
print(nombre_persona.strip())


#NUMEROS : Se uasn para mantener el puntaje en un juego, representar visualizacion de datos, guardar info. en pag. web
#INTEGERS: Puedes sumar + , restar - , multiplicar * y dividir / enteros en python
#Exponentes: **

print(2+3)
print(3-2)
print(2*3)
3/2
3**2 
print(10**6)

#Puedes especificar el orden de las operaciones

print(2  +3 * 4) #Los espacios no tienen efecto en como python hace las op.
print((2 + 3) * 4)

#FLOAT: Pyton llama a cualquier numero con un punto decimal un float se refiere a que el punto decimal puede aparecer en cualquier posicion en un numero.

0.1 + 0.1 , 0.2 + 0.2 , 0.4 * 0.2 , 2 * 0.2 #Python trata de encontrar precision

#Evita Type Errors con la Funcion str() 

edad = 28
#  mensaje = 'Feliz' + edad + 'avo cumpleaños!' no se reconoce la info. que usa

#Se debe especificar como quiere ser usado ese tipo de dato en python

edad = 28
mensaje = 'Feliz ' + str(edad) + ' avo cumpleaños!'
print(mensaje)

#EJERCICIOS: 2.8 NUMERO OCHO: escribe suma,resta,multi y division que den 8

print(2+6)
print(10-2)
print(4*2)
print(24/3)

#2.9 Numero favorito: guarda tu numero fav en una variable,crea un mensaje

fav_number = 23
numero_fav = 'Mi Numero favorito es ' + str(fav_number) + ' por que nací.'
print(numero_fav)

#The Zen of python
import this