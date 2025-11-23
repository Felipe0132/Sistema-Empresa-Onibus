# Codigo para rodar  python3 -m Main.main001

from Linhas.Linha import Linha
from Onibus.Onibus import Onibus
import Conexao.Conexao as Conexao
import datetime
from datetime import datetime
import customtkinter as ctk # Interface grafica

linhas = dict()


#FUNÇOES PARA INTERFACE

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue") 

# Criar janela principal

janela = ctk.CTk()
janela.title("Empresa Rodoviaria") # Nome da janela
janela.geometry("800x700") # Tamanho

janela_inicial = ctk.CTkFrame(janela, fg_color="white") # Cor de fundo
janela_inicial.pack(fill="both", expand=True) # Cria um widget, fill é o preenchimento, expand seria a responsividade do tamanho


# Funcoes para abrir janelas segundarias e terciarias

def janela_adicionar_linha(): # Funcao para criar a janela responsavel para recolher informacoes de adicionar linha
    janela_adicionar_linha = ctk.CTkToplevel(janela)
    janela_adicionar_linha.title("Adicionando Linha")
    janela_adicionar_linha.geometry("500x450")
    janela_adicionar_linha.configure(fg_color='white')

    titulo = ctk.CTkLabel(janela_adicionar_linha, text="Adicionar dados", text_color='black', font=('Arial', 25))
    titulo.pack(pady=10)

    cidade_origem = ctk.CTkEntry(janela_adicionar_linha, placeholder_text="Digite a cidade de origem...", width=320, height=50)
    cidade_origem.pack(pady=10)

    cidade_destino = ctk.CTkEntry(janela_adicionar_linha, placeholder_text="Digite a cidade de destino...", width=320, height=50)
    cidade_destino.pack(pady=10)

    horario_saida = ctk.CTkEntry(janela_adicionar_linha, placeholder_text="Digite a hora de saída do ônibus (HR:MIM): ", width=320, height=50)
    horario_saida.pack(pady=10)

    valor = ctk.CTkEntry(janela_adicionar_linha, placeholder_text="Digite o valor R$... ", width=320, height=50)
    valor.pack(pady=10)

    mensagem = ctk.CTkLabel(janela_adicionar_linha, text="", text_color="black", font=('Arial', 17))
    mensagem.pack(pady=5)


    # Cria o campo dos botões abaixo, para não conflitar com o espaço
    janela_botoes = ctk.CTkFrame(janela_adicionar_linha, fg_color="white")
    janela_botoes.pack(pady=10)

    def inserir(): # Pelo motivo da interface grafica nao aceitar funcoes com parametros, cria-se uma para usar e manipular na interface grafica
        try:
            hora = datetime.strptime(horario_saida.get(), "%H:%M")
            preco = float(valor.get())

            nova_linha = Linha(cidade_origem.get(), cidade_destino.get(), hora, preco) # Pegando os dados da interface e transformando na linha

            Conexao.adicionar_linha(linhas, nova_linha) # Funcao de adicionar linha

        except ValueError:
            Conexao.janela_aviso("Dados inválidos. Verifique Informacoes passadas.", "red")

        except Exception as e:
            Conexao.janela_aviso(f"Erro: {e}", "red")

    btn_inserir = ctk.CTkButton(janela_botoes,text="Inserir", command=inserir)
    btn_inserir.pack(side="left", padx=10)
    # Nessa linha acima eh usado .get() para conseguir converter o valores das caixas
    # A funcao datetime.strptime converte o que foi recebido na caixa para valores de data

    btn_voltar = ctk.CTkButton(janela_botoes, text="Voltar", command=janela_adicionar_linha.destroy, fg_color="#4682B4", text_color="white")
    btn_voltar.pack(side="left", padx=10) 


def janela_adicionar_onibus(): # Funcao para criar a janela responsavel para recolher informacoes de adicionar linha
    jan_adicionar_onibus = ctk.CTkToplevel(janela)
    jan_adicionar_onibus.title("Adicionando Onibus")
    jan_adicionar_onibus.geometry("500x690")
    jan_adicionar_onibus.configure(fg_color='white')

    titulo = ctk.CTkLabel(jan_adicionar_onibus, text="Adicionar dados", text_color='black', font=('Arial', 25))
    titulo.pack(pady=10)

    data_saida = ctk.CTkEntry(jan_adicionar_onibus, placeholder_text="Digite a data de saida (DD/MM/AAAA)...", width=320, height=50)
    data_saida.pack(pady=10)

    linha_nome = ctk.CTkEntry(jan_adicionar_onibus, placeholder_text="Digite a linha que deseja adicionar...", width=320, height=50)
    linha_nome.pack(pady=10)

    texto = ctk.CTkLabel(jan_adicionar_onibus, text="Lista de Linhas Disponiveis", text_color='black', font=('Arial', 22)) # Mostrando as linhas que podem receber onibus
    texto.pack(pady=10)

    linhas_disponiveis = Conexao.retornar_linhas(linhas) # Aqui cria uma lista de linhas para puder imprimir os dados melhor

    scrolllist = ctk.CTkScrollableFrame(jan_adicionar_onibus, orientation=ctk.VERTICAL, width=320) # Cria uma parte de scroll na janela
    scrolllist.pack(pady=5)

    for linha_disp in linhas_disponiveis:
        ctk.CTkLabel(scrolllist, text=linha_disp).pack(pady=2) # Aqui ele coloca na caixa de scroll os itens da lista

    # Cria o campo dos botões abaixo, para não conflitar com o espaço
    janela_botoes = ctk.CTkFrame(jan_adicionar_onibus, fg_color="white")
    janela_botoes.pack(pady=5)

    def inserir(): # Pelo motivo da interface grafica nao aceitar funcoes com parametros, cria-se uma para usar e manipular na interface grafica
        try:
            data = datetime.strptime(data_saida.get(), "%d/%m/%Y")

            novo_onibus = Onibus(data) # Pegando os dados da interface e transformando na linha

            Conexao.adicionar_onibus(linhas, linha_nome.get(), novo_onibus) # Funcao de adicionar linha

        except ValueError:
            Conexao.janela_aviso("Dados inválidos. Verifique Informacoes passadas.", "red")

        except Exception as e:
            Conexao.janela_aviso(f"Erro: {e}", "red")

    btn_inserir = ctk.CTkButton(janela_botoes,text="Inserir", command= inserir)
    btn_inserir.pack(side="left", padx=5)   
    # A funcao datetime.strptime converte o que foi recebido na caixa para valores de data       

    btn_voltar = ctk.CTkButton(janela_botoes, text="Voltar", command=jan_adicionar_onibus.destroy, fg_color="#4682B4", text_color="white")
    btn_voltar.pack(side="left", padx=5) 

def janela_reservar_lugar():
    print()

def janela_comprar_passagem():
    janela_comprar_passagem = ctk.CTkToplevel(janela)
    janela_comprar_passagem.title("Comprando passagem")
    janela_comprar_passagem.geometry("500x450")
    janela_comprar_passagem.configure(fg_color='white')

    titulo = ctk.CTkLabel(janela_comprar_passagem, text="Escolha os dados", text_color='black', font=('Arial', 25))
    titulo.pack(pady=10)

    data_saida = ctk.CTkEntry(janela_comprar_passagem, placeholder_text="Digite a data de saida (DD/MM/AAAA)...", width=320, height=50)
    data_saida.pack(pady=10)

    linha = ctk.CTkEntry(janela_comprar_passagem, placeholder_text="Digite a linha que deseja adicionar...", width=320, height=50)
    linha.pack(pady=10)

    linhas_onibus_disponiveis = Conexao.retornar_linhas_onibus(linhas)

    scrolllist = ctk.CTkScrollableFrame(janela_comprar_passagem, orientation=ctk.VERTICAL, width=320) # Cria uma parte de scroll na janela
    scrolllist.pack(pady=5)

    for lin_dados in linhas_onibus_disponiveis:
        ctk.CTkLabel(scrolllist, text=lin_dados).pack(pady=2)

    # Cria o campo dos botões abaixo, para não conflitar com o espaço
    janela_botoes = ctk.CTkFrame(janela_comprar_passagem, fg_color="white")
    janela_botoes.pack(pady=5)

    def buscar_lugares():
        try:
            data = datetime.strptime(data_saida.get(), "%d/%m/%Y")

            linha_nome = linha.get()

            for linha_existente, lista_onibus in linhas.items():
                if linha_existente.nome == linha_nome:
                    for onibus in lista_onibus:
                        if onibus.data_formatada == data:
                            janela_reservar_lugar(linhas, linha_existente, data, data_user)
                            return
                    Conexao.janela_aviso("Onibus nao pertecem a essa linha!", "red")
                    return
            Conexao.janela_aviso("Linha no existe!", "red")

        except ValueError:
            Conexao.janela_aviso("Dados inválidos. Verifique Informacoes passadas.", "red")

        except Exception as e:
            Conexao.janela_aviso(f"Erro: {e}", "red")

    btn_inserir = ctk.CTkButton(janela_botoes,text="Olhar lugares", command= buscar_lugares)
    btn_inserir.pack(side="left", padx=5)   
    # A funcao datetime.strptime converte o que foi recebido na caixa para valores de data       

    btn_voltar = ctk.CTkButton(janela_botoes, text="Voltar", command=janela_comprar_passagem.destroy, fg_color="#4682B4", text_color="white")
    btn_voltar.pack(side="left", padx=5) 
            
            
                    


#----------------------------------------------------------------------------------__#




# Menu de opcoes principal
titulo = ctk.CTkLabel(janela_inicial, text="Sistema Rodoviario", font=("Arial Rounded MT Bold", 30), text_color="black", fg_color="transparent") # Titulo central
titulo.pack(pady=(20, 20))

Opcoes = ctk.CTkLabel(janela_inicial, text="Opcoes disponiveis", font=("Arial Rounded MT Bold", 20), text_color="black", fg_color="transparent")
Opcoes.pack(pady=(20, 20))

botao1 = ctk.CTkButton(janela, text="Adicionar uma linha", command=janela_adicionar_linha, width=270, height=70, font=("Arial Rounded MT Bold", 19))
botao1.pack(pady=15)

botao2 = ctk.CTkButton(janela, text="Adicionar um onibus", command=janela_adicionar_onibus, width=270, height=70, font=("Arial Rounded MT Bold", 19))
botao2.pack(pady=15)

botao3 = ctk.CTkButton(janela, text="Comprar passagem", command=janela_comprar_passagem, width=270, height=70, font=("Arial Rounded MT Bold", 19))
botao3.pack(pady=15)

botao4 = ctk.CTkButton(janela, text="Editar linhas", command=" ", width=270, height=70, font=("Arial Rounded MT Bold", 19))
botao4.pack(pady=15)

botao5 = ctk.CTkButton(janela, text="Relatorios", command=" ", width=270, height=70, font=("Arial Rounded MT Bold", 19))
botao5.pack(pady=15)


"""


linha1 = Linha("Div", "BH", "14:20", 12)
onibus1 = Onibus("21/11")
onibus2 = Onibus("20/11")


Conexao.adicionar_onibus(linhas, linha1, onibus1)



Conexao.adicionar_onibus(linhas, linha1, onibus2)

for linha, onibus in linhas.items():
    print(linha.nome, end=": ")
    for oni in onibus:
        print(oni.nome, end=", ")

print()
"""

janela.mainloop()


