def split_string(texto, delimitador=" "):
    resultado = []  # Lista para armazenar as partes da string
    palavra = ""  # Variável para armazenar caracteres temporariamente
    tamanho_delimitador = len(delimitador)
    i = 0  # Índice para percorrer o texto
    
    while i < len(texto):
        # Verifica se encontrou o delimitador na posição atual
        if texto[i:i + tamanho_delimitador] == delimitador:
            if palavra:  # Adiciona a palavra acumulada se não estiver vazia
                resultado.append(palavra)
                palavra = ""  # Reinicia a palavra acumulada
            i += tamanho_delimitador  # Avança o índice além do delimitador
        else:
            palavra += texto[i]  # Adiciona caractere à palavra atual
            i += 1  # Avança para o próximo caractere
    
    if palavra:  # Adiciona a última palavra se existir
        resultado.append(palavra)
    
    return resultado

