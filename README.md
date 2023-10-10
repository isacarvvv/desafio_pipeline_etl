# Desafio Pipeline ETL
Repositório para o desafio "Crie seu próprio pipeline de ETL"

# Objetivo
Criar uma ferramenta para monitorar processos em execução em um computador,
e assim identificar processos que estão ocupando muitos recursos(memoria e cpu), e deixando o
computador lento.
No processo de ETL seão feitos as seguintes operações:

- extract.py
Periodicamente o script extract.py deve ser executado por um agendador,
ele coletará os processos em execução, a porcentagem de uso de memória e cpu,
e armazenará o resultado no final do arquivo extractions.csv

- transform.py
Totaliza a memoria e a cpu do arquivo extractions.csv e salva o resultado do calculo no arquivo
summary.csv

- load.py
Carrega o resultado do summary.csv e exibe as conclusões sobra quais os processos estão ocupando mais
memória e cpu do computador

# Instalação de dependencias
pip -r requirements.txt

# Execução dos scripts

python extract.py

python transform.py

python load.py