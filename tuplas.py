# Tuplas, este tipo de dato es parecido a las listas
tupla = ('a','a','b')

lista = [1,2,3]

print(tupla.count('a')) # Esta funcion devuelve cuantos elementos iguales a lo especificado entre parentesis hay dentro de la tupla
print(tupla.index('a')) # Esta devuleve el primer indice del elemento igual a lo de dentro del parentesis 

# Las tuplas son de valores inmutables
lista[0] = 'NUEVO'
tupla[0] = 'NUEVO' # Esto dara un error en el programa dado que no se pueden modificar los valores con los que fue declarada