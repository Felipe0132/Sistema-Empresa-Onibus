import datetime
from Linhas.Linha import Linha
import customtkinter as ctk
from Onibus.Onibus import Onibus
import os

def janela_aviso(mensagem, cor): # Recebe um texto e a cor do texto
    # Criar janela para avisar situação apos uma ação

    janela = ctk.CTkToplevel() # Cria uma de nível alto
    janela.title("AVISO") # Nome da janela
    janela.geometry("500x80") # Tamanho
    janela.configure(fg_color="white") # Cor do fundo

    janela_aviso = ctk.CTkFrame(janela, fg_color="white") # Cor de fundo
    janela_aviso.pack(fill="both", expand=True) # Cria um widget, fill é o preenchimento, expand seria a responsividade do tamanho

    aviso = ctk.CTkLabel(janela_aviso, text=mensagem, text_color=cor, font=('Arial',17))
    aviso.pack(pady=10) # Aqui ele imprime na tela o texto do parâmetro com a cor passada

    botao = ctk.CTkButton(janela_aviso, text="OK", command=janela.destroy) 
    botao.pack(pady=5) # Botão de voltar que apaga a janela de aviso

def mostrar_linhas(dirct_linhas): # Imprime as linhas disponiveis
    for linhas in dirct_linhas.keys(): # Percorre todas as chaves, linhas, do dicionario
        print(linhas.nome, end=", ") # Printa o nome

def retornar_linhas(dict_linhas): # Retorna os nomes das linhas em lista
    linhas_disponiveis = [] # Cria a lista que sera retornada
    for linha in dict_linhas.keys(): # Percorre todas as chaves do dicionario
        linhas_disponiveis.append(linha.nome) # Adiciona na lista o nome, string
    return linhas_disponiveis # Retorna toda lista

def retornar_linhas_onibus(dict_linhas): # Retorna a linha e onibus disponiveis
    vendas =  [] # Cria uma lista que conterá as informações da lista, porém será como string
    for linha, lista_onibus in dict_linhas.items(): # Percorre todo o dicionario
        dados = f"Linha {linha.nome}: " # Aqui guarda o nome da lista
        for onibus in lista_onibus: # Percorre todos os onibus existentes na linha
            dados += f"{onibus.nome}, " 
        vendas.append(dados) # Coloca na lista o nome do onibus

    return vendas # Retorna a lista



def mostrar_linhas_detalhadas(dirct_linhas): # Mesma funcao do retorno mas imprime
    print("Linhas e Onibus:")
    for linhas, lista_onibus in dirct_linhas.items():
        print(f"{linhas.nome}: ",end=", ")
        for onibus in lista_onibus:
            print(onibus.data_partida, end=", ")

def adicionar_onibus(dict_linhas, linha_desejada, onibus): # Funcao que adiciona onibus em uma linha
    try:
        for linha in dict_linhas.keys(): # Percorre as linhas existentes
            if linha_desejada.nome == linha.nome: # Quando a linha nome encontrar um linha que existe
                for onibus_existentes in dict_linhas[linha]: # Anda dentro da lista de onibus dessa linha
                    if onibus_existentes.nome == onibus.nome: # Se existir um onibus igual, ele nao cria outro
                        janela_aviso("Onibus ja existe!", "green")
                        return
                dict_linhas[linha].append(onibus) # Se nao existir, adiciona o onibus na linha
                janela_aviso("Onibus adicionado!", "green")
                return
        janela_aviso("Linha inexistente!", "red") # Quando chega aqui ele não acha uma linha com esse nome
    except Exception as e: # Caso der algum erro
        janela_aviso(e, "red")
    
def remover_linha(dirct_linhas, linha): # Remove uma linha existente
    try:
        for linha_existente in dirct_linhas.keys(): # Percorre todas as linhas do dicionario
            if linha.nome == linha_existente.nome:  # Se encontrar uma linha igual a desejada
                del dirct_linhas[linha_existente] # Remove a linha
                janela_aviso("Linha removida", "red")

        janela_aviso("Linha nao existente!", "red") # Se percorrer e nao achar a linha
        
    except Exception as e: # Se achar erro
        janela_aviso(f"Error: {e}")

def adicionar_linha(dirct_linhas, linha): # Função de adicionar linha
    try:
        for linha_existente in dirct_linhas.keys(): # Percorre todas as linhas existentes
            if linha.cidade_origem == linha_existente.cidade_origem and linha.cidade_destino == linha_existente.cidade_destino and linha.horario_saida == linha_existente.horario_saida:
                # Se achar uma linha identida a adicionada, ele entra no if
                janela_aviso("Linha já existente!", "red")
                return
    except Exception as e:
        janela_aviso(f"Ocorreu o erro {e}", "red")    
        return
    
    dirct_linhas[linha] = list() # Se nao existir linha igual, ele cria a linha e define que valor receberá uma lista
    
    data_usuario = datetime.datetime.now().date() # Pega a data do usuario
    
    # Assim que a linha é criada, ela terá que inicializar com onibus de 30 datas apartir dela, dela mais 30

    for dia in range(30): # Faz um for de 0 a 30
        dia_onibus = data_usuario + datetime.timedelta(days=dia) #Soma a data pela vez que o for esta
        
        onibus = Onibus(dia_onibus) # Cria um onibus com a data da variavel

        dirct_linhas[linha].append(onibus) # Adiciona o onibus na lista de onibus da linha

    janela_aviso("Linha adicionado!", "green")                                                                                    
    
"""
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
"""

def verifica_reserva(dirct_linhas, linha, onibus): # Função que verifica se é possivel reserva
    dados_user = datetime.datetime.now() # Pega datra do usuario

    # Cria variaveis para verificar requisitos da reserva
    data_user = dados_user.date() # Data
    hora_user = dados_user.time() # Horario

    data_onibus = datetime.datetime.strptime(onibus.data_formatada, "%d/%m/%Y").date() # Data
    hora_linha = datetime.datetime.strptime(linha.hora_formatada, "%H:%M").time() # Horario

    if data_user > data_onibus: # Se a data do usuario é maior que a do onibus, já passou
        janela_aviso("Onibus ja partiu neste dia!", "red")
        return False
    
    if data_user == data_onibus: # Se o onibus for no mesmo dia que deseja fazer a reserva
        if hora_user > hora_linha: # Se o horario ja tiver passado, não é possivel
            janela_aviso("Onibus ja partiu neste horario!", "red")
            return False
        
    return True # Se não parar em nenhuma restição, OK para horario e data

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


    
def editar_rota(dirct_linhas, linha_original, cidade_origem, cidade_destino): # Alterar uma rota
    try:
        for linha in dirct_linhas.keys(): # Percorre todas as linhas
            if linha.nome == linha_original: # Se encontrar a linha desejada
                linha_aux = Linha(cidade_origem, cidade_destino, linha.horario_saida, linha.valor)
                # Cria uma nova linha com a cidade destino e origem novas, porem conserva o valor e horario

                dirct_linhas[linha_aux] = dirct_linhas[linha]
                # Aqui ele conserva todos os onibus que haviam na original

                del dirct_linhas[linha] # Assim que tudo for alterado, ele remove a linha antiga

                janela_aviso("Linha atualizada!", "green")
                return
            
        janela_aviso("Linha nao encontrada!", "red") # Se nao achar uma linha igual, ela não existe
    except ValueError: # Erro de tipo de dados
        janela_aviso("Tipo de dados invalidos!", "red")
    except Exception as e: # Erro inesperado
        janela_aviso(f"Error: {e}", "red")

def editar_horario(dirct_linhas, linha, novo_horario): # Função de editar horario de uma linha
    try:
        for linha_existente in dirct_linhas.keys(): # Percorre todo o dicionario
            if linha.nome == linha_existente: # Procura a linha desejada
                linha_existente.horario_saida = novo_horario # Muda o horario do objeto
                janela_aviso("horario alterado!", "green")
                return
        
        janela_aviso("Linha nao encontrada!", "red") # Caso nao entre nos IFs, a linha não existe
    except ValueError: # Erro de tipo de dado
        janela_aviso("Tipo de dados invalidos!", "red")
    except Exception as e: # Erro inesperado
        janela_aviso(f"Error: {e}")

def remover_onibus(dirct_linhas, linha_desejada, nova_data): # Função que remove um onibus da linha
    try:
        for linha, lista_onibus in dirct_linhas.items(): # Percorre todo o dicionario
            if linha.nome == linha_desejada: # Se achar a linha
                for onibus in lista_onibus: # Percorre todo os onibus
                    if onibus.data_formatada == nova_data: # Se chegar no onibus desejado
                        lista_onibus.remove(onibus) # Remove o onibus
                        janela_aviso("Onibus removido com sucesso", "green")
                        return
                janela_aviso("Onibus nao encontrado!", "red") # Se nao cair no if ele nao encontra onibus
                return
                
            janela_aviso("Linha nao existente!", "red") # Se chegar aqui eh porque nao achou a linha desejada
            return
    except ValueError: # Erro de dado
        janela_aviso("Tipo de dados invalidos!", "red")
    except Exception as e: # Erro inesperado
        janela_aviso(f"Error: {e}")   

def vendas_mes_linha(dirct_linhas, linha_desejada): # Funcao que retorna ganha do mes atual
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
        janela_aviso("Linha nao encontrada!", "red") # Se ele nao achar a linha no Loop
        return
    except ValueError: # Erro de dado
        janela_aviso("Tipo de dados invalidos!", "red")
    except Exception as e: # Erro inesperado
        janela_aviso(f"Error: {e}", "red")   



def vendas_mes_linha_txt(dirct_linhas, linha_desejada): # Funcao que retorna ganha do mes atual
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
                # TODO Adicionar no relatorio mensal.txt
                return
        janela_aviso("Linha nao encontrada!", "red") # Se ele nao achar a linha no Loop
        return
    except ValueError: # Erro de dado
        janela_aviso("Tipo de dados invalidos!", "red")
    except Exception as e: # Erro inesperado
        janela_aviso(f"Error: {e}", "red")   


def registrar_erro(mensagem):
    try:
        # Cria a pasta logs se não existir
        if not os.path.exists("logs"):
            os.makedirs("logs")

        # Pega data e hora atual
        data_hora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        # Monta a linha que será escrita no txt
        linha = f"[{data_hora}] - {mensagem}\n"

        # Abre (ou cria) o arquivo e adiciona a nova linha
        with open("logs/logs_erros.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(linha)

    except Exception as e:
        # FAILSAFE: evita que erro dentro da função quebre o sistema
        print("Falha ao registrar erro:", e)


def matriz_percentual_ocupacao(dirct_linhas):
    """
    Gera uma matriz onde:
    - cada linha da matriz representa uma linha de ônibus
    - cada coluna representa um dia da semana
    - cada célula contém a ocupação média (%)
    """
    
    # Dias da semana na ordem certa da matriz
    dias_semana = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    matriz_resultado = []     # Aqui ficará a matriz final
    nomes_linhas = []         # Guarda os nomes das linhas (para o usuário exibir depois)

    # Percorre todas as entradas do dicionário: linha -> lista de ônibus
    for chave_linha, lista_onibus in dirct_linhas.items():
        
        # Guarda nome da linha
        nomes_linhas.append(chave_linha)

        # Aqui guardaremos ocupação média de cada dia dessa linha
        ocupacoes_semanais = []  
        
        # Para cada dia da semana, vamos calcular a média
        for dia in dias_semana:

            porcentagens = []  # guarda % de ocupação de cada ônibus que roda nesse dia

            # Agora percorremos todos os ônibus da linha
            for onibus in lista_onibus:

                # Descobrir o dia da semana desse ônibus
                dia_onibus = onibus.data_partida.strftime("%A")

                # Se esse ônibus roda no dia que estamos calculando
                if dia_onibus == dia:
                    ocupados = len(onibus.assentos_ocupados)
                    porcentagem = (ocupados / 20) * 100
                    porcentagens.append(porcentagem)

            # Terminamos de verificar os ônibus desse dia
            # Agora calculamos a média
            if len(porcentagens) > 0:
                media = sum(porcentagens) / len(porcentagens)
            else:
                media = 0  # Se nenhum ônibus rodou nesse dia

            # Adiciona a média desse dia
            ocupacoes_semanais.append(media)

        # Terminou os 7 dias → adiciona linha completa na matriz
        matriz_resultado.append(ocupacoes_semanais)

    return matriz_resultado, nomes_linhas


    
def reservar_lugar_txt(dirct_linhas, linha_nome, data, assento): # Funcao que recebe uma reserva no .txt
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



def ler_arquivo(dirct_linhas, arquivo): # Função que le um arquivo e faz reserva por ele
    try:
        with open(f"txt/{arquivo}", "r", encoding="utf-8") as arq: # Abre o arquivo .txt
            for linha in arq: # percorre as linhas do arquivo
                linha = linha.strip() # Para quando desce a linha
                infos = linha.split(",") # Separa todas as partes no espaco
                linha = f"{infos[0]} para {infos[1]} as {infos[2]}" # Cria o nome da linha desejada
                data = datetime.strptime(infos[3], "%d/%m/%Y") # Define a data da reserva
                data = data.strftime("%d/%m/%Y") # Transfomra no objeto de datas
                assento = int(infos[4]) # Define o assento da reserva

                for linha_existente, lista_onibus in dirct_linhas.item(): # percorre dicionario
                    if linha_existente.nome == linha: # Encontra a linha que deseja
                        for onibus in lista_onibus: # Percorre a lista de onibus da linha
                            if data == onibus.data_formatada: # Acha o onibus com a data desejada
                                if verifica_reserva(dirct_linhas, linha_existente, onibus): # Verifica se pode reservar
                                    onibus.reservar_assento(assento) # Reservar o assento se possivel
                                    return
                        janela_aviso("Onibus nao encontrado!", "red") # Se nao achar o onibus
                        return
                janela_aviso("Linha nao encontrada!", "red") # Se a linha nao for
                return
    except FileNotFoundError: # Se não achar o arquivo
        janela_aviso("Arquivo nao encontrado!", "red")
    except Exception as e: # Erro inesperado
        janela_aviso(f"Error {e}", "red")
