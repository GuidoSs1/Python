import random
from words import words
import string
from draws import vidas_diccionario_visual

def ahorcado():
    print('================================')
    print('Bienvenido al juego del Ahorcado')
    print('================================')

    palabra = palabra_valida(words)

    letras_restantes = set(palabra)
    letras_adivinadas = set()
    abecedario = set(string.ascii_uppercase)

    vidas = 9

    while len(letras_restantes) > 0 and vidas > 0:
        print(f'Te quedan {vidas} vidas y has usado estas letras: {" ".join(letras_adivinadas)}')

        palabra_lista = [letra if letra in letras_adivinadas else '-' for letra in palabra]

        print(vidas_diccionario_visual[vidas])
        print(f'\nPalabra: {" ".join(palabra_lista)}')

        letra_usuario = input("Escoge una letra: ").upper()

        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)
            if letra_usuario in letras_restantes:
                letras_restantes.remove(letra_usuario)
                print('')
            else:
                vidas -= 1
                print(f'\nLa letra {letra_usuario} no esta en la palabra.')
        elif letra_usuario in letras_adivinadas:
            print('\nYa escogiste esa letra, Por favor escoge una nueva letra.')
        else:
            print('\nEsta letra no es valida.')
    
    if vidas == 0:
        print(vidas_diccionario_visual[vidas])
        print(f'\nAhorcado!!. La palabra era "{palabra}"')
    else:
        print(f'Felicitaciones!! Adivinaste la palabra "{palabra}"')





def palabra_valida(words):
    palabra = random.choice(words)

    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(words)

    return palabra.upper()

ahorcado()