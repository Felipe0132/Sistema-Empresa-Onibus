# Codigo para rodar  python3 -m Main.main001

from Linhas.Linha import Linha
from Onibus.Onibus import Onibus
import Conexao.Conexao as Conexao
import datetime
import customtkinter as ctk # Interface grafica
import tkinter as tk

linhas = dict()

datetime_user = datetime.datetime.now()

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
            hora = datetime.datetime.strptime(horario_saida.get(), "%H:%M")
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
            data = datetime.datetime.strptime(data_saida.get(), "%d/%m/%Y") # Transforma ela em String
            
            novo_onibus = Onibus(data) # Pegando os dados da interface e transformando na linha

            for linha_existente in linhas:
                if linha_existente.nome == linha_nome.get():
                    Conexao.adicionar_onibus(linhas, linha_existente, novo_onibus) # Funcao de adicionar linha

            

        except ValueError:
            Conexao.janela_aviso("Dados inválidos. Verifique Informacoes passadas.", "red")

        except Exception as e:
            Conexao.janela_aviso(f"Erro: {e}", "red")

    btn_inserir = ctk.CTkButton(janela_botoes,text="Inserir", command= inserir)
    btn_inserir.pack(side="left", padx=5)   
    # A funcao datetime.strptime converte o que foi recebido na caixa para valores de data       

    btn_voltar = ctk.CTkButton(janela_botoes, text="Voltar", command=jan_adicionar_onibus.destroy, fg_color="#4682B4", text_color="white")
    btn_voltar.pack(side="left", padx=5) 

def janela_reservar_lugar(linhas, linha_existente, onibus):

    if not Conexao.verifica_reserva(linhas, linha_existente, onibus):
        return


    janela_reservar_lugar = ctk.CTkToplevel(janela)
    janela_reservar_lugar.title("Lugares disponiveis")
    janela_reservar_lugar.geometry("500x450")
    janela_reservar_lugar.configure(fg_color='white')

    titulo = ctk.CTkLabel(janela_reservar_lugar, text="Escolha um lugar", text_color='black', font=('Arial', 25))
    titulo.pack(pady=10)    

    lugar_escolhido = ctk.CTkEntry(janela_reservar_lugar, placeholder_text="Digite um lugar disponivel (1 a 20)...", width=320, height=50)
    lugar_escolhido.pack(pady=10)

    texto = ctk.CTkLabel(janela_reservar_lugar, text="Lugares", text_color='black', font=('Arial', 25))
    texto.pack(pady=10)

    lugares_onibus = ctk.CTkFrame(janela_reservar_lugar, fg_color='white')
    lugares_onibus.pack(pady=5) # Aqui vai criar a sessao para imprirmir os lugares do onibus

    # Frame onde os lugares serão exibidos
    frame_lugares = ctk.CTkFrame(janela_reservar_lugar, fg_color="white")
    frame_lugares.pack(pady=2)  

    for coluna, numero in enumerate(range(1, 20 + 1)):
        if numero in onibus.assentos_disponiveis:
            cor = 'green'
        else:
            cor = 'red'

        lugares = ctk.CTkLabel(frame_lugares, text=str(numero), text_color=cor)
        lugares.pack(side="left", padx=3)


    def reservar_lugar():
        try:
            lugar = int(lugar_escolhido.get())

            if len(onibus.assentos_disponiveis) == 0:
                Conexao.janela_aviso("Nenhum assento disponivel!", "red")

            onibus.reservar_assento(lugar)

        except ValueError:
            Conexao.janela_aviso("Tipo invalido!","red")

        except Exception as e:
            Conexao.janela_aviso(f"Error: {e}", "red")

    # Cria o campo dos botões abaixo, para não conflitar com o espaço
    janela_botoes = ctk.CTkFrame(janela_reservar_lugar, fg_color="white")
    janela_botoes.pack(pady=4)

    btn_marcar_lugar = ctk.CTkButton(janela_botoes,text="Marcar Lugar", command= reservar_lugar, height=40, width=150, font=("Arial", 16))
    btn_marcar_lugar.pack(side="left", padx=20, pady=4)   
    # A funcao datetime.strptime converte o que foi recebido na caixa para valores de data       

    btn_voltar = ctk.CTkButton(janela_botoes, text="Voltar", command=janela_reservar_lugar.destroy, fg_color="#4682B4", text_color="white", height=40, width=150, font=("Arial", 16))
    btn_voltar.pack(side="left", padx=20, pady=4) 


def janela_comprar_passagem():
    janela_comprar_passagem = ctk.CTkToplevel(janela)
    janela_comprar_passagem.title("Comprando passagem")
    janela_comprar_passagem.geometry("800x500")
    janela_comprar_passagem.configure(fg_color='white')

    titulo = ctk.CTkLabel(janela_comprar_passagem, text="Escolha os dados", text_color='black', font=('Arial', 25))
    titulo.pack(pady=7)

    data_saida = ctk.CTkEntry(janela_comprar_passagem, placeholder_text="Digite a data de saida (DD/MM/AAAA)...", width=320, height=50)
    data_saida.pack(pady=7)

    linha = ctk.CTkEntry(janela_comprar_passagem, placeholder_text="Digite a linha que deseja adicionar...", width=320, height=50)
    linha.pack(pady=7)

    texto = ctk.CTkLabel(janela_comprar_passagem, text="Lista de Linhas Disponiveis", text_color='black', font=('Arial', 22)) # Mostrando as linhas que podem receber onibus
    texto.pack(pady=7)

    linhas_disponiveis = Conexao.retornar_linhas_onibus(linhas) # Aqui cria uma lista de linhas para puder imprimir os dados melhor

        # --- FRAME CONTÊINER (CustomTkinter) ---
    ctk_frame_scroll = ctk.CTkFrame(janela_comprar_passagem, fg_color="white")
    ctk_frame_scroll.pack(pady=5)

    # --- CANVAS (Tkinter) ---
    canvas = tk.Canvas(ctk_frame_scroll, width=500, height=200)
    canvas.pack(side="left", fill="both", expand=True)

    # --- SCROLLBARS ---
    scroll_y = tk.Scrollbar(ctk_frame_scroll, orient="vertical", command=canvas.yview)
    scroll_y.pack(side="right", fill="y")

    scroll_x = tk.Scrollbar(janela_comprar_passagem, orient="horizontal", command=canvas.xview)
    scroll_x.pack(fill="x")

    canvas.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

    # --- INTERIOR DO CANVAS ---
    frame_interno = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame_interno, anchor="nw")

    # --- Preencher com os textos das linhas ---
    for linha_disp in linhas_disponiveis:
        tk.Label(frame_interno, text=linha_disp, anchor="w").pack(pady=2)

    # --- Atualizar área scrollável ---
    def ajustar_scroll(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    frame_interno.bind("<Configure>", ajustar_scroll)

    # Cria o campo dos botões abaixo, para não conflitar com o espaço
    janela_botoes = ctk.CTkFrame(janela_comprar_passagem, fg_color="white")
    janela_botoes.pack(pady=3)

    def buscar_lugares():
        try:
            data = datetime.datetime.strptime(data_saida.get(), "%d/%m/%Y")
            data = data.strftime("%d/%m/%Y")
            linha_nome = linha.get()

            for linha_existente, lista_onibus in linhas.items():
                if linha_existente.nome == linha_nome:
                    for onibus in lista_onibus:
                        if onibus.data_formatada == data:
                            janela_reservar_lugar(linhas, linha_existente, onibus)
                            return
        
                    # Só cai aqui se não achou nenhum onibus igual
                    Conexao.janela_aviso("Ônibus não pertencem a essa linha!", "red")
                    return

            # Só chega aqui se nao ahcar a linha
            Conexao.janela_aviso("Linha não existe!", "red")

        except ValueError:
            Conexao.janela_aviso("Dados inválidos. Verifique Informacoes passadas.", "red")

        except Exception as e:
            Conexao.janela_aviso(f"Erro: {e}", "red")

    btn_inserir = ctk.CTkButton(janela_botoes,text="Olhar lugares", command= buscar_lugares)
    btn_inserir.pack(side="left", padx=3)   
    # A funcao datetime.strptime converte o que foi recebido na caixa para valores de data       

    btn_voltar = ctk.CTkButton(janela_botoes, text="Voltar", command=janela_comprar_passagem.destroy, fg_color="#4682B4", text_color="white")
    btn_voltar.pack(side="left", padx=3) 
            

def janela_editar_rota():
    janela_editar_rota = ctk.CTkToplevel(janela)
    janela_editar_rota.title("Editando Rota")
    janela_editar_rota.geometry("500x550")
    janela_editar_rota.configure(fg_color='white')

    titulo = ctk.CTkLabel(janela_editar_rota, text="Novos Dados", text_color='black', font=('Arial', 25))
    titulo.pack(pady=7)

    linha_original = ctk.CTkEntry(janela_editar_rota, placeholder_text="Digite a linha que deseja editar...", width=320, height=50)
    linha_original.pack(pady=5)

    cidade_origem = ctk.CTkEntry(janela_editar_rota, placeholder_text="Digite a cidade origem...", width=320, height=50)
    cidade_origem.pack(pady=5)

    cidade_destino = ctk.CTkEntry(janela_editar_rota, placeholder_text="Digite a cidade destino...", width=320, height=50)
    cidade_destino.pack(pady=5)

    texto = ctk.CTkLabel(janela_editar_rota, text="Lista de Linhas Disponiveis", text_color='black', font=('Arial', 22)) # Mostrando as linhas que podem receber onibus
    texto.pack(pady=5)

    linhas_onibus_disponiveis = Conexao.retornar_linhas_onibus(linhas)

    scrolllist = ctk.CTkScrollableFrame(janela_editar_rota, orientation="vertical", width=320, height=200) # Cria uma parte de scroll na janela
    scrolllist.pack(pady=5)

    for lin_dados in linhas_onibus_disponiveis:
        ctk.CTkLabel(scrolllist, text=lin_dados).pack(pady=2)

    def editar():
        try:
            Conexao.editar_rota(linhas, linha_original.get(), cidade_origem.get(), cidade_destino.get())
        except ValueError:
            Conexao.janela_aviso("Dados Invalidos!", "red")
        except Exception as e:
            Conexao.janela_aviso(f"Error: {e}","red")

    janela_botoes = ctk.CTkFrame(janela_editar_rota, fg_color="white")
    janela_botoes.pack(pady=3)
    
    btn_editar = ctk.CTkButton(janela_botoes,text="Editar", command=editar)
    btn_editar.pack(side="left", padx=3)
 
    btn_voltar = ctk.CTkButton(janela_botoes, text="Voltar", command=janela_editar_rota.destroy, fg_color="#4682B4", text_color="white")
    btn_voltar.pack(side="left", padx=3) 

def janela_editar_horario():
    janela_editar_horario = ctk.CTkToplevel(janela)
    janela_editar_horario.title("Editar Horario")
    janela_editar_horario.geometry("500x600")
    janela_editar_horario.configure(fg_color='white')

    titulo = ctk.CTkLabel(janela_editar_horario, text="Novos Dados", text_color='black', font=('Arial', 25))
    titulo.pack(pady=5)

    linha_original = ctk.CTkEntry(janela_editar_horario, placeholder_text="Digite a linha que deseja editar...", width=320, height=50)
    linha_original.pack(pady=2)

    novo_horario = ctk.CTkEntry(janela_editar_horario, placeholder_text="Digite o novo horario...", width=320, height=50)
    novo_horario.pack(pady=2)

    linhas_disponiveis = Conexao.retornar_linhas_onibus(linhas)

        # --- FRAME CONTÊINER (CustomTkinter) ---
    ctk_frame_scroll = ctk.CTkFrame(janela_comprar_passagem, fg_color="white")
    ctk_frame_scroll.pack(pady=5)

    # --- CANVAS (Tkinter) ---
    canvas = tk.Canvas(ctk_frame_scroll, width=500, height=200)
    canvas.pack(side="left", fill="both", expand=True)

    # --- SCROLLBARS ---
    scroll_y = tk.Scrollbar(ctk_frame_scroll, orient="vertical", command=canvas.yview)
    scroll_y.pack(side="right", fill="y")

    scroll_x = tk.Scrollbar(janela_comprar_passagem, orient="horizontal", command=canvas.xview)
    scroll_x.pack(fill="x")

    canvas.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

    # --- INTERIOR DO CANVAS ---
    frame_interno = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame_interno, anchor="nw")

    # --- Preencher com os textos das linhas ---
    for linha_disp in linhas_disponiveis:
        tk.Label(frame_interno, text=linha_disp, anchor="w").pack(pady=2)

    # --- Atualizar área scrollável ---
    def ajustar_scroll(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    frame_interno.bind("<Configure>", ajustar_scroll)


    def editar():
        try:
            horario_saida = datetime.datetime.strptime(novo_horario.get(), "%H:%M")

            Conexao.editar_horario(linhas, str(linha_original.get()), horario_saida)
        except ValueError:
            Conexao.janela_aviso("Dados Invalidos!", "red")
        except Exception as e:
            Conexao.janela_aviso(f"Error: {e}", "red")

    # Cria o campo dos botões abaixo, para não conflitar com o espaço
    janela_botoes = ctk.CTkFrame(janela_editar_horario, fg_color="white")
    janela_botoes.pack(pady=3)

    btn_editar = ctk.CTkButton(janela_botoes,text="Editar", command= editar)
    btn_editar.pack(side="left", padx=3)   
    # A funcao datetime.strptime converte o que foi recebido na caixa para valores de data       

    btn_voltar = ctk.CTkButton(janela_botoes, text="Voltar", command=janela_editar_horario.destroy, fg_color="#4682B4", text_color="white")
    btn_voltar.pack(side="left", padx=3) 

def janela_remover_onibus():
    janela_remover_onibus = ctk.CTkToplevel(janela)
    janela_remover_onibus.title("Removendo Onibus")
    janela_remover_onibus.geometry("500x450")
    janela_remover_onibus.configure(fg_color='white')

    titulo = ctk.CTkLabel(janela_remover_onibus, text="Removendo Dados", text_color='black', font=('Arial', 25))
    titulo.pack(pady=5)

    linha_original = ctk.CTkEntry(janela_remover_onibus, placeholder_text="Digite a linha que deseja editar...", width=320, height=50)
    linha_original.pack(pady=2)

    data_onibus = ctk.CTkEntry(janela_remover_onibus, placeholder_text="Digite a data do onibus...", width=320, height=50)
    data_onibus.pack(pady=2)

    texto = ctk.CTkLabel(janela_remover_onibus, text="Lista de Linhas Disponiveis", text_color='black', font=('Arial', 22)) # Mostrando as linhas que podem receber onibus
    texto.pack(pady=2)

    linhas_disponiveis = Conexao.retornar_linhas_onibus(linhas)


        # --- FRAME CONTÊINER (CustomTkinter) ---
    ctk_frame_scroll = ctk.CTkFrame(janela_comprar_passagem, fg_color="white")
    ctk_frame_scroll.pack(pady=5)

    # --- CANVAS (Tkinter) ---
    canvas = tk.Canvas(ctk_frame_scroll, width=500, height=200)
    canvas.pack(side="left", fill="both", expand=True)

    # --- SCROLLBARS ---
    scroll_y = tk.Scrollbar(ctk_frame_scroll, orient="vertical", command=canvas.yview)
    scroll_y.pack(side="right", fill="y")

    scroll_x = tk.Scrollbar(janela_comprar_passagem, orient="horizontal", command=canvas.xview)
    scroll_x.pack(fill="x")

    canvas.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

    # --- INTERIOR DO CANVAS ---
    frame_interno = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame_interno, anchor="nw")

    # --- Preencher com os textos das linhas ---
    for linha_disp in linhas_disponiveis:
        tk.Label(frame_interno, text=linha_disp, anchor="w").pack(pady=2)

    # --- Atualizar área scrollável ---
    def ajustar_scroll(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    frame_interno.bind("<Configure>", ajustar_scroll)


    def editar():
        try:
            data = datetime.datetime.strptime(data_onibus.get(), "%d/%m/%Y")
            data = data.strftime("%d/%m/%Y") # Transfomra no objeto de datas

            Conexao.remover_onibus(linhas, str(linha_original.get()), data)
        except ValueError:
            Conexao.janela_aviso("Dados Invalidos!", "red")
        except Exception as e:
            Conexao.janela_aviso(f"Error: {e}","red")

    # Cria o campo dos botões abaixo, para não conflitar com o espaço
    janela_botoes = ctk.CTkFrame(janela_remover_onibus, fg_color="white")
    janela_botoes.pack(pady=2)

    btn_editar = ctk.CTkButton(janela_botoes,text="Editar", command=editar)
    btn_editar.pack(side="left", padx=3)
 
    btn_voltar = ctk.CTkButton(janela_botoes, text="Voltar", command=janela_remover_onibus.destroy, fg_color="#4682B4", text_color="white")
    btn_voltar.pack(side="left", padx=3)

def janela_editar_linhas():
    janela_editar_linhas = ctk.CTkToplevel(janela)
    janela_editar_linhas.title("Opcoes de Edicao")
    janela_editar_linhas.geometry("500x450")
    janela_editar_linhas.configure(fg_color='white')

    titulo = ctk.CTkLabel(janela_editar_linhas, text="Opcoes", text_color='black', font=('Arial', 25))
    titulo.pack(pady=10)

    editar_rotas = ctk.CTkButton(janela_editar_linhas, text="Editar Rota", command=janela_editar_rota, width=270, height=70, font=("Arial Rounded MT Bold", 19))
    editar_rotas.pack(pady=15)

    editar_horario = ctk.CTkButton(janela_editar_linhas, text="Editar Horario", command=janela_editar_horario, width=270, height=70, font=("Arial Rounded MT Bold", 19))
    editar_horario.pack(pady=15)

    remover_onibus = ctk.CTkButton(janela_editar_linhas, text="Remover Onibus", command=janela_remover_onibus, width=270, height=70, font=("Arial Rounded MT Bold", 19))
    remover_onibus.pack(pady=15)

    # Cria o campo dos botões abaixo, para não conflitar com o espaço
    janela_botoes = ctk.CTkFrame(janela_editar_linhas, fg_color="white")
    janela_botoes.pack(pady=2)

    btn_editar = ctk.CTkButton(janela_botoes,text="Editar", command=" ")
    btn_editar.pack(side="left", padx=3)
 
    btn_voltar = ctk.CTkButton(janela_botoes, text="Voltar", command=janela_editar_linhas.destroy, fg_color="#4682B4", text_color="white")
    btn_voltar.pack(side="left", padx=3)

def janela_vendas_mes_linha():
    janela_vendas_mes_linha = ctk.CTkToplevel(janela)
    janela_vendas_mes_linha.title("Vendas do mes de uma linha")
    janela_vendas_mes_linha.geometry("500x450")
    janela_vendas_mes_linha.configure(fg_color='white')

    linha_desejavel = ctk.CTkEntry(janela_vendas_mes_linha, placeholder_text="Digite a linha que deseja editar...", width=320, height=50)
    linha_desejavel.pack(pady=2)

    texto = ctk.CTkLabel(janela_vendas_mes_linha, text="Lista de Linhas Disponiveis", text_color='black', font=('Arial', 22)) # Mostrando as linhas que podem receber onibus
    texto.pack(pady=2)

    linhas_disponiveis = Conexao.retornar_linhas(linhas) # Aqui cria uma lista de linhas para puder imprimir os dados melhor

    scrolllist = ctk.CTkScrollableFrame(janela_vendas_mes_linha, orientation=ctk.VERTICAL, width=320) # Cria uma parte de scroll na janela
    scrolllist.pack(pady=5)

    for linha_disp in linhas_disponiveis:
        ctk.CTkLabel(scrolllist, text=linha_disp).pack(pady=2) # Aqui ele coloca na caixa de scroll os itens da lista
    
    def gerar_relatorio():
        try:
            Conexao.vendas_mes_linha(linhas, str(linha_desejavel.get()))
        except ValueError:
            Conexao.janela_aviso("Dados Invalidos!", "red")
        except Exception as e:
            Conexao.janela_aviso(f"Error: {e}","red")

    def gerar_relatorio_txt():
        try:
            Conexao.vendas_mes_linha_txt(linhas, str(linha_desejavel.get()))
        except ValueError:
            Conexao.janela_aviso("Dados Invalidos!", "red")
        except Exception as e:
            Conexao.janela_aviso(f"Error: {e}", "red")
        
    # Cria o campo dos botões abaixo, para não conflitar com o espaço
    janela_botoes = ctk.CTkFrame(janela_vendas_mes_linha, fg_color="white")
    janela_botoes.pack(pady=2)

    btn_gerar = ctk.CTkButton(janela_botoes,text="Gerar", command=gerar_relatorio)
    btn_gerar.pack(side="left", padx=3)

    btn_gerar_txt = ctk.CTkButton(janela_botoes,text="Gerar em .txt", command=gerar_relatorio_txt)
    btn_gerar_txt.pack(side="left", padx=3)  
 
    btn_voltar = ctk.CTkButton(janela_botoes, text="Voltar", command=janela_vendas_mes_linha.destroy, fg_color="#4682B4", text_color="white")
    btn_voltar.pack(side="left", padx=3)    

def janela_relatorios():
    janela_relatorios = ctk.CTkToplevel(janela)
    janela_relatorios.title("Opcoes de Relatorio")
    janela_relatorios.geometry("500x450")
    janela_relatorios.configure(fg_color='white')

    titulo = ctk.CTkLabel(janela_relatorios, text="Opcoes", text_color='black', font=('Arial', 25))
    titulo.pack(pady=10)    

    vendas_mes_linha = ctk.CTkButton(janela_relatorios, text="Venda do mes", command=janela_vendas_mes_linha, width=270, height=70, font=("Arial Rounded MT Bold", 19))
    vendas_mes_linha.pack(pady=15)

    porcentual_medio_linha_dia = ctk.CTkButton(janela_relatorios, text="Porcentual medio de \ncada dia da semana", command="", width=270, height=70, font=("Arial Rounded MT Bold", 19))
    porcentual_medio_linha_dia.pack(pady=15)

    # Cria o campo dos botões abaixo, para não conflitar com o espaço
    janela_botoes = ctk.CTkFrame(janela_relatorios, fg_color="white")
    janela_botoes.pack(pady=15)
 
    btn_voltar = ctk.CTkButton(janela_botoes, text="Voltar", command=janela_relatorios.destroy, fg_color="#4682B4", text_color="white", width=270, height=70, font=("Arial Rounded MT Bold", 19))
    btn_voltar.pack(side="left", padx=15)


def janela_receber_txt():
    janela_receber_txt = ctk.CTkToplevel(janela)
    janela_receber_txt.title("Recebendo via .txt")
    janela_receber_txt.geometry("600x450")
    janela_receber_txt.configure(fg_color='white')

    texto = ctk.CTkLabel(janela_receber_txt, text="Padrao leitura:", text_color='black', font=('Arial', 22)) # Mostrando as linhas que podem receber onibus
    texto.pack(pady=16)

    texto = ctk.CTkLabel(janela_receber_txt, text="Uma linha por reserva", text_color='black', font=('Arial', 19)) # Mostrando as linhas que podem receber onibus
    texto.pack(pady=6)

    texto = ctk.CTkLabel(janela_receber_txt, text="(Cidade saida) (Cidade destino) (HR/MM) (DIA/MES/ANO) (Lugar)", text_color='black', font=('Arial', 19)) # Mostrando as linhas que podem receber onibus
    texto.pack(pady=16)

    texto = ctk.CTkLabel(janela_receber_txt, text="Os espaço são limitantes de Dados,não escreva cidades compostas!", text_color='black', font=('Arial', 19)) # Mostrando as linhas que podem receber onibus
    texto.pack(pady=6)

    arquivo_ler = ctk.CTkEntry(janela_receber_txt, placeholder_text="Digite o nome do arquivo que deseja ler...", width=320, height=50)
    arquivo_ler.pack(pady=16)   

    def ler_arquivo():
        try:
            arquivo = str(arquivo_ler.get())
            if not arquivo.endswith(".txt"):
                arquivo += ".txt"
            Conexao.ler_arquivo(linhas, arquivo)
        except ValueError:
            Conexao.janela_aviso("Dados Invalidos!", "red")
        except Exception as e:
            Conexao.janela_aviso(f"Error: {e}", "red")


    # Cria o campo dos botões abaixo, para não conflitar com o espaço
    janela_botoes = ctk.CTkFrame(janela_receber_txt, fg_color="white")
    janela_botoes.pack(pady=16)

    btn_gerar = ctk.CTkButton(janela_botoes,text="Ler e reservar", command=ler_arquivo)
    btn_gerar.pack(side="left", padx=3)
 
    btn_voltar = ctk.CTkButton(janela_botoes, text="Voltar", command=janela_receber_txt.destroy, fg_color="#4682B4", text_color="white")
    btn_voltar.pack(side="left", padx=3)  

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

botao4 = ctk.CTkButton(janela, text="Editar linhas", command=janela_editar_linhas, width=270, height=70, font=("Arial Rounded MT Bold", 19))
botao4.pack(pady=15)

botao5 = ctk.CTkButton(janela, text="Relatorios", command=janela_relatorios, width=270, height=70, font=("Arial Rounded MT Bold", 19))
botao5.pack(pady=15)

botao6 = ctk.CTkButton(janela, text="Receber .txt", command=janela_receber_txt, width=270, height=70, font=("Arial Rounded MT Bold", 19))
botao6.pack(pady=15)



janela.mainloop()


