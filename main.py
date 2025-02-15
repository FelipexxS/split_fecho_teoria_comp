import string
import os

from funcao_Split_String import split_string
from funcao_fecho import KleeneLanguage


def processar_string_com_split_e_fecho(texto, delimitador="", max_fecho=1):
    partes = split_string(texto, delimitador)
    print(f"Partes divididas: {partes}")

    resultados_fecho = []
    
    for parte in partes:
        # Gerar manualmente combinações repetidas até max_fecho
        combinacoes = [parte * i for i in range(1, max_fecho + 1)]
        resultados_fecho.append(f"{parte}: {combinacoes}")
    
    # Exibir resultados do fecho com split
    print("\nResultados do Fecho com Split:")
    for resultado in resultados_fecho:
        print(resultado)


def compactar_sequencia_palavras(texto, delimitador=" "):
    partes = split_string(texto, delimitador)
    resultado = []
    n = len(partes)
    i = 0

    while i < n:
        palavra_atual = partes[i]
        count = 1

        while i + 1 < n and partes[i + 1] == palavra_atual:
            count += 1
            i += 1

        resultado.append(f"{palavra_atual}*{count}" if count > 1 else palavra_atual)
        i += 1

    return " ".join(resultado)


# Função para verificar se uma frase é um palíndromo
def verificar_palindromos(texto, delimitador=" "):
    partes = split_string(texto, delimitador)
    palindromos = []
    
    for parte in partes:
        if parte == parte[::-1]:  # Verifica se a palavra é igual ao seu reverso
            palindromos.append(parte)
    
    return palindromos


# Função para Processamento de Dados em Lote (Vendas)
def processar_dados_vendas(arquivo, delimitador=","):
    total_vendas = 0
    transacoes = []
    
    with open(arquivo, 'r') as f:
        for linha in f:
            # Remover possíveis quebras de linha
            linha = linha.strip()
            # Dividir os campos de cada transação (ID, Quantidade, Preço)
            campos = split_string(linha, delimitador)
            if len(campos) == 3:
                id_produto, quantidade, preco = campos
                try:
                    quantidade = int(quantidade)
                    preco = float(preco)
                    # Calcular o total da transação
                    total_transacao = quantidade * preco
                    transacoes.append((id_produto, quantidade, preco, total_transacao))
                    total_vendas += total_transacao
                except ValueError:
                    print(f"Erro ao processar os dados na linha: {linha}")
    
    return transacoes, total_vendas

def processar_log_eventos_criticos(arquivo_log):
    eventos_criticos = ["WARNING", "ERROR", "CRITICAL"]
    eventos = {}
    with open(arquivo_log, "r") as f:
        for linha in f:
            campos = split_string(linha,  ";")
            timestamp, tipo_evento, mensagem, valor = campos
            if tipo_evento not in eventos and tipo_evento in eventos_criticos:
                eventos[tipo_evento] = [f"{timestamp}: {mensagem} => {valor}"]
            elif tipo_evento in eventos and tipo_evento in eventos_criticos:
                eventos[tipo_evento].append(f"{timestamp}: {mensagem} => {valor}")
    return eventos


if __name__ == "__main__":
    # Exemplo 1: Fecho de Kleene com "0" e "1", permitindo a sequência vazia
    L = KleeneLanguage(["0", "1"], allow_empty=True)
    resultado_ate_3 = L ^ 3  # Fecho até o comprimento 3
    print("Fecho de Kleene até comprimento 3 (L = {0,1}, com ε):")
    print(resultado_ate_3)

    # Exemplo 2: Fecho de Kleene com "ab", "cd", "ef", sem permitir a sequência vazia
    L2 = KleeneLanguage(["ab", "cd", "ef"], allow_empty=False)
    resultado_ate_4 = L2 ^ 4  # Fecho até o comprimento 4
    print("\nFecho de Kleene até comprimento 4 (L = {ab, cd, ef}, sem ε):")
    print(resultado_ate_4)

    # Exemplo 3: Fecho de Kleene com "0" e "1", sem permitir a sequência vazia
    resultado_ate_5 = L ^ 5  # Fecho até o comprimento 5
    print("\nFecho de Kleene até comprimento 5 (L = {0, 1}, sem ε):")
    print(resultado_ate_5)

    # Exemplo 4: Texto para testar a divisão, fecho e compactação
    texto = "sol sol lua lua lua estrela estrela estrela estrela sol lua sol lua lua estrela"
    delimitador = " "
    max_fecho = 1

    print("\n=== Processamento com Split, Fecho e Compactação ===")
    processar_string_com_split_e_fecho(texto, delimitador, max_fecho)

    print("\nCompactação de sequência:")
    resultado_compactado = compactar_sequencia_palavras(texto, delimitador)
    print("Entrada:", texto)
    print("Saída compactada:", resultado_compactado)

    # Exemplo 5: Verificar palíndromos em frases
    texto_palindromos = "radar sol ana arara computar level"
    palindromos = verificar_palindromos(texto_palindromos)
    print("\nPalíndromos encontrados:")
    print(palindromos)

    # Exemplo 6: Processamento de Dados em Lote (Vendas)
    # Caminho absoluto para o arquivo de vendas
    arquivo_vendas = r"./vendas.txt"
    
    # Verifique se o arquivo existe
    if os.path.exists(arquivo_vendas):
        transacoes, total_vendas = processar_dados_vendas(arquivo_vendas)
        
        print("\nTransações Processadas:")
        for transacao in transacoes:
            id_produto, quantidade, preco, total_transacao = transacao
            print(f"ID: {id_produto}, Quantidade: {quantidade}, Preço: {preco}, Total da Transação: {total_transacao}")
        
        print(f"\nTotal de Vendas: {total_vendas}")
    else:
        print("O arquivo 'vendas.txt' não foi encontrado no diretório especificado.")
        
    # Exemplo 7: Processamento de Log 
    arquivo_log = r"./mock_log_file.txt"
    eventos = processar_log_eventos_criticos(arquivo_log)
    contador_de_tipos = {tipo: len(mensagens) for tipo, mensagens in eventos.items()}
    print(f"\nEventos Críticos Processados: {contador_de_tipos}\n")
    for tipo_evento, mensagens in eventos.items():
        print(f"Tipo de Evento: {tipo_evento}")
        for mensagem in mensagens:
            print(mensagem)
    print("\n=== Fim do Processamento ===")
     

'''

SAIDA DO TERMINAL 

Fecho de Kleene até comprimento 3 (L = {0,1}, com ε):
['', '0', '1', '00', '01', '10', '11', '000', '001', '010', '011', '100', '101', '110', '111']

Fecho de Kleene até comprimento 4 (L = {ab, cd, ef}, sem ε):
['ef', 'ab', 'cd', 'efef', 'efab', 'efcd', 'abef', 'abab', 'abcd', 'cdef', 'cdab', 'cdcd']

Fecho de Kleene até comprimento 5 (L = {0, 1}, sem ε):
['', '0', '1', '00', '01', '10', '11', '000', '001', '010', '011', '100', '101', '110', '111', '0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111', '00000', '00001', '00010', '00011', '00100', '00101', '00110', '00111', '01000', '01001', '01010', '01011', '01100', '01101', '01110', '01111', '10000', '10001', '10010', '10011', '10100', '10101', '10110', '10111', '11000', '11001', '11010', '11011', '11100', '11101', '11110', '11111']

=== Processamento com Split, Fecho e Compactação ===
Partes divididas: ['sol', 'sol', 'lua', 'lua', 'lua', 'estrela', 'estrela', 'estrela', 'estrela', 'sol', 'lua', 'sol', 'lua', 'lua', 'estrela']

Resultados do Fecho com Split:
sol: ['sol']
sol: ['sol']
lua: ['lua']
lua: ['lua']
lua: ['lua']
estrela: ['estrela']
estrela: ['estrela']
estrela: ['estrela']
estrela: ['estrela']
sol: ['sol']
lua: ['lua']
sol: ['sol']
lua: ['lua']
lua: ['lua']
estrela: ['estrela']

Compactação de sequência:
Entrada: sol sol lua lua lua estrela estrela estrela estrela sol lua sol lua lua estrela
Saída compactada: sol*2 lua*3 estrela*4 sol lua sol lua*2 estrela

Palíndromos encontrados:
['radar', 'ana', 'arara', 'level']

Transações Processadas:
ID: 1, Quantidade: 10, Preço: 50.0, Total da Transação: 500.0
ID: 2, Quantidade: 5, Preço: 100.0, Total da Transação: 500.0
ID: 3, Quantidade: 20, Preço: 30.0, Total da Transação: 600.0
ID: 4, Quantidade: 3, Preço: 150.0, Total da Transação: 450.0
ID: 5, Quantidade: 15, Preço: 60.0, Total da Transação: 900.0

Total de Vendas: 2950.0

Eventos Críticos Processados: {'WARNING': 2, 'ERROR': 2}

Tipo de Evento: WARNING
2023-10-27 10:20:00: High CPU usage => Process ID 1234

2023-10-27 10:05:00: Low disk space => C:\ drive

Tipo de Evento: ERROR
2023-10-27 10:10:00: Database connection failed => SQL Server

2023-10-27 10:25:00: Application crash => NullPointerException

=== Fim do Processamento ===
'''


