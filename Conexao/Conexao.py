import datetime
from Linhas.Linha import Linha

def mostrar_linhas(dirct_linhas):
    print("Linha disponiveis:")
    for linhas in dirct_linhas.keys():
        print(linhas.nome, end=", ")

def mostrar_linhas_detalhadas(dirct_linhas):
    print("Linhas e Onibus:")
    for linhas, lista_onibus in dirct_linhas.items():
        print(f"{linhas.nome}: ",end=", ")
        for onibus in lista_onibus:
            print(onibus.data_partida, end=", ")

def adicionar_onibus(dirct_linhas, linha, onibus):
    lista_onibus = list()

    try:
        if linha in dirct_linhas.keys(): # Caso a linha ja existir
            lista_onibus.append(dirct_linhas[linha]) # Cria uma lista auxiliar com todos os onibus que ja haviam
            lista_onibus.append(onibus)

            dirct_linhas[linha] = lista_onibus

            print("Onibus adicionado a linha!")
            return

        dirct_linhas[linha] = onibus # Caso nao existir no dicionario, a linha comeca so com esse onibus
        print("Onibus e linha adicionados juntos!")

    except Exception as e:
        print("Ocorreu um erro ao adicionar!")
        print(e)
    
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
    if linha in dirct_linhas:
        print("Linha ja existente!")
        return
    
    dirct_linhas[linha] = list() # Criando a chave da linha

def atualizar_onibus(dirct_linhas, dados_user):
    lista_aux = list()

    data_user_dia = datetime.datetime.now()
    data_user_hora = data_user_dia.time()

    try:
        for linha, lista_onibus in dirct_linhas.items():
            for onibus in lista_onibus:
                if onibus.data_partida < data_user_dia: # Verifica se a data do usuario eh maior que a dos onibus das linhas
                    lista_aux = lista_onibus
                    lista_aux.remove(onibus) # Remove os onibus que ja passaram da data

                    dirct_linhas[linha] = lista_aux # Atualiza a lista de onibus

                if onibus.data_partida == dados_user.data: # Verifica os onibus que estao no mesmo dia
                    if linha.horario_saida < data_user_hora: # Se o horario de sair ja estiver passado
                        lista_aux = lista_onibus
                        lista_aux.remove(onibus) # Remove os onibus que ja passaram do horario

                        dirct_linhas[linha] = lista_aux # Atualiza a lista de onibus
    except Exception as e:
        print("Ocorreu um erro ao adicionar!")
        print(e)

def reservar_linha_onibus(dirct_linhas, linha, data, dados_user):
    if not data < dados_user.dataatual: # TODO 
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


    
def editar_rota(dirct_linhas):
    mostrar_linhas(dirct_linhas)

    linha = input("Digite o nome da linha que deseja alterar: (CONFORME APARECE A CIMA!) ")

    if not linha in dirct_linhas.keys():
        print("Linha nao existe!")
    else:
        for linha in dirct_linhas.keys():
            if linha == dirct_linhas.nome:
                cidade_origem = input("Digite a cidade origem: ")
                cidade_destino = input("Digite o destino")

                linha_aux = Linha(cidade_origem, cidade_destino, linha.horario_saida, linha.valor)

                dirct_linhas[linha_aux] = dirct_linhas[linha]

                remover_linha(dirct_linhas, linha)

def editar_horario(dirct_linhas):
    mostrar_linhas(dirct_linhas)

    linha = input("Digite o nome da linha que deseja alterar: (CONFORME APARECE A CIMA!) ")

    if not linha in dirct_linhas.keys():
        print("Linha nao existe!")
    else:
        for linha in dirct_linhas.keys():
            if linha == dirct_linhas.nome:
                horario_saida = input("Digite o novo horario") #TODO

                linha_aux = Linha(linha.cidade_origem, linha.cidade_destino, horario_saida, linha.valor)

                dirct_linhas[linha_aux] = dirct_linhas[linha]

                remover_linha(dirct_linhas, linha)

def remover_onibus(dirct_linhas):
    mostrar_linhas(dirct_linhas)
    contador_iguais = 0

    linha = input("Digite o nome da linha que deseja alterar: (CONFORME APARECE A CIMA!) ")

    if not linha in dirct_linhas.keys():
        print("Linha nao existe!")
    else:
        for linha, lista_onibus in dirct_linhas.items():
            if linha == dirct_linhas.nome:
                onibus_select = input("Digite a data de onibus que deseja remover") #TODO

                for onibus in lista_onibus:
                    if onibus.data == onibus_select:
                        dirct_linhas[linha].remove(onibus)
                        contador_iguais += 1
                
    if contador_iguais == 0:
        print("Nenhum onibus assim!")
                        
        