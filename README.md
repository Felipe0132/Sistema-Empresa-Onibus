# Sistema de Empresa de Ônibus (Python)
 
Esse é um código que simula um sistema de uma empresa de ônibus que seria utilizado pelos funionários (não pelos consumidores), na qual os ônibus possuem sempre 20 lugares e são criados de forma dinâmica aṕos a criação da linha a qual eles pertecem. Nesse trabalho o usuário insere os dados em uma interface gráfica e a cada ação uma janela aparece.

## Funcionalidades 

* A criação da linha é feita pelo usuário (funcionário da empresa):
    * O usuário insere o local de partida, o local de chegada e a hora de partida da linha .
    * Após a criação da linha são criados de forma automática um ônibus para cada dia do mês (30 ônibus em 30 dias)
      * Cada ônibus possui 20 lugares, sendo os ímares os lugares na janela e os pares os lugares do corredor 
    * Para reservar um lugar é possível selecionar 1 pela interface ou reservar por um arquivo .txt, o qual é necessário colocar o endereço 
    * Sempre é possível trocar o horário da linha, remover um ônibus e alterar o local de partida e de chegada dela
* O código possui funções para gerar relatórios em arquivos txt sendo elas:
    *  Cálculo total do faturamento de determinada linha
    *  Cálculo do percentual de ocupação de detrminada linha dividido pelos dias da semana durante um mẽs (30 dias)
