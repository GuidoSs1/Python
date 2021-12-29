# El manejo de los errores y/o excepciones es por medio de sentencias parecidas a las de C#

try:
    resultado = 10 + '10'
    print(resultado)
except:
    resultado = 10 + 10
    print(resultado)
finally:
    print('Esto se ejecutara de todas formas')