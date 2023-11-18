

class Animal:

    def __init__(self, nome, cor):
        self.nome=nome
        self.cor=cor


    def comer(self):
        print(f"O {self.nome} foi comer")

class Gato(Animal):

    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def miar(self):
        print(f"O {self.nome} foi miando")

#cachorro, coelho e vaca

class Cachorro(Animal):

    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def latir(self):
        print(f"O {self.nome} foi latindo")

class Coelho(Animal):

    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def ronronar(self):
        print(f"O {self.nome} foi ronronando")

class Vaca(Animal):

    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def mungir(self):
        print(f"O {self.nome} foi mungindo")