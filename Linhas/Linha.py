import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='') # Configurando e colocando chave de acesso na  API

class Linha():
    def __init__(self, cidade_origem, cidade_destino, horario_saida, valor):

        self.cidade_origem = cidade_origem
        self.cidade_destino = cidade_destino
        self.horario_saida = horario_saida
        self.valor = valor
        self.nome = f"{cidade_origem} para {cidade_destino} as {horario_saida}"
        #self.estimar_horario_chegada()




        
    
'''
    # API para retornar o tempo pelo Google Maps de duracao da viagem
    def estimar_horario_chegada(self):

        try:
            matrix = gmaps.distance_matrix([self.cidade_origem], [self.cidade_destino], mode="driving", units="metric")

            if matrix['status'] != 'OK':
                print(f"Erro na requisição da API: {matrix['status']}")
                return

            #print("Matriz de Distâncias e Tempos de Viagem:")

            element = matrix['rows'][0]['elements'][0] # Padrao do JSON

            if element['status'] == 'OK':
                distance = element['distance']['text'] # Recebe a distancia em Km
                duration = element['duration']['text'] # Recebe a distancia em horas e minutos

                self.horario_chegada = duration + self.horario_saida # Definindo o tempo de chegada

                #print(f"De {self.cidade_origem} para {self.cidade_destino}:")
                #print(f"Distância = {distance}, Duração = {duration}")
            else:
                print(f"Rota não encontrada ({element['status']})")

        except Exception as e:
            print(f"Ocorreu um erro: {e}")
'''