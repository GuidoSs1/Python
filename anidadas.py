# Funciones anidadas en python
name = 'global'

def saludo():
    name = 'Guido'
    def hola():
        print(f'Hola {name}')
    
    hola()

saludo()

nombre = 'guido'
def variables():
    global nombre # De esta forma se pueden utilizar las variables definidas fuera de las funciones
    print(nombre)
    nombre = 'julio'
    print(f'Nuevo nombre {nombre}')

variables()
print(nombre)