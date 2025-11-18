def vendas_do_mes(dirct_linhas, dados_user):

    valor_arrecadado = 0

    if dirct_linhas():
        for linha, lista_onibus in dirct_linhas.items():
            for onibus in lista_onibus:
                if onibus.data_partida.mes == dados_user.mes: #TODO
                    valor_arrecadado += len(onibus.assentos_ocupados) * linha.valor

    print(f"O valor arrecado eh R$ {valor_arrecadado}")
