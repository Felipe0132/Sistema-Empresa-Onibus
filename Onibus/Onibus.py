import numpy as np # Importa biblioteca numpy
import customtkinter as ctk # Importa biblioteca grafica
import datetime # Importa biblioteca de formato de datas
import os # Importa biblioteca de sistema operacional

# --------------------------------------------------------------

# Extras

def janela_aviso(mensagem, cor): # Funcao que recebe uma mensagem e cor para aparecer na tela

    # Criar janela

    janela = ctk.CTkToplevel()
    janela.title("AVISO") # Nome da janela
    janela.geometry("500x80") # Tamanho
    janela.configure(fg_color="white")

    janela_aviso = ctk.CTkFrame(janela, fg_color="white") # Cor de fundo
    janela_aviso.pack(fill="both", expand=True) # Cria um widget, fill é o preenchimento, expand seria a responsividade do tamanho

    aviso = ctk.CTkLabel(janela_aviso, text=mensagem, text_color=cor, font=('Arial',17))
    aviso.pack(pady=10) # Mostrando mensagem

    botao = ctk.CTkButton(janela_aviso, text="OK", command=janela.destroy)
    botao.pack(pady=5) # Destroi a atual

def registrar_erro(mensagem): # Funcao que registra erro em um arquivo .txt
    try:
        # Cria a pasta logs se não existir
        if not os.path.exists("logs"):
            os.makedirs("logs")

        # Pega data e hora atual
        data_hora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        # Monta a linha que será escrita no txt
        linha = f"[{data_hora}] - {mensagem}\n"

        # Abre (ou cria) o arquivo e adiciona a nova linha
        with open("txts/logs_erros.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(linha)

    except Exception as e:
        # FAILSAFE: evita que erro dentro da função quebre o sistema
        print("Falha ao registrar erro:", e)

# -------------------------------------------------------------

# Classe

class Onibus(): # Criando classe Onibus

    def __init__(self, data_partida): # Construtor recebe somente uma data, sua identificacao
        self.data_partida = data_partida 
        self.assentos_disponiveis = np.arange(1, 21) # Sempre cria uma lista de numeros de 1 a 20 que sao seus assentos
        self.assentos_ocupados = list() # Assentos ocupados comecam com 0
        self.data_formatada = data_partida.strftime("%d/%m/%Y") # Fomata para poder comparar depois
        self.nome = f"{self.data_formatada}" # Identificacao


    def reservar_assento(self, assento): #  Funcao de reservar um assento
        if assento > 0 and assento < 21:         # Verifica se o assento existe

            # Converter numpy array para lista, se necessário para evitar erros
            if not isinstance(self.assentos_disponiveis, list):                                                
                self.assentos_disponiveis = list(self.assentos_disponiveis)

            if len(self.assentos_disponiveis) == 0: # Se os assentos disponiveis forem 0
                janela_aviso("Assentos indisponiveis!", 'red')
                registrar_erro(f"[{self.data_formatada}] Reserva não realizada: ônibus cheio")
                return False

            if assento in self.assentos_ocupados: # Se o assento ja estiver ocupado
                janela_aviso("Assento escolhido ocupado!", 'red')
                registrar_erro(f"[{self.data_formatada}] Reserva não realizada: assento {assento} já ocupado")
                return False
                
            if assento % 2 == 0: # Se o assento for impar ele fica na janela, se nao, no corredor
                janela = "no corredor!"
            else:
                janela = "na janela!"

            janela_aviso(f"Assento {assento} reservado {janela} Atualize para ver disponibilidade!", 'green')    
            self.assentos_disponiveis.remove(assento) 
            self.assentos_ocupados.append(assento)
            # Caso nao tenha parado em nenhuma restricao, ele remove o assento dos disponiveis e joga para o ocupados

        else: # Se o assento nao exisitr
            janela_aviso("Lugar inexistente!", "red")
            registrar_erro(f"[{self.data_formatada}] Reserva não realizada: assento {assento} inválido (1–20)")
            return False