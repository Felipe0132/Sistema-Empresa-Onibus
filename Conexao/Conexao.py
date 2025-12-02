import datetime
from Linhas.Linha import Linha
import customtkinter as ctk
from Onibus.Onibus import Onibus

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

def mostrar_linhas(dict_linhas): # Imprime as linhas disponiveis
    for linhas in dict_linhas.keys(): # Percorre todas as chaves, linhas, do dicionario
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

def mostrar_linhas_detalhadas(dict_linhas): # Mesma funcao do retorno mas imprime
    print("Linhas e Onibus:")
    for linhas, lista_onibus in dict_linhas.items():
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
    
def remover_linha(dict_linhas, linha): # Remove uma linha existente
    try:
        for linha_existente in dict_linhas.keys(): # Percorre todas as linhas do dicionario
            if linha.nome == linha_existente.nome:  # Se encontrar uma linha igual a desejada
                del dict_linhas[linha_existente] # Remove a linha
                janela_aviso("Linha removida", "red")

        janela_aviso("Linha nao existente!", "red") # Se percorrer e nao achar a linha
        
    except Exception as e: # Se achar erro
        janela_aviso(f"Error: {e}")

def adicionar_linha(dict_linhas, linha): # Função de adicionar linha
    try:

        if linha.valor <= 0:
            janela_aviso("Valor precisa ser maior que 0!", "red")
            return

        for linha_existente in dict_linhas.keys(): # Percorre todas as linhas existentes
            if linha.cidade_origem == linha_existente.cidade_origem and linha.cidade_destino == linha_existente.cidade_destino and linha.horario_saida == linha_existente.horario_saida:
                # Se achar uma linha identida a adicionada, ele entra no if
                janela_aviso("Linha já existente!", "red")
                return
    except Exception as e:
        janela_aviso(f"Ocorreu o erro {e}", "red")    
        return
    
    dict_linhas[linha] = list() # Se nao existir linha igual, ele cria a linha e define que valor receberá uma lista
    
    data_usuario = datetime.datetime.now().date() # Pega a data do usuario
    
    # Assim que a linha é criada, ela terá que inicializar com onibus de 30 datas apartir dela, dela mais 30

    for dia in range(30): # Faz um for de 0 a 30
        dia_onibus = data_usuario + datetime.timedelta(days=dia) # Coloca a data do ônibus sempre igual a mais a variável dia do for a data do usuário até dar 30
        
        onibus = Onibus(dia_onibus) # Cria um onibus com a data da variavel

        dict_linhas[linha].append(onibus) # Adiciona o onibus na lista de onibus da linha

    janela_aviso("Linha adicionado!", "green")                                                                                    

def verifica_reserva(dict_linhas, linha, onibus): # Função que verifica se é possivel reserva
    dados_user = datetime.datetime.now() # Pega datra do usuario

    # Cria variaveis para verificar requisitos da reserva
    data_user = dados_user.date() # Data
    hora_user = dados_user.time() # Horario

    data_onibus = datetime.datetime.strptime(onibus.data_formatada, "%d/%m/%Y").date() # Data
    hora_linha = datetime.datetime.strptime(linha.hora_formatada, "%H:%M").time() # Horario

    if data_user > data_onibus: # Se a data do usuario é maior que a do onibus, já passou
        janela_aviso("Onibus ja partiu neste dia!", "red")
        registrar_erro("Reserva nao realizada: Onibus ja partiu neste dia!")
        return False
    
    if data_onibus > data_user + datetime.timedelta(days=30):
        janela_aviso("Data do ônibus é após o limite de 30 dias a partir de hoje!", "red")
        registrar_erro("Reserva não realizada: Data do ônibus é após o limite de 30 dias!")
        return False
    
    if data_user == data_onibus: # Se o onibus for no mesmo dia que deseja fazer a reserva
        if hora_user > hora_linha: # Se o horario ja tiver passado, não é possivel
            janela_aviso("Onibus ja partiu neste horario!", "red")
            registrar_erro("Reserva nao realizada: Onibus ja partiu neste horario!")
            return False
        
    return True # Se não parar em nenhuma restição, OK para horario e data
                          
def editar_rota(dict_linhas, linha_original, cidade_origem, cidade_destino): # Alterar uma rota
    try:
        for linha in dict_linhas.keys(): # Percorre todas as linhas
            if linha.nome == linha_original: # Se encontrar a linha desejada
                linha_aux = Linha(cidade_origem, cidade_destino, linha.horario_saida, linha.valor)
                # Cria uma nova linha com a cidade destino e origem novas, porem conserva o valor e horario

                dict_linhas[linha_aux] = dict_linhas[linha]
                # Aqui ele conserva todos os onibus que haviam na original

                del dict_linhas[linha] # Assim que tudo for alterado, ele remove a linha antiga

                janela_aviso("Linha atualizada!", "green")
                return
            
        janela_aviso("Linha nao encontrada!", "red") # Se nao achar uma linha igual, ela não existe
    except ValueError: # Erro de tipo de dados
        janela_aviso("Tipo de dados invalidos!", "red")
    except Exception as e: # Erro inesperado
        janela_aviso(f"Error: {e}", "red")

def editar_horario(dict_linhas, linha, novo_horario): # Função de editar horario de uma linha
    try:
        for linha_existente in dict_linhas.keys(): # Percorre todo o dicionario
            if linha == linha_existente.nome: # Procura a linha desejada
                linha_alterada = Linha(linha_existente.cidade_origem, linha_existente.cidade_destino, novo_horario, linha_existente.valor)
                dict_linhas[linha_alterada] = dict_linhas[linha_existente]

                del dict_linhas[linha_existente]
                janela_aviso("horario alterado!", "green")
                return
        
        janela_aviso("Linha nao encontrada!", "red") # Caso nao entre nos IFs, a linha não existe
    except ValueError: # Erro de tipo de dado
        janela_aviso("Tipo de dados invalidos!", "red")
    except Exception as e: # Erro inesperado
        janela_aviso(f"Error: {e}", "red")

def remover_onibus(dict_linhas, linha_desejada, nova_data): # Função que remove um onibus da linha
    try:
        for linha, lista_onibus in dict_linhas.items(): # Percorre todo o dicionario
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
        janela_aviso(f"Error: {e}", "red")   

def calcular_vendas_do_mes(dict_linhas, linha_desejada, mes):
    """
    Calcula o faturamento total de um mês específico.
    dict_linhas: dicionário {Linha: [lista de Onibus]}
    mes: número do mês (1–12)
    """
    
    if not dict_linhas:
        janela_aviso("Nao ha linhas!", "red")

    total = 0.0
    mes = int(mes)  # garante número

    for linha_obj, lista_onibus in dict_linhas.items():
        if linha_obj.nome == linha_desejada:
            # preço por passagem está SEMPRE em linha_obj.valor
            preco = float(linha_obj.valor)

            for onibus in lista_onibus:

                # data_partida é um datetime, então pegar o mês direto
                mes_onibus = onibus.data_partida.month

                # só soma se o mês bate
                if mes_onibus == mes:

                    # número de assentos ocupados é só o tamanho da lista
                    ocupados = len(onibus.assentos_ocupados)

                    total += ocupados * preco 
                    # Total vai receber o numero de lugares ocupados vezes o preco

            janela_aviso(f"Valor arrecadado no mes pela linha:\n{total}", "green")
            return total
    janela_aviso("Linha nao encontrada!", "red")
    return

def salvar_relatorio_vendas_txt(dict_linhas, linha_desejada, mes):
    caminho="txts/Relatorio_Mensal.txt"

    total = calcular_vendas_do_mes(dict_linhas, linha_desejada, mes)

    # cria o arquivo se não existir
    modo = "a"  # append (acrescentar no fim)
    
    with open(caminho, modo, encoding="utf-8") as arquivo:

        timestamp = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")

        arquivo.write(f"Cotação no momento [{timestamp}] -> Mês {mes}: R$ {total:.2f}\n")

    janela_aviso("Relatorio emitido via .txt!", "green")
    return total

def registrar_erro(mensagem):
    try:

        # Pega data e hora atual
        data_hora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        # Monta a linha que será escrita no txt
        linha = f"[{data_hora}] - {mensagem}\n"

        # Abre (ou cria) o arquivo e adiciona a nova linha
        with open("txts/logs_erros.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(linha)

    except Exception as e:
        # FAILSAFE: evita que erro dentro da função quebre o sistema
        janela_aviso(f"Falha ao registrar erro: {e}", "red")

def matriz_percentual_ocupacao(dict_linhas, linha_desejada):
    """
    Gera uma matriz onde:
    - cada linha da matriz representa uma linha de ônibus
    - cada coluna representa um dia da semana
    - cada célula contém a ocupação média (%)
    """
    
    # Dias da semana na ordem certa da matriz
    dias_semana = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    matriz_resultado = [dias_semana, []]     # Aqui ficará a matriz final

    try:
        # Percorre todas as entradas do dicionário: linha -> lista de ônibus
        for chave_linha, lista_onibus in dict_linhas.items():
            if chave_linha.nome == linha_desejada:
                
                # Para cada dia da semana, vamos calcular a média
                for dia in dias_semana:
                    numero_onibus_dia = 0 # Guarda o numero de onibus que tem o mesmo dia
                    total_ocupado = 0
                    
                    # Agora percorremos todos os ônibus da linha
                    for onibus in lista_onibus:

                        # Descobrir o dia da semana desse ônibus
                        dia_onibus = onibus.data_partida.strftime("%A")

                        # Se esse ônibus roda no dia que estamos calculando
                        if dia_onibus == dia:
                            total_ocupado += len(onibus.assentos_ocupados) # Pega quantos assentos ocupados nesse onibus
                            numero_onibus_dia += 1 # Adiciona quando haver onibus no dia

                    if numero_onibus_dia > 0:
                        porcentagem = (total_ocupado / numero_onibus_dia) * 5 # Porcentagem é o total ocupado no dia analisado / o numero de onibus desse dia vezes 20
                    else:
                        porcentagem = 0 # para nao ter divisao por 0

                    # Adiciona a média desse dia
                    matriz_resultado[1].append(porcentagem)

            janela_aviso(f"Procentagens\n{matriz_resultado[0]}\n{matriz_resultado[1]}", "black")
            return matriz_resultado
        janela_aviso("Linha nao encontrada!","red")
        return
    except Exception as e:
        janela_aviso(f"Erro:{e}", "red")

def matriz_percentual_ocupacao_txt(dict_linhas, linha_desejada):
    """
    Gera uma matriz onde:
    - cada linha da matriz representa uma linha de ônibus
    - cada coluna representa um dia da semana
    - cada célula contém a ocupação média (%)
    """
    
    # Dias da semana na ordem certa da matriz
    dias_semana = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    matriz_resultado = [dias_semana, []]     # Aqui ficará a matriz final

    try:
        # Percorre todas as entradas do dicionário: linha -> lista de ônibus
        for chave_linha, lista_onibus in dict_linhas.items():
            if chave_linha.nome == linha_desejada:
                
                # Para cada dia da semana, vamos calcular a média
                for dia in dias_semana:
                    numero_onibus_dia = 0 # Guarda o numero de onibus que tem o mesmo dia
                    total_ocupado = 0
                    
                    # Agora percorremos todos os ônibus da linha
                    for onibus in lista_onibus:

                        # Descobrir o dia da semana desse ônibus
                        dia_onibus = onibus.data_partida.strftime("%A")

                        # Se esse ônibus roda no dia que estamos calculando
                        if dia_onibus == dia:
                            total_ocupado += len(onibus.assentos_ocupados) # Pega quantos assentos ocupados nesse onibus
                            numero_onibus_dia += 1 # Adiciona quando haver onibus no di

                    if numero_onibus_dia > 0:
                        porcentagem = (total_ocupado / numero_onibus_dia) * 5 # Porcentagem é o total ocupado no dia analisado / o numero de onibus desse dia vezes 20
                    else:
                        porcentagem = 0

                    # Adiciona a média desse dia
                    matriz_resultado[1].append(porcentagem)

            with open(f"txts/Relatorio_Ocupacao.txt", "a", encoding="utf-8") as arq:# Abre o arquivo .txt
                arq.write(f"Relatorio linha: {linha_desejada} em {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}:\n{matriz_resultado[0]}\n{matriz_resultado[1]}")
                janela_aviso("Relatorio emitido via .txt!", "green")
                return
        janela_aviso("Linha nao encontrada!","red")
        return
    except Exception as e:
        janela_aviso(f"Erro:{e}", "red")

def ler_arquivo(dict_linhas, arquivo): # Função que le um arquivo e faz reserva por ele
    try:
        with open(f"txts/{arquivo}", "r", encoding="utf-8") as arq:# Abre o arquivo .txt
            for linha in arq: # percorre as linhas do arquivo
                linha = linha.strip() # Para quando desce a linha
                infos = linha.split(",") # Separa todas as partes no espaco
                linha = f"{infos[0]} para {infos[1]} as {infos[2]}" # Cria o nome da linha desejada
                data = datetime.datetime.strptime(infos[3], "%d/%m/%Y") # Define a data da reserva
                data = data.strftime("%d/%m/%Y") # Transfomra no objeto de datas
                assento = int(infos[4]) # Define o assento da reserva

                for linha_existente, lista_onibus in dict_linhas.items(): # percorre dicionario
                    if linha_existente.nome == linha: # Encontra a linha que deseja
                        for onibus in lista_onibus: # Percorre a lista de onibus da linha
                            if data == onibus.data_formatada: # Acha o onibus com a data desejada
                                if verifica_reserva(dict_linhas, linha_existente, onibus): # Verifica se pode reservar
                                    onibus.reservar_assento(assento) # Reservar o assento se possivel
                                    return
                                else:
                                    return
                                
                        janela_aviso("Onibus nao encontrado!", "red") # Se nao achar o onibus
                        return
                janela_aviso("Linha nao encontrada!", "red") # Se a linha nao for
                return
    except FileNotFoundError: # Se não achar o arquivo
        janela_aviso("Arquivo nao encontrado!", "red")
    except Exception as e: # Erro inesperado
        janela_aviso(f"Error {e}", "red")
