  #LOOPING ATRAVEZ DE UNA LISTA ENTERA: cuando queremos 
  #item in a list you can use for loop

ejercicios = ['jalar','empujar','correctivo','estirar','resistir']
for ejercicio in ejercicios: #agarra el nombre de la lista ejercicios y lo guarda en una variable llamada ejercicio
    print(ejercicio)
  #El codigo podria entenderse como "Para cada ejercio en ejercicios, imprime el ejercicio"

  #Doing more work within a foor loop

ejercicios = ['jalar','empujar','correctivo','estirar','resistir']
for ejercicio in ejercicios:
    print(ejercicio.title()+' te hace bien') 
    print('Tengo que recuperarme de mi codo para poder ' + ejercicio+'\n')
  
    #Cada linea escrita despues del espacio se considera dentro del loop
    #y cada linea escrita se ejecuta una vez por cada valor en la lista
    #Puedes usar las lineas que necesites encontraras util ocupar operaciones con cada elemento de la lista

  #Doing something after a for loop:cada linea escrita despues del espacio
  #se ejecuta una sola vez
print('Pronto podre hacer ejercicio de nuevo!')

  #Avoiding indentation errors:
  #Olvidar escribir despues del espacio para referir bien el loop
  #Errores de logica pero que son codigo valido en python
  #Escribir lineas innecesarias arrojaran error cuando no hay razon de hacerlo
  #Escribir lineas que no quieres que esten en el loop

# ejercicios = ['jalar','empujar','correctivo','estirar','resistir']
# for ejercicio in ejercicios     ---------- Aqui no estan los :
# print(ejercicio.title()+' te hace bien')---Aquí no se dejo el espacio
#     print('Tengo que recuperarme de mi codo para poder ' + ejercicio+'\n')
   
  #EJERCICIOS 4.1 PIZZAS: piensa en tres tipos de pizza que te gusten y crea una lista
  #y usa un for loop para escribir cada nombre de cada pizza.

print('\tEjercicio 4.1')
pizzas = ['peperoni','carnes','hawaiana']
for pizza in pizzas:
    print('Me gusta la pizza de ' + pizza.title())
print('Me encantan las pizzas!\n')
    
  #4.2 Animals: Piensa en animales con caracteisticas similares 

print('\n\tEjercicio 4.2')
animales = ['perro','gato','perico']
for animal in animales:
    print(animal.title())
print('\nEl '+ animales[0]+' es el mejor amigo del hombre.')
print('El '+ animales[1] + ' es muy dormilon.')
print('El '+ animales[2]+ ' se puede escapar.\n')
for animal in animales:
    print('El '+animal + ' se puede tener de mascota.')

  #MAKING NUMERICAL LIST:las listas son ideales para guardar conjuntos de numeros
  #y python provee muchas herramientas para trabajar eficientemente con ellas
  #tu código trabajara bien incluso con lista de millones de datos
  #Using range() Function:hace facil generar series de num.

for value in range(0,9):     #imprime 9 digitos empieza desde el 0 que es el primer valor
    print(value)             #y termina en el 8 que es el ultimo valor 9
print('\nEn esta nueva lista si incluye al 9')
for valor in range(0,10):    #En este caso si llega al 9 por el valor 10 que le dimos
    print(valor)

  #Using range()to make a list of numbers: Si se quiere una lista de numeros se pueden 
  #convertir los resultados de range() directamente a una lista usando la funcion list()

print('\nLista de 1-5, pares y primeros 10 cuadrados ')
numeros = list(range(1,6))
print(numeros)

numeros_par = list(range(2,11,2)) #empieza en el valor 2 y suma 2 al valor repetidamente hasta llegar o revasar el final del valor 11
print(numeros_par)

  #Se puede crear casi cualquier conjunto de numeros usando range() 
  #Ejemplo crear una lista de los primeros 10 cuadrados enteros del 1 al 10

cuadrados = []
for value in range(1,11):
    square = value**2     
    cuadrados.append(square)
print(cuadrados)    

  #Para mas consistencia se puede omitir la variable square y añadir un nuevo valor directamente
  #Se puede usar ambas una se lee mas facil pero hace más largo el codigo enfocate en escribir
  #codigo que funcione y haga loq ue quieres, después buscas maneras más efectivas de hacerlo

cuadrados = []
for value in range(1,11):     
    cuadrados.append(value**2)
print(cuadrados)    

  #Estadistica simple con una lista de numeros:algunas funciones son especificas a listas de numeros 
  #por ejemplo, se pueden encontrar el minimo,maximo y las suma de una lista de numeros:

digitos = [1,2,3,4,5,6,7,8,9,0]
min(digitos)

digitos = [1,2,3,4,5,6,7,8,9,0]
max(digitos)

digitos = [1,2,3,4,5,6,7,8,9,0]
sum(digitos)

digits = list(range(0,10))
min(digits)

  #List comprehensions:permite generar la misma lista con una linea de codigo.Combina el for loop y 
  #creacion de nuevos elementos en una línea, y añadir automaticamente cada elemento 

cuadrados = [value**2 for value in range(1,11)] #Crea la lista anterior usando comprension de lista
print(cuadrados)

#EJERCICIOS 4.3:COUNTING TO TWENTY : usa un for loop para escribir los numeros del 1 al 20

cuentas = list(range(1,21))
for cuenta in cuentas:
    print(cuenta)

  #4.4 One Million:haz una lista de numeros de uno a un millon,usa un for loop para imprimirla
print('\nEjercicio 4.4')
one_hundred = list(range(1,100))
for hundred in one_hundred:
     print(hundred)

  #4.5 Summing a million: haz una lista de uno a un millon y usa min() y max(),también sumalos
print('Ejercicio 4.5')
print(min(one_hundred))
print(max(one_hundred))
print(sum(one_hundred))

  #4.6 Odd Numbres: Usa el tercer argumento de range() para hacer una lista de numeros pares del 1 al 20
print('\nEjercicio 4.6')
cuentas = list(range(1,21,1+1))
for cuenta in cuentas:
    print(cuenta)

  #4.7 Trees: Haz una lista de multiplos de 3 en 3 al 30.Usa un for loop para imprimir la lista.
print('\nEjercicio 4.7')
tres = list(range(3,31,3))
for tree in tres:
    print(tree)
    
  #4.8 and 4.9 Cubos:Haz una lista de los 10 primeros cubos del 1 al 10 y usa un for loop para ver cada valor
print('\nEjercicio 4.8 y 4.9')

cubes = []
for cubo in range(1,11):
    valor = cubo**3     
    cubes.append(valor)
print(cubes)    

cubes = []               #Se puede reducir el codigo para hacerlo más eficiente 
for cubo in range(1,11):
    cubes.append(cubo**3) 
print(cubes)

cubes = [cubo**3 for cubo in range(1,11)] #Se hizo por comprension 
print(cubes)

  #TRABAJANDO CON UNA PARTE DE UNA LIST:Asi como se puede trabajar con elementos de una lista se puede 
  #trabajar con partes de una lista que se llama slice.
  #Slicing a List

jugadores = ['carlos','bernardo','gerard','alex','ash']
print(jugadores[0:3])   #Para hacer un slice especificas el indice del primer y ultimo elemento 

print(jugadores[1:4])   #Se puede hacer cualquier subconjunto de la lista

print(jugadores[:4])    #si se omite el primer indice se imprime desde el inicio de la lista

print(jugadores[2:])    #Una sintaxis similar se usa si se quiere una parte que incluya el final 

print(jugadores[-3:])   #Esto imprime los ulrimos 3 elementos de la lista 

  #Looping en slice:puedes usar una parte de la lista en un for loop
  #si quieres un loop en un subconjunto de elementos de la lista.

jugadores = ['carlos','bernardo','gerard','alex','ash']
print('\nAquí estan los primeros 3 jugadores de mi lista:')
for jugador in jugadores[:3]:   #En vez de hacer un loop en toda la lista se hace sobre una parte 
    print(jugador.title())

  #Los slice sirven para varias cosas como:poner el nombre de los jugadores en el puntaje final
  #puedes poner el top 3, procesar mejor los datos en paquetes de un tamaño especifico, 
 #o cuando se hace una aplicacion web se puede usar slice para desplegar info. en una serie de pag.

  #Copiar una list:haces un slice que incluye la lista orignal omitiendo el primer y segundo indice
 #esto le dice a python que el slice comience en el primer elemento y termine en el segundo.

mi_comida = ['brocoli','pollo','sopa','avena','platano']
comida_fit = (mi_comida[:])

mi_comida.append('manzana')   #Con estos agregados podemos ver que son dos listas diferentes 
comida_fit.append('nueces')
    
print('La comida que más consumo es:')
print(mi_comida)

print('\nLa comida que te ayuda a mantenerte sano es:')
print(comida_fit)

print('\n\tHaciendo ambas listas iguales no es una forma conveniente de copiar una lista')

mi_comida = ['brocoli','pollo','sopa','avena','platano']

  #Asi ambas listas serian la misma y lo que le hagas a una le pasa a la otra no conviene copiar así

comida_fit = mi_comida

mi_comida.append('manzana')   
comida_fit.append('nueces')
    
print('La comida que más consumo es:')
print(mi_comida)

print('\nLa comida que te ayuda a mantenerte sano es:')
print(comida_fit)

 #EJERCICIOS:4.10 Slices escribe un mensaje
    
mi_comida = ['brocoli','pollo','sopa','avena','platano']
print(mi_comida)

print('\nLos primeros elementos en la lista son:')
print(mi_comida[0:3])

print('\nLos tres elementos de enmedio de la lista son:')
print(mi_comida[1:4])

print('\nLos ultimos tres elementos de la lista son:')
print(mi_comida[2:])

  #4.11My Pizzas,your pizza:
    
print('\nEjercicio 4.11:')
pizzas = ['peperoni','carnes','hawaiana']
pizzas_amigos = pizzas[:]

pizzas.append('pollo')
pizzas_amigos.append('birria')

print('Mis pizzas favoritas son:')
for pizza in pizzas:
    print(pizza.title())

print('\nLas pizzas favoritas de mis amigos son:')
for pizza in pizzas_amigos:
    print(pizza.title())
    
    #4.12More Loops
print('\nLas comidas favoritas son:')    
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

for food in my_foods:
    print(food)
      
for food in friend_foods:
    print(food)

       #TUPLES:Son valores que no pueden cambiar las listas inmutables se les llama tuple.
   #Defining a Tuple: luce igual a una lista solo que usa parentesis en vez de squarebrackets
   #Una vez definida la tupla puedes acceder a los elementos justo como lo harías con una lista.

dimension = (200,50)
print(dimension[0])
print(dimension[1])

  #Looping through all values in a tuple.

dimension = (200,50)
for dimen in dimension:
    print(dimen)

    #Writing over a tuple.Aunque no podamos modificar un tuple, se pueden asignar nuevos valores 
    #a las variables que tiene el tuple.Si queremos cambiar los valores, hay que redefinir tuple.

dimension = (200,50)
print('\nDimensiones originales')
for dimen in dimension:
    print(dimen)
    
print('\nDimensiones modificadas')
dimension = (400,100)
for dime in dimension:
    print(dime)
  
  #Las tuple se usas cuando se quiere guardar información que no quieres que cambie en el programa.

    #EJERCICIO 4.13 Buffet:Un restaurante estilo buffet tiene solo 5 tipos de comida.

buffet = ('costilla','yakimeshi','noodles','sushi','postres')
for comida in buffet:
    print(comida)

print('\nCambio de menu:')
buffet = ('pollo','arroz','noodles','sushi','postres')
for comida in buffet:
    print(comida)
    
    #STYLING YOUR CODE:STYLE GUIDE,INDENTATION,LINE LENGTH,BLANK LINE,PEP8.