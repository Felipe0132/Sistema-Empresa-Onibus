# Sistema de Empresa de Ônibus (Python)

Este projeto simula o sistema interno utilizado pelos funcionários de
uma empresa de ônibus.\
Ele permite cadastrar linhas, criar ônibus, registrar reservas, gerar
relatórios e verificar informações de ocupação.\
O sistema também automatiza processos: assim que uma linha é criada,
30 ônibus são gerados dinamicamente a partir da data criada.

##  Funcionalidades Principais

##  Criação de Linhas

O funcionário informa:

-   Cidade de origem
-   Cidade de destino
-   Horário da linha
-   Valor da passagem

Após criar a linha:

-   São automaticamente gerados **30 ônibus** (um para cada dia do mês)
-   Cada ônibus possui **20 lugares**
-   **Números ímpares** -> assentos na **janela**
-   **Números pares** -> assentos no **corredor**

##  Gerenciamento de Ônibus

O funcionário pode:

-   Adicionar ônibus extra informando data e linha
-   Remover ônibus
-   Alterar horário
-   Editar rota (origem e destino)

Tudo realizado pela interface gráfica com janelas informativas.

##  Reserva de Assentos

### Pela Interface

O funcionário seleciona:

-   Linha
-   Data de saída
-   Assento desejado

O sistema exibe mensagens indicando:

-    Assento reservado
-    Assento ocupado
-    Ônibus cheio
-    Ônibus já partiu
-    Entrada inválida

### Via Arquivo `.txt`

-   O funcionário informa um arquivo contendo várias reservas ou uma
-   O sistema processa todas automaticamente (sendo necessário apenas colocar o endereço do .txt)

##  Registro de Erros

Toda reserva não concluída é registrada em um arquivo `.txt` contendo:

-   Data e horário\
-   Motivo do erro

##  Relatórios

### Faturamento Mensal de uma Linha

O sistema:

-   Verifica todas as passagens vendidas no mês
-   Calcula o valor total com base no preço da linha
-   Gera um arquivo `.txt` ou exibe na interface

### Percentual de Ocupação por Dia da Semana

O sistema calcula:

-   A ocupação média (%)
-   Por dia da semana durante toda linha 
-   Exibida como matriz na interface ou em `.txt`

##  Como Executar o Programa

### Pré-requisitos

É necessário ter instalado:

-   Python 3\
-   `datetime`
-   `numpy`
-   `tkinter`
-   `customtkinter`
-   `os`

### Execução

1.  Baixe o repositório
2.  Abra o terminal e navegue até a pasta do projeto
3.  Execute:

``` bash
python3 -m Main.main001
```

A interface principal será aberta automaticamente.

##  Interface (GUI)

A interface permite:

-   Adicionar linha
-   Adicionar ônibus extra
-   Comprar passagem
-   Editar rota
-   Editar horário
-   Remover ônibus
-   Gerar relatórios
-   Processar arquivos de reservas `.txt`

Mini-janelas exibem as linhas cadastradas para facilitar a navegação.

##  Estrutura do Código (Resumo)

    Main/Interface
     └── main001.py
    Linhas
     └── Linha.py
    Onibus
     └── Onibus.py
    Conexao
     └── Conexoes.py
    .txt
     └── registrar_erros.py
     └── Relatorio_Mensal
     └── Relatoria_Ocupacao
     └── Reservas
