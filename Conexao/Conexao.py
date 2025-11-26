import datetime
from Linhas.Linha import Linha
import customtkinter as ctk

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


def mostrar_linhas(dirct_linhas):
    print("Linha disponiveis:")
    for linhas in dirct_linhas.keys():
        print(linhas.nome, end=", ")

def retornar_linhas(dict_linhas):
    linhas_disponiveis = []
    for linha in dict_linhas.keys():
        linhas_disponiveis.append(linha.nome)
    return linhas_disponiveis

def retornar_linhas_onibus(dict_linhas):
    vendas =  []
    for linha, lista_onibus in dict_linhas.items():
        dados = f"Linha {linha.nome}: "
        for onibus in lista_onibus:
            dados += f"{onibus.nome}, "
        vendas.append(dados)

    return vendas



def mostrar_linhas_detalhadas(dirct_linhas):
    print("Linhas e Onibus:")
    for linhas, lista_onibus in dirct_linhas.items():
        print(f"{linhas.nome}: ",end=", ")
        for onibus in lista_onibus:
            print(onibus.data_partida, end=", ")

def adicionar_onibus(dict_linhas, linha_nome, onibus):
    try:
        # Se a linha já existe
        for linha in dict_linhas.keys(): # Percorre as linhas existentes
            if linha_nome == linha.nome: # Quando a linha nome encontrar um linha que existe
                for onibus_existentes in dict_linhas[linha]: # Anda dentro da lista de onibus dessa linha
                    if onibus_existentes.nome == onibus.nome: # Se existir um onibus igual, ele nao cria outro
                        janela_aviso("Onibus ja existe!", "green")
                        return
                dict_linhas[linha].append(onibus) # Se nao existir, cria o onibus
                janela_aviso("Onibus adicionado!", "green")
                return
            
        janela_aviso("Linha inexistente!", "red")

    except Exception as e:
        janela_aviso(e, "red")
    
def remover_linha(dirct_linhas, linha):
    try:
        if linha in dirct_linhas.key():
            del dirct_linhas[linha]
            print("Linha removida!")
        else:
            print("Linha nao consta no sistema!")
        
    except Exception as e:
        print("Ocorreu um erro ao adicionar!")
        print(e)

def adicionar_linha(dirct_linhas, linha):
    try:
        for linha_existente, lista_onibus in dirct_linhas.items():
            if linha.cidade_origem == linha_existente.cidade_origem and linha.cidade_destino == linha_existente.cidade_destino and linha.horario_saida == linha_existente.horario_saida:
                janela_aviso("Linha ja existente!", "green")  # Aqui ele compara item a item da nova linha e das linhas existentes, para nao duplicar. E precisa comparar elemento a elemento, porque os Objs sao diferentes 
                return
    except Exception as e:
        janela_aviso(f"Ocorreu o erro {e}", "red")    
        return
    
    dirct_linhas[linha] = []
    janela_aviso("Linha adicionado!", "green")                                                                                    
    
    
    dirct_linhas[linha] = list() # Criando a chave da linha

def atualizar_onibus(dirct_linhas, dados_user): # Função que paga a data local e verifica os ônibus disponíveis nauquele momento
    lista_aux = list()

    data_user_dia = datetime.datetime.now() # Pega a data do usuário
    data_user_hora = data_user_dia.time()

    try:
        for linha, lista_onibus in dirct_linhas.items():
            for onibus in lista_onibus:
                if onibus.data_partida < data_user_dia: # Verifica se a data do usuario eh maior que a dos onibus das linhas
                    lista_aux = lista_onibus
                    lista_aux.remove(onibus) # Remove os onibus que ja passaram da data

                    dirct_linhas[linha] = lista_aux # Atualiza a lista de onibus

                    

                if onibus.data_partida == dados_user.data: # Verifica os onibus que estao no .nomem já partiu. Hora esmo dia
                    if linha.horario_saida < data_user_hora: # Se o horario de sair ja estiver passado
                        lista_aux = lista_onibus
                        lista_aux.remove(onibus) # Remove os onibus que ja passaram do horario

                        dirct_linhas[linha] = lista_aux # Atualiza a lista de onibus
    except Exception as e:
        print("Ocorreu um erro ao adicionar!")
        print(e)

def verifica_reserva(dirct_linhas, linha, onibus):
    dados_user = datetime.datetime.now()

    # Cria variáveis separadas com padroes certos para fazer comparacoes
    data_user = dados_user.date()
    hora_user = dados_user.time()

    data_onibus = datetime.datetime.strptime(onibus.data_formatada, "%d/%m/%Y").date()
    hora_linha = datetime.datetime.strptime(linha.hora_formatada, "%H:%M").time()

    if data_user > data_onibus:
        janela_aviso("Onibus ja partiu neste dia!", "red")
        return False
    
    if data_user == data_onibus:
        if hora_user > hora_linha:
            janela_aviso("Onibus ja partiu neste horario!", "red")
            return False
        
    return True

def reservar_linha_onibus(dirct_linhas, linha, data, dados_user):
    if not data < dados_user.data_atual: # TODO 
        if dirct_linhas:
            for linha_existentes, lista_onibus in dirct_linhas.items():
                if linha_existentes.nome == linha.nome:
                    for onibus in lista_onibus:
                        if onibus.data_partida == data:
                            if onibus.mostrar_assentos():
                                return
    else:
        print("Onibus ja partiram!")
                        
def editar_linha(dirct_linhas):
    print("Qual acao deseja realizar?")
    print("[1] Editar rota da linha\n[2] Editar horarios\n[3] Remover algum onibus\n")
    resp = input("Digite a opcao desejada")

    match resp:
        case "1":
            editar_rota()
        
        case "2":
            editar_horario()

        case "3":
            remover_onibus()
        
        case _:
            print("Opcao invalida!")


    
def editar_rota(dirct_linhas, linha_original, cidade_origem, cidade_destino):
    try:
        for linha in dirct_linhas.keys():
            if linha.nome == linha_original:
                linha_aux = Linha(cidade_origem, cidade_destino, linha.horario_saida, linha.valor)

                dirct_linhas[linha_aux] = dirct_linhas[linha]

                del dirct_linhas[linha]

                janela_aviso("Linha atualizada!", "green")
                return
            
        janela_aviso("Linha nao encontrada!", "red")
    except ValueError:
        janela_aviso("Tipo de dados invalidos!", "red")
    except Exception as e:
        janela_aviso(f"Error: {e}", "red")

def editar_horario(dirct_linhas, linha_original, novo_horario):
    try:
        
        for linha, lista_onibus in dirct_linhas.items():
            if linha.nome == linha_original:

                for onibus in lista_onibus:
                    if onibus.data_formatada == novo_horario:
                        janela_aviso("Esse onibus ja existe nessa linha, antiga removida!", "orange")
                        return
                    
                linha_atualizada = Linha(linha.cidade_origem, linha.cidade_destino, novo_horario, linha.valor)
                dirct_linhas[linha_atualizada] = lista_onibus
                del dirct_linhas[linha]
                janela_aviso("horario alterado!", "green")
                return
        
        janela_aviso("Linha nao encontrada!", "red")
    except ValueError:
        janela_aviso("Tipo de dados invalidos!", "red")
    except Exception as e:
        janela_aviso(f"Error: {e}")

def remover_onibus(dirct_linhas, linha_desejada, nova_data):
    try:
        for linha, lista_onibus in dirct_linhas.items():
            if linha.nome == linha_desejada:

                for onibus in lista_onibus:
                    if onibus.data_formatada == nova_data:
                        lista_onibus.remove(onibus)
                        janela_aviso("Onibus removido com sucesso", "green")
                        return
                janela_aviso("Onibus nao encontrado!", "red") # Se nao cair no if ele nao encontra onibus
                return
                
            janela_aviso("Linha nao existente!", "red") # Se chegar aqui eh porque nao achou a linha desejada
            return
    except ValueError:
        janela_aviso("Tipo de dados invalidos!", "red")
    except Exception as e:
        janela_aviso(f"Error: {e}")   

def vendas_mes_linha(dirct_linhas, linha_desejada):
    # Pegando os dados do usuario e partindo ele
    dados_user = datetime.datetime.now()
    mes_user = dados_user.month
    ano_user = dados_user.year
    vendas_totais = 0
    try:
        for linha, lista_onibus in dirct_linhas.items(): # Percorre todo o dicionario de linhas
            if linha.nome == linha_desejada: # Se a linha existir ele entra no if
                for onibus in lista_onibus: # Percorre por todos os onibus que existem na linha
                    mes_onibus = mes_onibus = onibus.data_partida.month # Pega o mes do onibus
                    ano_onibus = onibus.data_partida.year # Pega o ano do onibus
                    if mes_user == mes_onibus and ano_user == ano_onibus: # Se o mes e ano for igual ao atual, ele entra no if
                        vendas_totais += linha.valor * len(onibus.assentos_ocupados) # Aqui ele soma o valor arrecadado total e soma com, o produto do valor da passagem pelos assentos ja reservados
                janela_aviso(f"Vendas totais do mes : R$ {vendas_totais}", "black")
                return
        janela_aviso("Linha nao encontrada!", "red")
        return
    except ValueError:
        janela_aviso("Tipo de dados invalidos!", "red")
    except Exception as e:
        janela_aviso(f"Error: {e}", "red")   



def vendas_mes_linha_txt():
    print()
      
def percentual_ocupacao(dirct_linhas, linha):
    data_user = datetime.datetime.today()
    dia_da_semana = data_user.strftime("%A")
    
    #for linha, lista_onibus in dirct_linhas.iten

def reservar_lugar_txt(dirct_linhas, linha_nome, data, assento):
    try:
        for linha_existente, lista_onibus in dirct_linhas.items():
            if linha_existente.nome == linha_nome:
                for onibus in lista_onibus:
                    if onibus.data_formatada == data:

                        if not verifica_reserva(dirct_linhas, linha_existente, onibus):
                            return
                        
                        onibus.reservar_assento(assento)
                        return
                janela_aviso("Onibus nao pertence a essa linha!","red")
                return
        janela_aviso("Linha nao existe!", "red")
    except ValueError:
        janela_aviso("Tipo invalido!","red")

    except Exception as e:
        janela_aviso(f"Error: {e}", "red")



def ler_arquivo(dirct_linhas, arquivo):
    try:
        with open(f"txt/{arquivo}", "r", encoding="utf-8") as arq:
            for linha in arq:
                linha = linha.strip() # Para quando desce a linha
                infos = linha.split() # Separa todas as partes no espaco
                linha = f"{infos[0]} para {infos[1]} as {infos[2]}"
                data = datetime.strptime(infos[3], "%d/%m/%Y")
                data = data.strftime("%d/%m/%Y") # Transfomra no objeto de datas
                assento = int(infos[4])

                reservar_linha_onibus(dirct_linhas, linha, data, assento)
    except FileNotFoundError:
        janela_aviso("Arquivo nao encontrado!", "red")
    except Exception as e:
        janela_aviso(f"Error {e}", "red")
