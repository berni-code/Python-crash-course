#LIST: Es una coleccion de objetos en un orden particular, puedes poner cualquier cosa
#es una buena idea hacer el nombre de la lista en plural como letras, digitos.
#En python los brackets [] indican una lista y los elementos individuales son separados por comas.


juegos = ['final fantasy vii','Tomb Raider','Hollow Knight','Doom 3']
print(juegos)

#ACCEDER A UN ELEMENTO DE LA LISTA : Puedes decirle a python el indice del objeto que quieras

print(juegos[0])
print(juegos[0].upper()) #se pueden usar metodos en los strings

#La posicion del indice empieza en  0, no en  1.Este codigo da el segundo y cuarto elemento.

print(juegos[1]) 
print(juegos[3])

#Sintax especial para acceder al ultimo elemento -1

print(juegos[-1]) #Llama al ultimo elemento de la lista
print(juegos[-2])
print(juegos[-3].upper())

#Usar valores individuales de la lista

juegos = ['final fantasy vii','Tomb Raider','Hollow Knight','Doom 3']
mensaje = "El juego que quiero acabar es " + juegos[0].upper() + "."
print(mensaje)

#EJERCICIOS 3.1 NOMBRES Guarda el nombre de personajes en una lista e imprime cada uno

personajes = ['cloud','tifa','barret','lara','marine','warrior']
print(personajes[0])
print(personajes[1])
print(personajes[2])
print(personajes[3])
print(personajes[4])
print(personajes[-1])

#3.2 SALUDOS:Inicia con la lista anterior y ocupa un mensaje para todos

print('\nEste es un personaje de un juego ' + personajes[0].title())
print('Este es un personaje de un juego ' + personajes[1].title())
print('Este es un personaje de un juego ' + personajes[2].title())
print('Este es un personaje de un juego ' + personajes[3].title())
print('Este es un personaje de un juego ' + personajes[4].title())
print('Este es un personaje de un juego ' + personajes[-1].title())

#3.3 TU PROPIA LISTA:haz una oración para cada elemento de la lista

transportes = ['coche','camion','metro','bici','patin'] 

print('\nYo no tengo ' + transportes[0])
print('Viajo poco en '+transportes[1])
print('El '+transportes[2]+' esta muy lleno casi siempre')
print('Vendí la '+transportes[3])
print('Es muy divertiddo usar el '+transportes[4])

#CAMBIAR ,AÑADIR Y REMOVER ELEMENTOS:
#Modificar elementos
juegos_vr = ['beat saber','pistolwhip','raw data','super hot']
print(juegos_vr)

juegos_vr[0] = 'borderlands2' #se puede cambiar cualquier valor elemento
print(juegos_vr)

#AÑADIR ELEMENTOS A UNA LISTA:

juegos_vr.append('beat blaster') #Añade el elemento a la lista pero al final
print(juegos_vr)

juegos_vr =[]
juegos_vr.append('beat saber')
juegos_vr.append('paper beast')
juegos_vr.append('thumper')

print(juegos_vr)

#Insertar elementos dentro de la lista con el método insert() 

juegos_vr = ['beat saber', 'paper beast', 'thumper']
juegos_vr.insert(1,'tetris effect')               #el metodo abre un espacio en 1 y mueve los demas a la derecha

#REMOVER ELEMENTOS DE LA LISTA
#Remueve un objeto usando la declaracion del

juegos_vr = ['beat saber', 'paper beast', 'thumper']
print(juegos_vr)

del juegos_vr [2] #se usa del para remover elementos de la lista
print(juegos_vr)

del juegos_vr[0]
print(juegos_vr)  
#en ambos casos ya no se puede acceder al elemento que se removio usando del

#Quita el ultimo objeto usando pop() en la lista.

juegos_vr = ['beat saber', 'paper beast', 'thumper']
print(juegos_vr)

popped_juegos = juegos_vr.pop() #popeamos el valor de la lista y lo guardamos
print(juegos_vr)
print(popped_juegos) #aun tenemos acceso a ese elemento 

juegos_vr = ['beat saber', 'paper beast', 'thumper']

ultimo_jugado = juegos_vr.pop()
print('El ultimo juego que probe de VR fue '+ultimo_jugado.title()+'.')

#Popping Items de cualquier posicion de la lista: solo indicamos el indice del elemento

mejor_juego = juegos_vr.pop(0)
print('El mejor juego de VR y más divertido es '+mejor_juego.title())

#Cada que se usa el metodo pop() el elemento no se guarda en la lista
#Cuando no se quiera algo en la lista lo borramos con del 
#Si se quiere usar ese elemento de la lista lo removemos con pop()

#Remover un objeto por valor: cuando solo sabes el valor de lo que quieres quitar

juegos_vr = ['beat saber', 'paper beast', 'thumper']
print(juegos_vr)

juegos_vr.remove('paper beast')
print(juegos_vr)

regalado = 'thumper'
juegos_vr.remove(regalado)
print(juegos_vr)
print("\nEl juego de " +regalado.title()+" fue regalado y no comprado.")

#El metodo remove() borra solo la primera aparición que especificas

#EJERCICIOS 3.4 GUEST LIST: crea una lista de tres juegos que quieres probar

por_probar = ['Nier Automata','Resident Evil VII','Persona 5']
print('Quiero jugar '+ por_probar[0])
print('Me asustaria jugando '+ por_probar[1])
print('He escuchado buenas reseñas de '+ por_probar[2])

#3.5Cambiando la lista de invitados: cambia un elemento y sustituylo por otro.

por_probar = ['Nier Automata','Resident Evil VII','Persona 5']
print('\n'+ por_probar.pop(2))

por_probar.insert(2,'Horizon Zero Dawn')
print('\tJugare '+ por_probar[2]+ ' cuando lo vuelva a instalar')
print('Esta de oferta el juego de ' + por_probar[0])
print('El '+ por_probar[1] + ' estaría bueno en vr!')
print(por_probar)

#3.6 Mas elementos.

por_probar.insert(0,'Crash bandicoot')
por_probar.insert(1,'Batman')
por_probar.append('Bloodborne')
print('Lo que me falta es tiempo para poder jugar a ' + por_probar[0])
print('Comprare ' + por_probar[2])
print('Volvere a instalar '+ por_probar[1])
print('Pronto tendre más memoria para instalar estos juegos')
print(por_probar)

#3.7 Haz la lista más pequeña.

print('\nAl final solo podré jugar estos dos juegos')
print(por_probar)

print('\nEl ' + por_probar.pop() + ' esta muy dificil')
print('Luego compro el ' + por_probar.pop(0))
print('No tengo espacio para guardar el ' + por_probar.pop(0))
print('Me da miedo jugar ' + por_probar.pop(1))
print('Luego compro el ' + por_probar[0])
print('Se que este es un juegazo ' + por_probar[1])
print('\nMe he quedado solo con ' + por_probar[0] + ' y '+ por_probar[1])
del por_probar[0]
del por_probar[0]
print(por_probar)

#ORGANIZANDO UNA LISTA
#Ordenar una lista permanentemente con el sort() method.

cosas = ['guitarra','silla','cama','monitor','computadora','visor','control']
cosas.sort()   #Cambia el orden de la lista de manera permanente 
print(cosas)

#Tambíen se pueden acomodar en el orden contrario con el argumento reverse = True

cosas = ['guitarra','silla','cama','monitor','computadora','visor','control']
cosas.sort(reverse = True)
print(cosas)

#Ordenar una lista temporalmente sorted() Function

cosas = ['guitarra','silla','cama','monitor','computadora','visor','control']

print('Aquí esta la lista original:')
print(cosas)

print('\nAquí esta la lista ordenada:')
print(sorted(cosas))

print('\nAquí esta la lista original de nuevo:')
print(cosas)

print('\nAquí esta la lista en reversa:')
print(sorted(cosas,reverse=True))

#Imprimir una lissta en orden inverso

cosas = ['guitarra','silla','cama','monitor','computadora','visor','control']
print(cosas)

cosas.reverse() #No ordena de manera alfebetica solo revierte el orden:
print(cosas)  #el metodo reverse() cambia el orden de manera permanete

len(cosas)  #Sirve para saber el número de elementos de una lista

#EJERCICIOS 3.8 Piensa en cinco lugares por visitar

lugares = ['jápon','nueva zelanda','cánada','new york','africa']
print(lugares)
print(sorted(lugares))
print(sorted(lugares,reverse = True))
print(lugares)

lugares.reverse()
print(lugares)

lugares.reverse()
print(lugares)

lugares.sort()
print(lugares)

lugares.sort(reverse=True)
print(lugares)

#3.9Numero de lugares: 
print('La catidad de lugares a los que ire son: '+ str(len(lugares)))

#3.10 Crea una lista de lo que quieras y ocupa todo 
# #Crear la lista con []
colores = ['morado','rojo','azul','verde','naranja','negro','amarillo','gris']
print('Los colores que tengo son: '+ str(len(colores))) #Mensaje y tamaño
print(colores[0].title()) #Llamar a cada elemnto y aplicar un metodo
print(colores[1])
print(colores[2])
print(colores[3])
print(colores[4])
print(colores[5])
print(colores[6])
print(colores[7])
print(colores[-1])

print('\nMi color favorito es el '+ colores[0].upper()) #Mensaje ocupando elem
print('La ropa que más uso es de color ' + colores[-3].title())
print('Mi segundo color favorito es el ' + colores[4])

colores[3] = 'blanco' #Cambiar un elemento de la lista por otro en donde quiera
print(colores)

colores.append('dorado') #Agregar un elemento a la lista al final de la misma
colores.append('café')
print(colores)

colores.insert(3,'rosa') #Inserta un elemento a la lista en  la posición deseada
print(colores)

del colores[2] #Borra un elemento de la lista indicando la posición
print(colores)

pop_color = colores.pop() #Guarda el ultimo elemento en una variable para usarlo cuando queramos
print(colores)
print('El color que menos me gusta es el ' + pop_color)
print(colores.pop())  #Guarda el ultimo elemento de la lista 
print(colores.pop())
print(colores.pop())
print(colores.pop())
print(colores.pop(2)) #Guarda el elemento que le indique de la lista 
print(colores)

colores.remove('blanco') #Remueve el elemento por el valor el mismo
print(colores)

print(sorted(colores)) #Acomoda temporalmente en orden alfabetico
print(colores)
sorted(colores,reverse=True) #Acomoda alreves en orden alfabetico con el argumento
print(colores)

colores.reverse() #revierte la lista sin orden
print(colores)

colores.sort() #Acomoda de manera permanente la lista y en orden alfabetico
print(colores)
colores.sort(reverse=True) #Acomoda con el argumento 
print(colores)

#AVOIDING INDEX ERRORS WHE WORKING WHIT LIST: 

# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles[3])  #El indice de la lista no llega al 4to elemnto 
#                        #Los indices empiezan en 0 

# motos = []
# print(motos[0]) #No se pueden llamar a elementos de una lista vacía