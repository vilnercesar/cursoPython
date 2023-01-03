# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela


class Carro:
    def __init__(self,nome):
        self._nome = nome
        self._motor = None
        self._fabricante = None
        

    @property
    def nome(self):
        return self._nome
    
    @property
    def motor(self):
        return self._motor
   
    @motor.setter
    def motor(self, nome_motor):
        self._motor = Motor(nome_motor,self)

    @property
    def fabricante(self):
        return self._fabricante
   
    @fabricante.setter
    def fabricante(self, nome_fabricante):
        self._fabricante = Fabricante(nome_fabricante)
    
    def config_MyCar(self,nome_motor,nome_fabricante):
        self.motor = nome_motor
        self.fabricante = nome_fabricante
    def print_car(self):
        print (f'Nome do carro: {self.nome}')
        print(f'Motor: {self.motor.nome_motor}')
        print( f'Fabricante: {self.fabricante.nome_fabricante}')



class Motor:
    def __init__(self,nome,obj_car):
        self.nome_motor = nome
        self.mycars = []
        self.mycars.append(obj_car)



class Fabricante:
    def __init__(self,nome):
        self.nome_fabricante = nome
     

gol = Carro('Gol')

gol.config_MyCar('Motor de Gol','WolksWagem')





