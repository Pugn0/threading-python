import threading
import os

def api(input):
    print(input)

def processar_quarto(dados):
    api(dados)

def numero_de_threads():
    return os.cpu_count()

def dividir_dados(data, n):
    tamanho_total = len(data)
    tamanho_parte = tamanho_total // n
    sobra = tamanho_total % n
    partes = []
    inicio = 0
    
    for i in range(n):
        fim = inicio + tamanho_parte + (1 if i < sobra else 0)
        partes.append(data[inicio:fim])
        inicio = fim
        
    return partes

# Leitura dos dados
with open('lista.txt', 'r') as arquivo:
    data = arquivo.read()

# Definindo o número de partes baseado no número de CPUs
n_partes = numero_de_threads()
partes_divididas = dividir_dados(data, n_partes)

# Criando e iniciando threads para cada parte dos dados
threads = []
for parte in partes_divididas:
    thread = threading.Thread(target=processar_quarto, args=(parte,))
    thread.start()
    threads.append(thread)

# Esperando todas as threads terminarem
for thread in threads:
    thread.join()
