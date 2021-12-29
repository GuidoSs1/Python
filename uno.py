def func():
    print('Func() en uno.py')

print('Nivel top en uno.py')

if __name__ == '__main__': # Esto verifica que el archivo que ejecuta esta funcion sea el main 
    print('uno.py esta siendo corrido directamente')
else:
    print('uno.py esta siendo importado')

