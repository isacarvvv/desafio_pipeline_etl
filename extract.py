"""
Coletar os processos em execução, a porcentagem de uso de memória e cpu,
e armazenará o resultado no final do arquivo extractions.csv
"""

import os
import psutil
import time

# Função para coletar os processos em execução, a porcentagem de uso de memória e cpu
def extract():
    # Coletar os processos em execução
    process = psutil.process_iter()
    # Verificar se o arquivo extractions.csv já existe
    arquivo_novo = not os.path.exists('extractions.csv')
    file = open('extractions.csv', 'a')
    # Se o arquivo extractions.csv é novo, escrever o cabeçalho
    if arquivo_novo:
        file.write(f'datetime,name,memory,cpu\n')
    process_list = list(process)
    # Necessário inicializar a coleta da cpu, para retornar a porcentagem correta
    for proc in process_list:
        proc.cpu_percent()
    # Intervalo de coleta
    time.sleep(2)
    for proc in process_list:
        try:
            process_name = proc.name()
            process_memory = proc.memory_percent()
            process_cpu = proc.cpu_percent()
            process_datetime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            # Armazenar os dados no arquivo extractions.csv
            file.write(f'{process_datetime},{process_name},{process_memory:.4f},{process_cpu:.4f}\n')
        except psutil.NoSuchProcess:
            continue
    # Fechar o arquivo extractions.csv
    file.close()


if __name__ == '__main__':
    extract()