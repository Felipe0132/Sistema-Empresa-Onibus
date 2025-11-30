from datetime import datetime
import os


def calcular_vendas_do_mes(dirct_linhas, mes):
    """
    Calcula o faturamento total de um mês específico.
    dirct_linhas: dicionário {Linha: [lista de Onibus]}
    mes: número do mês (1–12)
    """
    
    if not dirct_linhas:
        return 0.0

    total = 0.0
    mes = int(mes)  # garante número

    for linha_obj, lista_onibus in dirct_linhas.items():

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

    return total


def salvar_relatorio_vendas_txt(dirct_linhas, mes, caminho="relatorio_mensal.txt"):

    total = calcular_vendas_do_mes(dirct_linhas, mes)

    # cria o arquivo se não existir
    modo = "a"  # append (acrescentar no fim)
    
    with open(caminho, modo, encoding="utf-8") as arquivo:

        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M")

        arquivo.write(f"[{timestamp}] Mês {mes}: R$ {total:.2f}\n")

    return total
