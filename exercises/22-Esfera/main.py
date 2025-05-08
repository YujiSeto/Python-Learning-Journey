import math

class Esfera:
    def __init__(self, cor, raio):
        self.cor = cor
        self.raio = raio

    def volume(self):
        vol = (4 / 3) * math.pi * (self.raio ** 3)
        return vol

    def area(self):
        ar = 4 * math.pi * (self.raio ** 2)
        return ar

# Criando objetos
bola1 = Esfera('vermelha', 4)
bola2 = Esfera('azul', 7)

# Impressões formatadas
print(f'O volume da bola 1 é {bola1.volume():.2f} cm³')
print(f'A área superficial da bola 1 é {bola1.area():.2f} cm²')

# Chamadas diretas
print(bola1.volume())
print(Esfera.volume(bola1))  # Equivalente a bola1.volume()
