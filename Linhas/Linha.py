from datetime import datetime

class Linha():
    def __init__(self, cidade_origem, cidade_destino, horario_saida, valor):

        self.cidade_origem = cidade_origem
        self.cidade_destino = cidade_destino

        if isinstance(horario_saida, datetime): # Garante pegar somente o horario
            self.horario_saida = horario_saida.time()
        else:
            self.horario_saida = horario_saida

        self.valor = valor
        self.hora_formatada = self.horario_saida.strftime("%H:%M")
        self.nome = f"{cidade_origem} para {cidade_destino} as {self.hora_formatada}"