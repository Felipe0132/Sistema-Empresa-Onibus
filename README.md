Sistema de Empresa de Ônibus (Python)

Esse projeto simula o sistema interno de uma empresa de ônibus.
Ele não é usado por passageiros, e sim pelos funcionários da empresa, permitindo cadastrar linhas, criar ônibus, registrar reservas, gerar relatórios e verificar informações de ocupação.

O foco do programa é praticidade e automação: assim que uma linha é criada, todos os ônibus necessários são gerados dinamicamente, e todo o fluxo da empresa pode ser controlado pela interface gráfica.

Funcionalidades Principais
 Criação de linhas

O funcionário informa:

cidade de origem

cidade de destino

horário da linha

valor da passagem

Assim que a linha é criada:

são automaticamente gerados 30 ônibus, um para cada dia do mês

cada ônibus sempre tem 20 lugares

números ímpares → lugares na janela

números pares → lugares no corredor

 Gerenciamento de Ônibus

O funcionário pode:

adicionar manualmente um ônibus extra informando data de saída e a linha

remover ônibus de uma linha

alterar horário da linha

editar rota (origem e destino)

Todos esses processos são feitos pela interface gráfica com janelas informativas.

 Reserva de Assentos

A reserva de passagem pode ser feita de duas maneiras:

1) Pela interface

O funcionário escolhe:

a linha

a data de saída

o assento desejado
E o programa mostra mensagens automáticas indicando:

assento reservado

assento ocupado

ônibus cheio

ônibus já partiu

entrada inválida

2) Via arquivo .txt

O funcionário pode informar o endereço de um arquivo contendo várias reservas, e o sistema processa todas automaticamente.

 Registro de erros

Toda tentativa de reserva não concluída é registrada em um arquivo .txt, contendo:

data e horário

motivo do erro (ônibus cheio, assento ocupado, ônibus já partiu, etc.)
Isso garante rastreabilidade e permite auditoria.

 Relatórios Gerados

O sistema contém duas funções principais de relatório:

1) Faturamento mensal de uma linha

O programa:

verifica todas as passagens vendidas ao longo do mês

soma o valor total com base no preço da linha

gera um arquivo .txt com o resultado ou mostra na interface

2) Percentual de ocupação por dia da semana

O sistema calcula, para uma linha específica:

a ocupação média (%)

dividida pelos dias da semana

considerando todos os ônibus do mês

O relatório pode ser exibido:

diretamente na interface

ou gerado em um arquivo .txt

Esse relatório é apresentado como uma matriz onde:

colunas = dias da semana

valores = ocupação média (%) de cada dia

 Como executar o programa
Pré-requisitos

É necessário ter instalado:

Python 3

datetime

numpy

tkinter

customtkinter

os

(Normalmente todas já vêm no Python, exceto customtkinter.)

Passo a passo

Baixe o repositório Sistema-Empresa-Onibus

Abra o terminal e navegue até a pasta do projeto

Execute o comando:

python3 -m Main.main001


A interface principal será aberta automaticamente.

 Interface (GUI)

Ao executar o programa, uma janela aparece com diversas opções:

 Adicionar Linha

Digite cidade de origem

Digite cidade de destino

Digite horário (com instrução do formato)

Digite valor em R$

Após criar, os 30 ônibus do mês são gerados automaticamente.

 Adicionar Ônibus

Digite a data de saída

Digite a linha na qual deseja adicionar o ônibus

 Comprar Passagem

Digite a data de saída

Digite a linha desejada

Interface exibe os assentos disponíveis

Mensagens automáticas orientam o funcionário

Também é possível reservar por arquivo .txt.

 Editar Linhas
Editar rota

selecionar linha

informar nova origem e destino

Editar horário

selecionar linha

informar novo horário

Remover ônibus

selecionar linha

informar a data do ônibus que deseja remover

Todas essas opções possuem mini-janelas de apoio mostrando as linhas cadastradas.

 Relatórios
Venda do mês

selecionar linha

selecionar mês

gera arquivo .txt com total do faturamento

Percentual médio por dia da semana

selecionar linha

escolher se deseja ver pela interface ou gerar .txt

Receber arquivo .txt

carregar arquivo de reservas em massa

sistema processa todas

erros são registrados automaticamente

Estrutura do Código (resumo)

Você pode incluir se quiser, mas deixo uma versão curta:

Main/
  main001.py
Linhas/
  Linha.py
Onibus/
  Onibus.py
Interface/
  telas.py, janelas, avisos
Relatorios/
  faturamento.py
  ocupacao.py
Utils/
  registrar_erros.py
