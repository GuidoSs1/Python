from random import randint, shuffle #De esta forma se importan metodos como con 'using' en C# o 'import' en JS 

# Declaraciones If, Elif y Else
hambre = True
sed = True

if hambre and not sed:      # Siempre hay que respetar la identacion para aplicar sentencias if, elif o else
    print('Tenemos hambre')
elif hambre and sed:    # Los operadores logicos son con palabras(and, or, not)
    print('Tenemos hambre y sed')
else:
    print('No tenemos hambre')

# Ciclos FOR
miLista = [1,2,3,4,5,6]

for num in miLista:
    if num % 2 == 0:
        print(num)
    else:
        print(f'Numero impar: {num}') # La 'f' al comienzo de la cadena funciona como un format

# En tuplas 
listTupla = [(1,2),(1,3),(2,3),(2,2)]

for num in listTupla:
    print(num) # Esto mostrara cada elemento de la lista, por lo tanto (1,2) (1,3) y asi

for (a,b) in listTupla:     # Tuple Unpacking
    print(a)
    print(b) # De esta forma mostrara cada elemento independientemente

# En diccionarios
dic = {'y':'g', 'z':'a', 'e':'r'}

for item in dic:
    print(item) # De esta forma mostrara solo la clave por lo tanto 'y','z' y 'e'

for (clave,valor) in dic.items():
    print(valor) # De esta forma mostrara los valores y las claves de la misma forma que con las tuplas

# Ciclos While
x = 0

while x < 5:
    print(f'El valor actual de x es {x}')
    x += 1 # No se puede usar el incremento y decremento con las variables ++ o --
else: # El while posee la opcion de tener un else
    print('X no es mayor a 5')

# Al igual que en otros lenguajes posee las palabras clave break, continue y pass

# Operadores utiles
cadena = 'Hola mundo'
for item in enumerate(cadena):
    print(item) # Esto gracias a la funcion enumerate devolvera pares de indice y valor '(0,H)' 

for (indice,item) in enumerate(cadena):
    print(item)

lista = [1,2,3]
letras = ['a','b','c']

for item in zip(lista, letras):
    print(item) # Con la funcion zip, se juntaran los valores de las listas por indice, esto mostra los elemento de a pares

min(lista) # Esta funcion devolvera el valor mas pequenio dentro de la lista especificada
max(lista) # Devolvera el valor maximo dentro de la lista

# Input
resultado = input('Escribe tu nombre aqui: ')

print(resultado) # Se mostrara lo ingresado por el usuario