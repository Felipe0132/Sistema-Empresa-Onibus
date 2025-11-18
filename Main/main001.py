from Linhas.Linha import Linha
from Onibus.Onibus import Onibus

linhas = dict()

linha1 = Linha("Div", "BH", "14:20", 12)
onibus1 = Onibus("21/11")
onibus2 = Onibus("20/11")



linhas[linha1] = onibus1


onibus = list()

onibus.append(linhas[linha1])
onibus.append(onibus2)

linhas[linha1] = onibus

for linha, onibus in linhas.items():
    print(linha.nome, end=": ")
    for oni in onibus:
        print(oni.nome, end=", ")

print("Sistema Rodoviario")
print("[1] Adicionar linha")