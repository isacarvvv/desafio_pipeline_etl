"""
Utilizando a biblioteca pandas, totaliza a memoria e a cpu do arquivo extractions.csv e salva o resultado do calculo no arquivo
summary.csv
"""

import csv
import pandas as pd

def transform():
    # Ler o arquivo extractions.csv
    df = pd.read_csv('extractions.csv', dtype={'memory': float, 'cpu': float, 'datetime': str})
    # Data não será usada no calculo
    del df['datetime']
    # Adicionar contador de linha
    df["count"] = 1
    # Agrupar os processos por nome
    df_grp = df.groupby('name')
    # Somar os valores de memória e cpu
    df_sum = df_grp.sum()
    # Calcular a média de memória e cpu
    df_sum['memory_percent'] = df_sum['memory'] / df_sum['count']
    df_sum['cpu_percent'] = df_sum['cpu'] / df_sum['count']
    # Salvar o resultado no arquivo summary.csv
    df_sum.to_csv('summary.csv')


if __name__ == '__main__':
    transform()