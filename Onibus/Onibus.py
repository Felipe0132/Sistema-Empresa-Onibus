import numpy as np
import customtkinter as ctk
from Conexao.Conexao import registrar_erro


def janela_aviso(mensagem, cor):

    # Criar janela

    janela = ctk.CTkToplevel()
    janela.title("AVISO") # Nome da janela
    janela.geometry("500x80") # Tamanho
    janela.configure(fg_color="white")

    janela_aviso = ctk.CTkFrame(janela, fg_color="white") # Cor de fundo
    janela_aviso.pack(fill="both", expand=True) # Cria um widget, fill é o preenchimento, expand seria a responsividade do tamanho

    aviso = ctk.CTkLabel(janela_aviso, text=mensagem, text_color=cor, font=('Arial',17))
    aviso.pack(pady=10)

    botao = ctk.CTkButton(janela_aviso, text="OK", command=janela.destroy)
    botao.pack(pady=5)

    janela.after(10, janela.lift)


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
                janela_aviso("Assentos indisponiveis!", 'red')
                registrar_erro(f"[{self.data_formatada}] Reserva não realizada: ônibus cheio")
                return False

            if assento in self.assentos_ocupados:
                janela_aviso("Assento escolhido ocupado!", 'red')
                registrar_erro(f"[{self.data_formatada}] Reserva não realizada: assento {assento} já ocupado")
                return False
                
            janela_aviso(f"Assento {assento} reservado! Atualize para ver disponibilidade!", 'green')    
            self.assentos_disponiveis.remove(assento)
            self.assentos_ocupados.append(assento)
        else: #Esse else n tem utildade como o lugar é indisponivel
            janela_aviso("Lugar indiponivel!", "red")
            registrar_erro(f"[{self.data_formatada}] Reserva não realizada: assento {assento} inválido (1–20)")
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


            