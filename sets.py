# Sets, son colecciones unicas y desordenadas de elementos, solo puede haber una representacion del mismo objeto en un set
miSet = set()

miSet.add(1) # Funcion para agregar elementos al set
miSet.add(1) # No lo agregara ya que la principal caracteristica de los set es que solo aceptan valores unicos
miSet.add(2)

print(miSet) # Mostrara los elementos como un diccionario "{1,2}"

# Los set se pueden utilizar para filtrar listas con elementos repetidos
miLista = [1,1,1,1,1,1,1,2,2,2,2,2,2,2,3,3,3,3,4]

print(set(miLista)) # Motrara los elementos 1,2,3,4