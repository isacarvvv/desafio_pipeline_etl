"""
Carrega o resultado do summary.csv e exibe as conclusões sobra quais os processos estão ocupando mais
memória e cpu do computador
"""

import pandas as pd


def load():
    # Ler o arquivo summary.csv
    df = pd.read_csv('summary.csv')
    del df["memory"]
    del df["cpu"]
    del df["count"]

    # Ordenar os valores de memória e cpu
    df = df.sort_values(by=['memory_percent', 'cpu_percent'], ascending=False)
    # Exibir os 10 processos que estão ocupando mais memória e cpu, formatando a saida para exibir os valores em porcentagem
    print("Processos consumento mais memória:")
    print(df.head(10).to_string(index=False, float_format='%.2f%%'))

    print("\n\n\n")

    # Ordenar os valores de cpu e memória
    df = df.sort_values(by=['cpu_percent', 'memory_percent'], ascending=False)
    # Exibir os 10 processos que estão ocupando mais memória e cpu, formatando a saida para exibir os valores em porcentagem
    print("Processos consumento mais CPU:")
    print(df.head(10).to_string(index=False, float_format='%.2f%%'))

if __name__ == '__main__':
    load()