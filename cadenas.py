# Indices y Slicing
micadena = 'Hola Mundo'
print(micadena[2]) #Mostrara la letra 'l'
print(micadena[-1]) #Mostrara la letra 'o' por indexado inverso de python

print(micadena[3:6]) #Slicing [start:stop:step] o en este caso [start:stop] esto mostrara 'a M' (no toma la posicion 6)
print(micadena[::]) # Desde el incio hasta el fin

# Inmutabilidad de las cadenas
nombre = 'Guido'
#nombre[0] = 'S'  No es posible hacer esto
ultima = nombre[1:]

print('P' + ultima) # Esto mostrara "Puido" (Seria una forma de modificar una cadena)

letra = 'z'
letra *= 10 # Se multiplica las veces que se repite la letra 'z'

print(letra) # Esto mostrara 10 veces la letra 'z'

# Algunas Funciones
x = 'Hola Mundo'
x = x.upper() # Modifica todas las letras de la cadena a mayusculas (solo funciona cuando la cadena esta declarada con comillas simples)
print(x)
x = x.lower() #Modifica todas las letras de la cadena a mayusculas (solo funciona cuando la cadena esta declarada con comillas simples)
print(x)
x = x.split('o') # Quita el caracter definido dentro de los parentesis y mustra la cadena en forma de lista
print(x)

print('Esta es una cadena de {}'.format('TEXTO')) # parecido al stringbuilder y su meotodo de appendformat en C#
print("{g} {u} {i}".format(g="Esto", u="es", i="mentira"))

resultado = 100/888
#                  {valor:width.precision f}
print('Los resultados son {r:10.3f}'.format(r=resultado))
