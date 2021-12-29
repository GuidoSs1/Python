# Programacion Orientada a Objetos en python
class Perro():
    def __init__(self, raza, nombre,color): # Este es un constructor, siempre debera tener como parametro self
        self.raza = raza # EL self en este caso hace referencia la objeto o la instancia como el 'this' en C#
        self.nombre = nombre
        self.color = color


labrador = Perro(raza='labrador', nombre='apolo', color='marron claro') # De esta forma se instancia un objeto de la clase perro
# Self no necesita ningun valor al momento de instanciar un objeto

class Animal():
    def __init__(self):
        print('Animal creado')
    def soy(self):
        print('Soy un animal') # A todas los metodos de una clase se le pasa como parametro el 'self'
    def comer(self):
        print('Estoy comiendo')

class Gato(Animal): # Poniendo la clase dentro de los parentesis de la declaracion de la clase es como se trabaja con herencia en python, en este caso gato hereda de animal
    def __init__(self):
        Animal.__init__(self) # Esto seria como un llamado al constructor de la clase base en C#
        print('Gato creado')
    def soy(self):
        print('Soy un gato')

miGato = Gato()
miGato.soy()