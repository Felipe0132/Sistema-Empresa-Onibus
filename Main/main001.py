# Codigo para rodar  python3 -m Main.main001

from Linhas.Linha import Linha
from Onibus.Onibus import Onibus
import Conexao.Conexao as Conexao
import datetime

linhas = dict()

linha1 = Linha("Div", "BH", "14:20", 12)
onibus1 = Onibus("21/11")
onibus2 = Onibus("20/11")


Conexao.adicionar_onibus(linhas, linha1, onibus1)



Conexao.adicionar_onibus(linhas, linha1, onibus2)

for linha, onibus in linhas.items():
    print(linha.nome, end=": ")
    for oni in onibus:
        print(oni.nome, end=", ")

print()