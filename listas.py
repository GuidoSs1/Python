# Listas
miLista = [1,2,3]
lista = ['hola', 1, 3.2]

print(miLista) # Esto imprimira en pantalla la lista "[1,2,3]"
print(len(miLista)) # Mostrara la cantidad de elementos dentro de la lista

print(lista) # Lo mismo que al mostrar miLista, pero con sus elementos

# Se puede crear una nueva lista con los elementos de dos listas, sumandolas
print(miLista + lista)
# O de la siguiente forma que seria mas correcta
nuevaLista = miLista + lista
print(nuevaLista) # mostrara una lista con los elementos de ambas listas "[1,2,3,'hola',1,3.2]"

# Tambien se pueden modificar valores dentro de las listas, por indice de elemento
nuevaLista[0] = 'Guido'
print(nuevaLista)

# Funciones de las listas
nuevaLista.append('seis') # agrega un elemento al final de la lista
print(nuevaLista)

item = nuevaLista.pop() # Esta funcion popea el ultimo elemento de la lista, removiendolo y pudiendo asignarlo a una varible. Se puede especificar el elemento poniendo el indice dentro de los parentesis
itemDos = nuevaLista.pop(0)

print(nuevaLista)
print(item)
print(itemDos)

miLista = ['a','z','x','b','d']

miLista.sort() # Esta funcion ordena la lista en forma alfabetica o de menor a mayor siendo numericos NO SE ASIGNA A UNA VARIABLE
print(miLista)

miLista.reverse() # Este es un orden inverso al de la funcion sort()
print(miLista)

miLista = [x for x in range(0,10)]
print(miLista) # Esto mostrara una lista con los numeros del 0 al 10 no incluido

# Conversion de grados el celcius a fahrenheit
celcius = [0,10,20,34.5]

fahrenheit = [((9/5)*temp + 32) for temp in celcius]

print(fahrenheit) # Esto mostrara los valores de la lista de celcius en fahrenheit