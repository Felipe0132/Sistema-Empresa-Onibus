Sistema de Empresa de Ônibus (Python)

Este projeto simula o sistema interno utilizado pelos funcionários de uma empresa de ônibus.
Ele permite cadastrar linhas, criar ônibus, registrar reservas, gerar relatórios e verificar informações de ocupação.
O sistema foca em automação: assim que uma linha é criada, todos os ônibus necessários são gerados dinamicamente.

Funcionalidades Principais
Criação de Linhas

O funcionário informa:

Cidade de origem

Cidade de destino

Horário da linha

Valor da passagem

Após criar a linha:

São automaticamente gerados 30 ônibus (um para cada dia do mês)

Cada ônibus possui 20 lugares

Números ímpares → lugares na janela

Números pares → lugares no corredor

Gerenciamento de Ônibus

O funcionário pode:

Adicionar ônibus extra informando data e linha

Remover ônibus

Alterar horário

Editar rota (origem e destino)

Tudo realizado pela interface gráfica com janelas informativas.

Reserva de Assentos
Pela Interface

O funcionário seleciona:

Linha

Data de saída

Assento desejado

O sistema exibe mensagens automáticas indicando:

Assento reservado

Assento ocupado

Ônibus cheio

Ônibus já partiu

Entrada inválida

Via Arquivo .txt

O funcionário informa o arquivo contendo várias reservas

O sistema processa todas automaticamente

Registro de Erros

Toda tentativa de reserva não concluída é registrada em um arquivo .txt contendo:

Data e horário

Motivo do erro

Relatórios
Faturamento Mensal de uma Linha

O sistema:

Verifica todas as passagens vendidas no mês

Calcula o valor total com base no preço da linha

Gera um arquivo .txt ou exibe na interface

Percentual de Ocupação por Dia da Semana

Para uma linha específica, o sistema calcula:

A ocupação média (%)

Dividida por dia da semana

Apresentada como matriz ou gerada em .txt

Como Executar o Programa
Pré-requisitos

É necessário ter instalado:

Python 3

datetime

numpy

tkinter

customtkinter

os

Para instalar o customtkinter:

pip install customtkinter

Execução

Baixe o repositório

Abra o terminal e navegue até a pasta do projeto

Execute:

python3 -m Main.main001


A interface principal será aberta automaticamente.

Interface (GUI)

A interface permite:

Adicionar linha

Adicionar ônibus extra

Comprar passagem

Editar rota

Editar horário

Remover ônibus

Gerar relatórios

Processar arquivos de reservas (.txt)

Mini-janelas exibem as linhas cadastradas para facilitar a navegação.

Estrutura do Código (Resumo)
Main/
 └── main001.py
Linhas/
 └── Linha.py
Onibus/
 └── Onibus.py
Interface/
 ├── telas.py
 ├── janelas/
 └── avisos/
Relatorios/
 ├── faturamento.py
 └── ocupacao.py
Utils/
 └── registrar_erros.py
