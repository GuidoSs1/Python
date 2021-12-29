# Funciones
def primera(nombre):
    print(f'Tu nombre es {nombre}')

primera('Guido')

def numerosParesEnLista(lista):
    for number in lista:
        if number % 2 == 0:
            print(number)
        else:
            print(f'{number} No es par')

lista = [1,2,3,4,5,6,7,8,9,10]

numerosParesEnLista(lista)

# Args y kwargs
def func(*args): # Con el *args se define una tupla como parametro de la funcion, por lo cual podra recibir un conjunto de datos
    return print(sum(args) * 0.05)

func(1,2,3,4,5)
func(11,2,3,455,6,7,8)

def funcion(**kwargs): # Se pronuncia keyboardarguments, esto define un diccionario como parametro por lo cual al pasarle valores a la funcion se tendra que hacer de la misma forma que con un diccionario, pasando clave='valor'
    if 'fruit' in kwargs:
        print('Mi fruta escogida es {}'.format(kwargs['fruit']))
    else:
        print('No hay fruta')

funcion(fruit='manzana',vegetales='lechuga')

# Funcion mapa, es util para llenar una funcion con los elementos de una lista
numero = [1,2,3,4,5]

def square(num):
    result = num**2
    print(result)
    return result

for item in map(square, numero): # Esta funcion le pasa cada elemento a la funcion square
    print(item)

# Funcion filter
def numerosPares(num):
    return num % 2 == 0

for n in filter(numerosPares, numero): # filter le dara el valor retornado por la funcion a 'n' con el elemento de la lista
    print(n)

# Expresion lambda
squareDos = lambda num: num**2

print(map(lambda num:num**2, numero)) # Lo mismo que con la primera funcion pero utilizando lambda