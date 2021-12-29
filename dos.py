import uno

print('Nivel top en uno.py')

uno.func()

if __name__ == '__main__': # Esto verifica el nombre del archivo, si el archivo que ejecuta esta funcion es el mismo en el que la funcion fue definida sera true, de otra forma no
    print('dos.py esta siendo corrido directamente')
else:
    print('dos.py esta siendo importado')