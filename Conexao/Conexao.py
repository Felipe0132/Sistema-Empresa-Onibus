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
    
def remover_linha(dirct_linha, linha):
    try:
        if linha in dirct_linha.key():
            del dirct_linha[linha]
            print("Linha removida!")
        else:
            print("Linha nao consta no sistema!")
        
    except Exception as e:
        print("Ocorreu um erro ao adicionar!")
        print(e)

def atualizar_onibus(dirct_linha, dados_user):
    lista_aux = list()

    try:
        for linha, lista_onibus in dirct_linha.items():
            for onibus in lista_onibus:
                if onibus.data_partida < dados_user.data: # Verifica se a data do usuario eh maior que a dos onibus das linhas
                    lista_aux = lista_onibus
                    lista_aux.remove(onibus) # Remove os onibus que ja passaram da data

                    dirct_linha[linha] = lista_aux # Atualiza a lista de onibus

                if onibus.data_partida == dados_user.data: # Verifica os onibus que estao no mesmo dia
                    if linha.horario_saida < dados_user.hora: # Se o horario de sair ja estiver passado
                        lista_aux = lista_onibus
                        lista_aux.remove(onibus) # Remove os onibus que ja passaram do horario

                        dirct_linha[linha] = lista_aux # Atualiza a lista de onibus
    except Exception as e:
        print("Ocorreu um erro ao adicionar!")
        print(e)
