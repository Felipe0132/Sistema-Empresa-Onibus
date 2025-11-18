import numpy as np

class Onibus():

    def __init__(self, data_partida):
        self.datas_partida = data_partida
        self.assentos_disponiveis = np.arange(1, 21)
        self.assentos_ocupados = list()
        self.nome = f"{data_partida}"

        pass

    def reservar_assento(self, assento):
        if assento in self.assentos_ocupados:
            print("Assento ocupado!")
            return
        
        self.assentos_disponiveis.remove(assento)
        self.assentos_ocupados.append(assento)

    def mostrar_assentos(self):
        print("Assentos livres: ", end="")
        for livres in self.assentos_disponiveis:
            print(livres, end=", ")

        print("Assentos ocupados: ", end="")
        for ocupados in self.assentos_ocupados:
            print(ocupados, end=", ")