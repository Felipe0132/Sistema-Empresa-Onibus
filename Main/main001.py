from Linhas.Linha import Linha # Importando biblioteca das linhas
from Onibus.Onibus import Onibus # Importando biblioteca dos onibus
import Conexao.Conexao as Conexao # Importando biblioteca de conexão
import datetime # Importando biblioteca do formato de horas
import customtkinter as ctk # Importando biblioteca de interface grafica
import tkinter as tk # Importando biblioteca de interface grafica antiga

# Codigo para rodar -> python3 -m Main.main001

linhas = dict() # Criando o dicionario que contem key -> Obj linha e value -> lista de Obj onibus

datetime_user = datetime.datetime.now() # Define os dados do usuario

#FUNÇOES PARA INTERFACE

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue") 

# Criar janela principal

janela = ctk.CTk()
janela.title("Empresa Rodoviaria") # Nome da janela
janela.geometry("800x850") # Tamanho

janela_inicial = ctk.CTkFrame(janela, fg_color="white") # Cor de fundo
janela_inicial.pack(fill="both", expand=True) # Cria um widget, fill é o preenchimento, expand seria a responsividade do tamanho


# Funcoes para abrir janelas segundarias e terciarias

def janela_adicionar_linha(): # Funcao para criar a janela responsavel para recolher informacoes de adicionar linha
    janela_adicionar_linha = ctk.CTkToplevel(janela) # Janela herda de uma janela principal maior
    janela_adicionar_linha.title("Adicionando Linha") # Titulo
    janela_adicionar_linha.geometry("500x450") # Tamanho
    janela_adicionar_linha.configure(fg_color='white') # Cor de fundo

    titulo = ctk.CTkLabel(janela_adicionar_linha, text="Adicionar dados", text_color='black', font=('Arial', 25))
    titulo.pack(pady=10) # Titulo da jaenla

    cidade_origem = ctk.CTkEntry(janela_adicionar_linha, placeholder_text="Digite a cidade de origem...", width=320, height=50)
    cidade_origem.pack(pady=10) # Espaco de receber a cidade de origem

    cidade_destino = ctk.CTkEntry(janela_adicionar_linha, placeholder_text="Digite a cidade de destino...", width=320, height=50)
    cidade_destino.pack(pady=10) # Espaco de receber cidade de destino

    horario_saida = ctk.CTkEntry(janela_adicionar_linha, placeholder_text="Digite a hora de saída do ônibus (HR:MIM): ", width=320, height=50)
    horario_saida.pack(pady=10) # Espaco de receber horario de saida

    valor = ctk.CTkEntry(janela_adicionar_linha, placeholder_text="Digite o valor R$... ", width=320, height=50)
    valor.pack(pady=10) # Espaco de receber o valor

    # Cria o campo dos botões abaixo, para não conflitar com o espaço
    janela_botoes = ctk.CTkFrame(janela_adicionar_linha, fg_color="white")
    janela_botoes.pack(pady=10)

    def inserir(): # Pelo motivo da interface grafica nao aceitar funcoes com parametros, cria-se uma para usar e manipular na interface grafica
        try:
            hora = datetime.datetime.strptime(horario_saida.get(), "%H:%M") # Passa a hora para o formato padrao
            preco = float(valor.get()) # Passa o valor para float

            nova_linha = Linha(cidade_origem.get(), cidade_destino.get(), hora, preco) # Pegando os dados da interface e transformando na linha

            Conexao.adicionar_linha(linhas, nova_linha) # Funcao de adicionar linha

        except ValueError: # Erro de tipo de dado
            Conexao.janela_aviso("Dados inválidos. Verifique Informacoes passadas.", "red")

        except Exception as e: # Erro inesperado
            Conexao.janela_aviso(f"Erro: {e}", "red")

    btn_inserir = ctk.CTkButton(janela_botoes,text="Inserir", command=inserir)
    btn_inserir.pack(side="left", padx=10) # Botao que ao ser clicado chama a funcao inserir

    btn_voltar = ctk.CTkButton(janela_botoes, text="Voltar", command=janela_adicionar_linha.destroy, fg_color="#4682B4", text_color="white")
    btn_voltar.pack(side="left", padx=10) # Botao de voltar que destroi a atual

def janela_adicionar_onibus(): # Funcao para criar a janela responsavel para recolher informacoes de adicionar linha
    janela_adicionar_onibus = ctk.CTkToplevel(janela) # Janela herda de uma janela principal maior
    janela_adicionar_onibus.title("Adicionando Onibus") # Titulo da janela
    janela_adicionar_onibus.geometry("500x690") # Tamanho da janela
    janela_adicionar_onibus.configure(fg_color='white') # Cor de fundo

    titulo = ctk.CTkLabel(janela_adicionar_onibus, text="Adicionar dados", text_color='black', font=('Arial', 25))
    titulo.pack(pady=10) # Titulo na janela

    data_saida = ctk.CTkEntry(janela_adicionar_onibus, placeholder_text="Digite a data de saida (DD/MM/AAAA)...", width=320, height=50)
    data_saida.pack(pady=10) # Espaco de receber data de partida

    linha_nome = ctk.CTkEntry(janela_adicionar_onibus, placeholder_text="Digite a linha que deseja adicionar...", width=320, height=50)
    linha_nome.pack(pady=10) # Espaco de receber nome da linha

    texto = ctk.CTkLabel(janela_adicionar_onibus, text="Lista de Linhas Disponiveis", text_color='black', font=('Arial', 22)) # Mostrando as linhas que podem receber onibus
    texto.pack(pady=10) # Texto explicativo

    linhas_disponiveis = Conexao.retornar_linhas(linhas) # Aqui cria uma lista de linhas para puder imprimir os dados melhor

    scrolllist = ctk.CTkScrollableFrame(janela_adicionar_onibus, orientation=ctk.VERTICAL, width=320) # Cria uma parte de scroll na janela
    scrolllist.pack(pady=5)

    for linha_disp in linhas_disponiveis:
        ctk.CTkLabel(scrolllist, text=linha_disp).pack(pady=2) # Aqui ele coloca na caixa de scroll os itens da lista

    # Cria o campo dos botões abaixo, para não conflitar com o espaço
    janela_botoes = ctk.CTkFrame(janela_adicionar_onibus, fg_color="white")
    janela_botoes.pack(pady=5)

    def inserir(): # Pelo motivo da interface grafica nao aceitar funcoes com parametros, cria-se uma para usar e manipular na interface grafica
        try:
            data = datetime.datetime.strptime(data_saida.get(), "%d/%m/%Y") # Transforma ela em String
            
            novo_onibus = Onibus(data) # Pegando os dados da interface e transformando na linha

            for linha_existente in linhas:
                if linha_existente.nome == linha_nome.get():
                    Conexao.adicionar_onibus(linhas, linha_existente, novo_onibus) # Funcao de adicionar linha

            

        except ValueError: # Erro de tipo de dado
            Conexao.janela_aviso("Dados inválidos. Verifique Informacoes passadas.", "red")

        except Exception as e: # Erro inesperado
            Conexao.janela_aviso(f"Erro: {e}", "red")

    btn_inserir = ctk.CTkButton(janela_botoes,text="Inserir", command= inserir)
    btn_inserir.pack(side="left", padx=5) # Funcao que ao ser clicado entra na funcao inserir     

    btn_voltar = ctk.CTkButton(janela_botoes, text="Voltar", command=janela_adicionar_onibus.destroy, fg_color="#4682B4", text_color="white")
    btn_voltar.pack(side="left", padx=5) # Funcao voltar que destroi a janela atual

def janela_reservar_lugar(linhas, linha_existente, onibus): # Janela final da reserva de lugar

    if not Conexao.verifica_reserva(linhas, linha_existente, onibus): # Funcao que é o primeiro teste se pode reservar
        return


    janela_reservar_lugar = ctk.CTkToplevel(janela) # Janela herda de uma janela principal maior
    janela_reservar_lugar.title("Lugares disponiveis") # Titulo da janela
    janela_reservar_lugar.geometry("500x450") # tamanho da janela
    janela_reservar_lugar.configure(fg_color='white') # Cor de fundo

    titulo = ctk.CTkLabel(janela_reservar_lugar, text="Escolha um lugar", text_color='black', font=('Arial', 25))
    titulo.pack(pady=10) # Titulo na janela

    lugar_escolhido = ctk.CTkEntry(janela_reservar_lugar, placeholder_text="Digite um lugar disponivel (1 a 20)...", width=320, height=50)
    lugar_escolhido.pack(pady=10) # Lugar que recebe o assento desejado

    texto = ctk.CTkLabel(janela_reservar_lugar, text="Lugares", text_color='black', font=('Arial', 25))
    texto.pack(pady=10) # Texto explicativo

    lugares_onibus = ctk.CTkFrame(janela_reservar_lugar, fg_color='white')
    lugares_onibus.pack(pady=5) # Aqui vai criar a sessao para imprirmir os lugares do onibus

    # Frame onde os lugares serão exibidos
    frame_lugares = ctk.CTkFrame(janela_reservar_lugar, fg_color="white")
    frame_lugares.pack(pady=2)  

    for coluna, numero in enumerate(range(1, 20 + 1)):
        if numero in onibus.assentos_disponiveis: # Aqui no if ele coloca verde para disponiveis e vermelhor indisponiveis
            cor = 'green'
        else:
            cor = 'red'

        lugares = ctk.CTkLabel(frame_lugares, text=str(numero), text_color=cor)
        lugares.pack(side="left", padx=3) # Exibe os assentos


    def reservar_lugar(): # Funcao feita por motivo de ser limitado o uso de funcoes com parametros em interfaces
        try:
            lugar = int(lugar_escolhido.get()) # Transforma o dado em inteiro

            if len(onibus.assentos_disponiveis) == 0: # Se nao haver lugar disponivel
                Conexao.janela_aviso("Nenhum assento disponivel!", "red")

            onibus.reservar_assento(lugar) # Se tiver ok ele passar para a funcao de reservar

        except ValueError: # Erro de tipo de valor
            Conexao.janela_aviso("Tipo invalido!","red")

        except Exception as e: # Erro inesperado
            Conexao.janela_aviso(f"Error: {e}", "red")

    # Cria o campo dos botões abaixo, para não conflitar com o espaço
    janela_botoes = ctk.CTkFrame(janela_reservar_lugar, fg_color="white")
    janela_botoes.pack(pady=4)

    btn_marcar_lugar = ctk.CTkButton(janela_botoes,text="Marcar Lugar", command= reservar_lugar, height=40, width=150, font=("Arial", 16))
    btn_marcar_lugar.pack(side="left", padx=20, pady=4)   # Botao que ao ser clicado entra na funcao reservar_lugar     

    btn_voltar = ctk.CTkButton(janela_botoes, text="Voltar", command=janela_reservar_lugar.destroy, fg_color="#4682B4", text_color="white", height=40, width=150, font=("Arial", 16))
    btn_voltar.pack(side="left", padx=20, pady=4) # Botao que quando clicado destroi a janela atual

def janela_comprar_passagem():
    janela_comprar_passagem = ctk.CTkToplevel(janela) # Janela secundaria, nivel filha de janela
    janela_comprar_passagem.title("Comprando passagem") # Titulo da janela
    janela_comprar_passagem.geometry("800x500") # Tamanho
    janela_comprar_passagem.configure(fg_color='white') # Cor de fundo

    titulo = ctk.CTkLabel(janela_comprar_passagem, text="Escolha os dados", text_color='black', font=('Arial', 25))
    titulo.pack(pady=7) # Titulo na janela

    data_saida = ctk.CTkEntry(janela_comprar_passagem, placeholder_text="Digite a data de saida (DD/MM/AAAA)...", width=320, height=50)
    data_saida.pack(pady=7) # Lugar que recebe a data

    linha = ctk.CTkEntry(janela_comprar_passagem, placeholder_text="Digite a linha que deseja adicionar...", width=320, height=50)
    linha.pack(pady=7) # Lugar que recebe a linha

    texto = ctk.CTkLabel(janela_comprar_passagem, text="Lista de Linhas Disponiveis", text_color='black', font=('Arial', 22)) # Mostrando as linhas que podem receber onibus
    texto.pack(pady=7) # Texto explicativo

    linhas_disponiveis = Conexao.retornar_linhas_onibus(linhas) # Aqui cria uma lista de linhas para puder imprimir os dados melhor

    # Comando que cria um frame de scroll proprio para scroll vertical e horizontal
    ctk_frame_scroll = ctk.CTkFrame(janela_comprar_passagem, fg_color="white")
    ctk_frame_scroll.pack(pady=5)

    # CANVAS (Tkinter)
    canvas = tk.Canvas(ctk_frame_scroll, width=500, height=200)
    canvas.pack(side="left", fill="both", expand=True)

    # Nos codigos abaixo sera possivel configurar para rolagem vertical e horizontal
    scroll_y = tk.Scrollbar(ctk_frame_scroll, orient="vertical", command=canvas.yview)
    scroll_y.pack(side="right", fill="y")

    scroll_x = tk.Scrollbar(janela_comprar_passagem, orient="horizontal", command=canvas.xview)
    scroll_x.pack(fill="x")

    canvas.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

    # INTERIOR DO CANVAS
    frame_interno = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame_interno, anchor="nw")

    # Coloca no frame as linhas disponiveis
    for linha_disp in linhas_disponiveis:
        tk.Label(frame_interno, text=linha_disp, anchor="w").pack(pady=2)

    # Atualizar área scrollável
    def ajustar_scroll(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    frame_interno.bind("<Configure>", ajustar_scroll)

    # Cria o campo dos botões abaixo, para não conflitar com o espaço
    janela_botoes = ctk.CTkFrame(janela_comprar_passagem, fg_color="white")
    janela_botoes.pack(pady=3)

    def buscar_lugares(): # Funcao feita por motivo de ser limitado o uso de funcoes com parametros em interfaces
        try:
            data = datetime.datetime.strptime(data_saida.get(), "%d/%m/%Y") # Transforma a data no formato usado
            data = data.strftime("%d/%m/%Y") # Formata ela
            linha_nome = linha.get() # Pega o nome da linha

            for linha_existente, lista_onibus in linhas.items(): # Percorre todo o dicionario
                if linha_existente.nome == linha_nome: # Se encontra a linha
                    for onibus in lista_onibus: # Percorre todos os onibus
                        if onibus.data_formatada == data: # Se encontrar o onibus
                            janela_reservar_lugar(linhas, linha_existente, onibus) # Entra na funcao que chama outra janela
                            return
        
                    # Só cai aqui se não achou nenhum onibus igual
                    Conexao.janela_aviso("Ônibus não pertencem a essa linha!", "red")
                    return

            # Só chega aqui se nao ahcar a linha
            Conexao.janela_aviso("Linha não existe!", "red")

        except ValueError: # Erro de dado
            Conexao.janela_aviso("Dados inválidos. Verifique Informacoes passadas.", "red")

        except Exception as e: # Erro inesperado
            Conexao.janela_aviso(f"Erro: {e}", "red")

    btn_inserir = ctk.CTkButton(janela_botoes,text="Olhar lugares", command= buscar_lugares)
    btn_inserir.pack(side="left", padx=3)   
    # A funcao datetime.strptime converte o que foi recebido na caixa para valores de data       

    btn_voltar = ctk.CTkButton(janela_botoes, text="Voltar", command=janela_comprar_passagem.destroy, fg_color="#4682B4", text_color="white")
    btn_voltar.pack(side="left", padx=3) 
            
def janela_editar_rota(): # Janela para editar rota
    janela_editar_rota = ctk.CTkToplevel(janela) # Janela secundaria, nivel filha de janela
    janela_editar_rota.title("Editando Rota") # Titulo da janela
    janela_editar_rota.geometry("500x550") # Tamanho
    janela_editar_rota.configure(fg_color='white') # Cor de fundo

    titulo = ctk.CTkLabel(janela_editar_rota, text="Novos Dados", text_color='black', font=('Arial', 25))
    titulo.pack(pady=7) # Titulo da janela

    linha_original = ctk.CTkEntry(janela_editar_rota, placeholder_text="Digite a linha que deseja editar...", width=320, height=50)
    linha_original.pack(pady=5) # Lugar que recebe o nome que deseja alterar

    cidade_origem = ctk.CTkEntry(janela_editar_rota, placeholder_text="Digite a cidade origem...", width=320, height=50)
    cidade_origem.pack(pady=5) # Lugar que recebe novo lugar de origem

    cidade_destino = ctk.CTkEntry(janela_editar_rota, placeholder_text="Digite a cidade destino...", width=320, height=50)
    cidade_destino.pack(pady=5) # Lugar que recebe novo lugar de destino

    texto = ctk.CTkLabel(janela_editar_rota, text="Lista de Linhas Disponiveis", text_color='black', font=('Arial', 22)) # Mostrando as linhas que podem receber onibus
    texto.pack(pady=5) # Texto explicativo

    linhas_disponiveis = Conexao.retornar_linhas(linhas) # Aqui cria uma lista de linhas para puder imprimir os dados melhor

    scrolllist = ctk.CTkScrollableFrame(janela_editar_rota, orientation=ctk.VERTICAL, width=320) # Cria uma parte de scroll na janela
    scrolllist.pack(pady=5)

    for linha_disp in linhas_disponiveis:
        ctk.CTkLabel(scrolllist, text=linha_disp).pack(pady=2) # Aqui ele coloca na caixa de scroll os itens da lista

    def editar(): # Funcao feita por motivo de ser limitado o uso de funcoes com parametros em interfaces
        try:
            Conexao.editar_rota(linhas, linha_original.get(), cidade_origem.get(), cidade_destino.get()) # joga os argumentos na funcao principal
        except ValueError: # Erro de tipo
            Conexao.janela_aviso("Dados Invalidos!", "red")
        except Exception as e: # Erro inesperado
            Conexao.janela_aviso(f"Error: {e}","red")

    janela_botoes = ctk.CTkFrame(janela_editar_rota, fg_color="white")
    janela_botoes.pack(pady=3) # Lugar que configura botoes
    
    btn_editar = ctk.CTkButton(janela_botoes,text="Editar", command=editar)
    btn_editar.pack(side="left", padx=3) # Botao que chama a funcao editar
 
    btn_voltar = ctk.CTkButton(janela_botoes, text="Voltar", command=janela_editar_rota.destroy, fg_color="#4682B4", text_color="white")
    btn_voltar.pack(side="left", padx=3) # Botao que destroi a janela atual

def janela_editar_horario():
    janela_editar_horario = ctk.CTkToplevel(janela) # Janela herda da janela principal
    janela_editar_horario.title("Editar Horario") # Titulo da janela
    janela_editar_horario.geometry("500x600") # Tamanho
    janela_editar_horario.configure(fg_color='white') # Cor de fundo

    titulo = ctk.CTkLabel(janela_editar_horario, text="Novos Dados", text_color='black', font=('Arial', 25))
    titulo.pack(pady=5)

    linha_original = ctk.CTkEntry(janela_editar_horario, placeholder_text="Digite a linha que deseja editar...", width=320, height=50)
    linha_original.pack(pady=2)

    novo_horario = ctk.CTkEntry(janela_editar_horario, placeholder_text="Digite o novo horario...", width=320, height=50)
    novo_horario.pack(pady=2)

    linhas_disponiveis = Conexao.retornar_linhas(linhas) # Aqui cria uma lista de linhas para puder imprimir os dados melhor

    scrolllist = ctk.CTkScrollableFrame(janela_editar_horario, orientation=ctk.VERTICAL, width=320) # Cria uma parte de scroll na janela
    scrolllist.pack(pady=5)

    for linha_disp in linhas_disponiveis:
        ctk.CTkLabel(scrolllist, text=linha_disp).pack(pady=2) # Aqui ele coloca na caixa de scroll os itens da lista


    def editar():
        try:
            horario_novo = datetime.datetime.strptime(novo_horario.get(), "%H:%M") # Configura para formato padrao

            Conexao.editar_horario(linhas, str(linha_original.get()), horario_novo) # Chama a funcao principal
        except ValueError: # Erro de tipo
            Conexao.janela_aviso("Dados Invalidos!", "red")
        except Exception as e: # Erro inesperado
            Conexao.janela_aviso(f"Error: {e}", "red")

    # Cria o campo dos botões abaixo, para não conflitar com o espaço
    janela_botoes = ctk.CTkFrame(janela_editar_horario, fg_color="white")
    janela_botoes.pack(pady=3)

    btn_editar = ctk.CTkButton(janela_botoes,text="Editar", command= editar)
    btn_editar.pack(side="left", padx=3)   # Botao que ao clicar chama a funcao editar    

    btn_voltar = ctk.CTkButton(janela_botoes, text="Voltar", command=janela_editar_horario.destroy, fg_color="#4682B4", text_color="white")
    btn_voltar.pack(side="left", padx=3)  # Botao que destroi janela atual

def janela_remover_onibus():
    janela_remover_onibus = ctk.CTkToplevel(janela) # Janela herda da janela principal
    janela_remover_onibus.title("Removendo Onibus") # Titulo da janela
    janela_remover_onibus.geometry("500x450") # Tamanho
    janela_remover_onibus.configure(fg_color='white') # Cor de fundo

    titulo = ctk.CTkLabel(janela_remover_onibus, text="Removendo Dados", text_color='black', font=('Arial', 25))
    titulo.pack(pady=5) # Titulo na janela

    linha_original = ctk.CTkEntry(janela_remover_onibus, placeholder_text="Digite a linha que deseja editar...", width=320, height=50)
    linha_original.pack(pady=2) # Recebe a linha desejavel

    data_onibus = ctk.CTkEntry(janela_remover_onibus, placeholder_text="Digite a data do onibus...", width=320, height=50)
    data_onibus.pack(pady=2) # Recebe a data

    texto = ctk.CTkLabel(janela_remover_onibus, text="Lista de Linhas Disponiveis", text_color='black', font=('Arial', 22)) # Mostrando as linhas que podem receber onibus
    texto.pack(pady=2) # Texto explicativo

    linhas_disponiveis = Conexao.retornar_linhas_onibus(linhas)

    # Criacao para o frame dos scrolls
    ctk_frame_scroll = ctk.CTkFrame(janela_remover_onibus, fg_color="white")
    ctk_frame_scroll.pack(pady=5)

    # CANVAS (Tkinter)
    canvas = tk.Canvas(ctk_frame_scroll, width=500, height=200)
    canvas.pack(side="left", fill="both", expand=True)

    # Configuracao para o scroll vertical e horinzontal
    scroll_y = tk.Scrollbar(ctk_frame_scroll, orient="vertical", command=canvas.yview)
    scroll_y.pack(side="right", fill="y")

    scroll_x = tk.Scrollbar(janela_remover_onibus, orient="horizontal", command=canvas.xview)
    scroll_x.pack(fill="x")

    canvas.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

    # INTERIOR DO CANVAS
    frame_interno = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame_interno, anchor="nw")

    # Preencher com as linhas disponiveis
    for linha_disp in linhas_disponiveis:
        tk.Label(frame_interno, text=linha_disp, anchor="w").pack(pady=2)

    # Atualizar área scrollável
    def ajustar_scroll(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    frame_interno.bind("<Configure>", ajustar_scroll)


    def editar():
        try:
            data = datetime.datetime.strptime(data_onibus.get(), "%d/%m/%Y") # Confira o dado
            data = data.strftime("%d/%m/%Y") # Transfomra no objeto de datas

            Conexao.remover_onibus(linhas, str(linha_original.get()), data) # Chama a funcao principal
        except ValueError: # Erro por tipo
            Conexao.janela_aviso("Dados Invalidos!", "red")
        except Exception as e: # Erro inesperado
            Conexao.janela_aviso(f"Error: {e}","red")

    # Cria o campo dos botões abaixo, para não conflitar com o espaço
    janela_botoes = ctk.CTkFrame(janela_remover_onibus, fg_color="white")
    janela_botoes.pack(pady=2) 

    btn_editar = ctk.CTkButton(janela_botoes,text="Editar", command=editar)
    btn_editar.pack(side="left", padx=3) # janela que chama a funcao editar
 
    btn_voltar = ctk.CTkButton(janela_botoes, text="Voltar", command=janela_remover_onibus.destroy, fg_color="#4682B4", text_color="white")
    btn_voltar.pack(side="left", padx=3) # Botao que destroi a janela atual

def janela_remover_linha():
    janela_remover_linha = ctk.CTkToplevel(janela) # Janela herda da janela principal
    janela_remover_linha.title("Remover Linha") # Titulo da janela
    janela_remover_linha.geometry("500x600") # Tamanho
    janela_remover_linha.configure(fg_color='white') # Cor de fundo

    titulo = ctk.CTkLabel(janela_remover_linha, text="Linha", text_color='black', font=('Arial', 25))
    titulo.pack(pady=5)

    linha_original = ctk.CTkEntry(janela_remover_linha, placeholder_text="Digite a linha que deseja remover...", width=320, height=50)
    linha_original.pack(pady=2)

    linhas_disponiveis = Conexao.retornar_linhas(linhas) # Aqui cria uma lista de linhas para puder imprimir os dados melhor

    scrolllist = ctk.CTkScrollableFrame(janela_remover_linha, orientation=ctk.VERTICAL, width=320) # Cria uma parte de scroll na janela
    scrolllist.pack(pady=5)

    for linha_disp in linhas_disponiveis:
        ctk.CTkLabel(scrolllist, text=linha_disp).pack(pady=2) # Aqui ele coloca na caixa de scroll os itens da lista


    def editar():
        try:
            Conexao.remover_linha(linhas, str(linha_original.get())) # Chama a funcao principal
        except ValueError: # Erro de tipo
            Conexao.janela_aviso("Dados Invalidos!", "red")
        except Exception as e: # Erro inesperado
            Conexao.janela_aviso(f"Error: {e}", "red")

    # Cria o campo dos botões abaixo, para não conflitar com o espaço
    janela_botoes = ctk.CTkFrame(janela_remover_linha, fg_color="white")
    janela_botoes.pack(pady=3)

    btn_editar = ctk.CTkButton(janela_botoes,text="Editar", command= editar)
    btn_editar.pack(side="left", padx=3)   # Botao que ao clicar chama a funcao editar    

    btn_voltar = ctk.CTkButton(janela_botoes, text="Voltar", command=janela_remover_linha.destroy, fg_color="#4682B4", text_color="white")
    btn_voltar.pack(side="left", padx=3)  # Botao que destroi janela atual

def janela_editar_linhas():
    janela_editar_linhas = ctk.CTkToplevel(janela) # Janela herda da janela principal
    janela_editar_linhas.title("Opcoes de Edicao") # titulo da janela
    janela_editar_linhas.geometry("500x450") # Tamanho
    janela_editar_linhas.configure(fg_color='white') # Cor de fundo

    titulo = ctk.CTkLabel(janela_editar_linhas, text="Opcoes", text_color='black', font=('Arial', 25))
    titulo.pack(pady=10) # Titulo na janela

    editar_rotas = ctk.CTkButton(janela_editar_linhas, text="Editar Rota", command=janela_editar_rota, width=270, height=70, font=("Arial Rounded MT Bold", 19))
    editar_rotas.pack(pady=15) # Botao que chama a janela de editar rota

    editar_horario = ctk.CTkButton(janela_editar_linhas, text="Editar Horario", command=janela_editar_horario, width=270, height=70, font=("Arial Rounded MT Bold", 19))
    editar_horario.pack(pady=15) # Botao que chama a janela editar horario

    remover_onibus = ctk.CTkButton(janela_editar_linhas, text="Remover Onibus", command=janela_remover_onibus, width=270, height=70, font=("Arial Rounded MT Bold", 19))
    remover_onibus.pack(pady=15) # Botao que ao ser clicado, chama a janela de remover onibus

    remover_linha = ctk.CTkButton(janela_editar_linhas, text="Remover Linha", command=janela_remover_linha, width=270, height=70, font=("Arial Rounded MT Bold", 19))
    remover_linha.pack(pady=15) # Botao que ao ser clicado, chama a janela de remover Linha

    # Cria o campo dos botões abaixo, para não conflitar com o espaço
    janela_botoes = ctk.CTkFrame(janela_editar_linhas, fg_color="white")
    janela_botoes.pack(pady=2)
 
    btn_voltar = ctk.CTkButton(janela_botoes, text="Voltar", command=janela_editar_linhas.destroy, fg_color="#4682B4", text_color="white")
    btn_voltar.pack(side="left", padx=3) # Destroi a janela atual

def janela_vendas_mes_linha():
    janela_vendas_mes_linha = ctk.CTkToplevel(janela) # janela herda da janela principal
    janela_vendas_mes_linha.title("Vendas do mes de uma linha") # Titulo da janela
    janela_vendas_mes_linha.geometry("500x450") # Tamanho
    janela_vendas_mes_linha.configure(fg_color='white') # Cor de fundo

    linha_desejavel = ctk.CTkEntry(janela_vendas_mes_linha, placeholder_text="Digite a linha que deseja olhar...", width=320, height=50)
    linha_desejavel.pack(pady=2) # Pega a linha que deseja alterar

    mes_desejado = ctk.CTkEntry(janela_vendas_mes_linha, placeholder_text="Digite o mes que deseja olhar", width=320, height=50)
    mes_desejado.pack(pady=2) # Pega o mes que deseja alterar

    texto = ctk.CTkLabel(janela_vendas_mes_linha, text="Lista de Linhas Disponiveis", text_color='black', font=('Arial', 22)) # Mostrando as linhas que podem receber onibus
    texto.pack(pady=2) # Texto explicativo

    linhas_disponiveis = Conexao.retornar_linhas(linhas) # Aqui cria uma lista de linhas para puder imprimir os dados melhor

    scrolllist = ctk.CTkScrollableFrame(janela_vendas_mes_linha, orientation=ctk.VERTICAL, width=320) # Cria uma parte de scroll na janela
    scrolllist.pack(pady=5)

    for linha_disp in linhas_disponiveis:
        ctk.CTkLabel(scrolllist, text=linha_disp).pack(pady=2) # Aqui ele coloca na caixa de scroll os itens da lista
    
    def gerar_relatorio():# Funcao feita por motivo de ser limitado o uso de funcoes com parametros em interfaces
        try:
            Conexao.calcular_vendas_do_mes(linhas, str(linha_desejavel.get()), int(mes_desejado.get())) # Chama a funcao principal
        except ValueError: # Erro de tipo
            Conexao.janela_aviso("Dados Invalidos!", "red")
        except Exception as e: # Erro inesperado
            Conexao.janela_aviso(f"Error: {e}","red")

    def gerar_relatorio_txt(): # Funcao feita por motivo de ser limitado o uso de funcoes com parametros em interfaces
        try:
            Conexao.salvar_relatorio_vendas_txt(linhas, str(linha_desejavel.get()), int(mes_desejado.get()))
        except ValueError: # Erro de tipo
            Conexao.janela_aviso("Dados Invalidos!", "red")
        except Exception as e: # Erro inesperado
            Conexao.janela_aviso(f"Error: {e}", "red")
        
    # Cria o campo dos botões abaixo, para não conflitar com o espaço
    janela_botoes = ctk.CTkFrame(janela_vendas_mes_linha, fg_color="white")
    janela_botoes.pack(pady=2) 

    btn_gerar = ctk.CTkButton(janela_botoes,text="Gerar", command=gerar_relatorio)
    btn_gerar.pack(side="left", padx=3) # Gera na interface grafica

    btn_gerar_txt = ctk.CTkButton(janela_botoes,text="Gerar em .txt", command=gerar_relatorio_txt)
    btn_gerar_txt.pack(side="left", padx=3)  # Botao que chama a funcao gerar relatorio txt
 
    btn_voltar = ctk.CTkButton(janela_botoes, text="Voltar", command=janela_vendas_mes_linha.destroy, fg_color="#4682B4", text_color="white")
    btn_voltar.pack(side="left", padx=3)    # Botao que destroi janela atual

def janela_porcentual_medio_dia():
    janela_porcentual_medio_dia = ctk.CTkToplevel(janela) # Janela herdada da janela principal
    janela_porcentual_medio_dia.title("Porcentual media por dia") # Titulo da janela
    janela_porcentual_medio_dia.geometry("500x450") # Tamanho
    janela_porcentual_medio_dia.configure(fg_color='white') # Cor de fundo

    titulo = ctk.CTkLabel(janela_porcentual_medio_dia, text="Porcentual Media da linha", text_color='black', font=('Arial', 25))
    titulo.pack(pady=10)  # Titulo na janela

    linha_desejavel = ctk.CTkEntry(janela_porcentual_medio_dia, placeholder_text="Digite a linha que deseja olhar...", width=320, height=50)
    linha_desejavel.pack(pady=2) # Lugar que recebe o nome da linha que deseja olhar

    linhas_disponiveis = Conexao.retornar_linhas(linhas) # Aqui cria uma lista de linhas para puder imprimir os dados melhor

    scrolllist = ctk.CTkScrollableFrame(janela_porcentual_medio_dia, orientation=ctk.VERTICAL, width=320) # Cria uma parte de scroll na janela
    scrolllist.pack(pady=5)

    for linha_disp in linhas_disponiveis:
        ctk.CTkLabel(scrolllist, text=linha_disp).pack(pady=2) # Aqui ele coloca na caixa de scroll os itens da lista    

    def gerar(): # Funcao feita por motivo de ser limitado o uso de funcoes com parametros em interfaces
        try:
            Conexao.matriz_percentual_ocupacao(linhas, str(linha_desejavel.get())) # Chama a funcao principal
        except ValueError: # Erro de tipo
            Conexao.janela_aviso("Dados invalidos!", "red")
        except Exception as e: # Erro inesperado
            Conexao.janela_aviso(f"Erro: {e}", "red")

    def gerar_txt(): # Funcao feita por motivo de ser limitado o uso de funcoes com parametros em interfaces
        try:
            Conexao.matriz_percentual_ocupacao_txt(linhas, str(linha_desejavel.get())) # Chama a funcao principal
        except ValueError: # Erro de tipo
            Conexao.janela_aviso("Dados invalidos!", "red")
        except Exception as e: # Erro inesperado
            Conexao.janela_aviso(f"Erro: {e}", "red")

    # Cria o campo dos botões abaixo, para não conflitar com o espaço
    janela_botoes = ctk.CTkFrame(janela_porcentual_medio_dia, fg_color="white")
    janela_botoes.pack(pady=2)

    btn_gerar = ctk.CTkButton(janela_botoes,text="Gerar", command=gerar)
    btn_gerar.pack(side="left", padx=3) # Botao que chama a funcao gerar somente em janela

    btn_gerar_txt = ctk.CTkButton(janela_botoes,text="Gerar em .txt", command=gerar_txt)
    btn_gerar_txt.pack(side="left", padx=3)  # Botao que chama a funcao gerar txt
 
    btn_voltar = ctk.CTkButton(janela_botoes, text="Voltar", command=janela_porcentual_medio_dia.destroy, fg_color="#4682B4", text_color="white")
    btn_voltar.pack(side="left", padx=3) # Botao que destroi a janela atual

def janela_relatorios():
    janela_relatorios = ctk.CTkToplevel(janela) # Janela herda da janela principal
    janela_relatorios.title("Opcoes de Relatorio") # Titulo da janela
    janela_relatorios.geometry("500x450") # Tamanho
    janela_relatorios.configure(fg_color='white') # Cor de fundo

    titulo = ctk.CTkLabel(janela_relatorios, text="Opcoes", text_color='black', font=('Arial', 25))
    titulo.pack(pady=10) # Titulo na janela

    vendas_mes_linha = ctk.CTkButton(janela_relatorios, text="Venda do mes", command=janela_vendas_mes_linha, width=270, height=70, font=("Arial Rounded MT Bold", 19))
    vendas_mes_linha.pack(pady=15) # Botao que ao ser clicado abre a janela de vendas por mes

    porcentual_medio_linha_dia = ctk.CTkButton(janela_relatorios, text="Porcentual medio de \ncada dia da semana", command=janela_porcentual_medio_dia, width=270, height=70, font=("Arial Rounded MT Bold", 19))
    porcentual_medio_linha_dia.pack(pady=15) # Botao que ao ser clicado abre a janela do porcentual

    # Cria o campo dos botões abaixo, para não conflitar com o espaço
    janela_botoes = ctk.CTkFrame(janela_relatorios, fg_color="white")
    janela_botoes.pack(pady=15)
 
    btn_voltar = ctk.CTkButton(janela_botoes, text="Voltar", command=janela_relatorios.destroy, fg_color="#4682B4", text_color="white", width=270, height=70, font=("Arial Rounded MT Bold", 19))
    btn_voltar.pack(side="left", padx=15) # Botao que destroi a janela atual

def janela_receber_txt():
    janela_receber_txt = ctk.CTkToplevel(janela) # Janela herda da janela principal
    janela_receber_txt.title("Recebendo via .txt") # Titulo da janela
    janela_receber_txt.geometry("600x450") # Tamanho
    janela_receber_txt.configure(fg_color='white') # Cor de fundo

    texto = ctk.CTkLabel(janela_receber_txt, text="Padrao leitura:", text_color='black', font=('Arial', 22)) # Mostrando as linhas que podem receber onibus
    texto.pack(pady=16) # Texto explicativo

    texto = ctk.CTkLabel(janela_receber_txt, text="Uma linha por reserva", text_color='black', font=('Arial', 19)) # Mostrando as linhas que podem receber onibus
    texto.pack(pady=6) # Texto explicativo

    texto = ctk.CTkLabel(janela_receber_txt, text="(Cidade saida),(Cidade destino),(HR/MM),(DIA/MES/ANO),(Assento)", text_color='black', font=('Arial', 19)) # Mostrando as linhas que podem receber onibus
    texto.pack(pady=16) # Texto explicativo

    texto = ctk.CTkLabel(janela_receber_txt, text="As virgulas são limitantes de Dados, tome cuidado com o que separa!", text_color='black', font=('Arial', 19)) # Mostrando as linhas que podem receber onibus
    texto.pack(pady=6) # Texto explicativo

    arquivo_ler = ctk.CTkEntry(janela_receber_txt, placeholder_text="Digite o nome do arquivo que deseja ler...", width=320, height=50)
    arquivo_ler.pack(pady=16) # Pega o nome do arquivo

    def ler_arquivo(): # Funcao feita por motivo de ser limitado o uso de funcoes com parametros em interfaces
        try:
            arquivo = str(arquivo_ler.get()) # pega o nome do arquivo
            if not arquivo.endswith(".txt"): # caso o arquivo nao terminar .txt ele adiciona o .txt
                arquivo += ".txt"
            Conexao.ler_arquivo(linhas, arquivo) # Chama funcao principal
        except ValueError: # Erro de tipo
            Conexao.janela_aviso("Dados Invalidos!", "red")
        except Exception as e: # Erro inesperado
            Conexao.janela_aviso(f"Error: {e}", "red")


    # Cria o campo dos botões abaixo, para não conflitar com o espaço
    janela_botoes = ctk.CTkFrame(janela_receber_txt, fg_color="white")
    janela_botoes.pack(pady=16)

    btn_gerar = ctk.CTkButton(janela_botoes,text="Ler e reservar", command=ler_arquivo)
    btn_gerar.pack(side="left", padx=3) # Botao que chama a funcao ler arquivo
 
    btn_voltar = ctk.CTkButton(janela_botoes, text="Voltar", command=janela_receber_txt.destroy, fg_color="#4682B4", text_color="white")
    btn_voltar.pack(side="left", padx=3)  # Botao que apaga a janela atual


#------------------------------------------------------------------------------------#

# Menu principal


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

botao4 = ctk.CTkButton(janela, text="Editar linhas", command=janela_editar_linhas, width=270, height=70, font=("Arial Rounded MT Bold", 19))
botao4.pack(pady=15)

botao5 = ctk.CTkButton(janela, text="Relatorios", command=janela_relatorios, width=270, height=70, font=("Arial Rounded MT Bold", 19))
botao5.pack(pady=15)

botao6 = ctk.CTkButton(janela, text="Receber .txt", command=janela_receber_txt, width=270, height=70, font=("Arial Rounded MT Bold", 19))
botao6.pack(pady=15)

janela.mainloop()