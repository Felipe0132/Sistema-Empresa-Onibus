import numpy as np
import customtkinter as ctk
import Conexao.Conexao as Conexao

class Onibus():

    def __init__(self, data_partida):
        self.data_partida = data_partida
        self.assentos_disponiveis = np.arange(1, 21)
        self.assentos_ocupados = list()
        self.data_formatada = data_partida.strftime("%d/%m/%Y")
        self.nome = f"{self.data_formatada}"


    def reservar_assento(self, assento):
        if assento > 0 and assento < 21:        

            # Converter numpy array para lista, se necessário para evitar erros
            if not isinstance(self.assentos_disponiveis, list):
                self.assentos_disponiveis = list(self.assentos_disponiveis)

            if len(self.assentos_disponiveis) == 0:
                Conexao.janela_aviso("Assentos indisponiveis!", 'red')
                return True

            if assento in self.assentos_ocupados:
                Conexao.janela_aviso("Assento escolhido ocupado!", 'red')
                return False
                
            Conexao.janela_aviso(f"Assento {assento} reservado! Atualize para ver disponibilidade!", 'green')    
            self.assentos_disponiveis.remove(assento)
            self.assentos_ocupados.append(assento)
        else:
            Conexao.janela_aviso("Lugar indiponivel!", "red")
            return False

    def mostrar_assentos(self):
        print("Assentos livres: ", end="")
        for livres in self.assentos_disponiveis:
            print(livres, end=", ")

        print("Assentos ocupados: ", end="")
        for ocupados in self.assentos_ocupados:
            print(ocupados, end=", ")

        if self.assentos_disponiveis: # Verifica se ha assentos
            while True:
                try:
                    lugar = input("Digite o lugar que deseja reservar: ")
                except ValueError:
                    print("Digite um inteiro!")
                    continue
                except Exception as e:
                    print(f"Error: {e}")
                    continue
                else:
                    self.reservar_assento(lugar)
                    break
        else: # Se estiver todos ocupados
            print("Sem opcao de reservar, lugares cheios!")


            