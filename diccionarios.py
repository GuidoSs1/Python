# Diccionarios se basan en pares clave/valor
miDiccionario = {'apellido':'Sosa Stillante', 'nombre':'Guido'}
print(miDiccionario) # Esto al igual que en las listas mostrara el diccionario explicitamente, osea "{'apellido':'Sosa Stillante','nombre':'Guido'}"

print(miDiccionario['nombre']) # Esto mostrara el valor relacionado a esta clave, por lo tanto 'Guido'

# Tambien se puede asisnar una lista como valor de una clave en los diccionarios
kekes = {'Manzana':'3.2','kekes':['manzana','banana'],'Pera':'3.5'}
print(miDiccionario['kekes'][1]) # De esta forma mostramos el valor 'banana' de la clave 'kekes'

# Agregas pares clave/valor a un diccionario
miDiccionario['amigo'] = 'julian'
print(miDiccionario) # mostrara el par clave/valor 'amigo':'julian'

print(miDiccionario.values()) # Mostrara una lista de los valores de los pares clave/valor dentro del diccionario
print(miDiccionario.items()) # Mostrara los pares como una lista separandolos por parentesis
