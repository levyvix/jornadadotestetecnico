import pandas as pd  # Importa a biblioteca pandas, utilizada para manipulação de dados

# Define o caminho do arquivo JSON de entrada
json_file_path = 'vendas_cerveja.json'

# Define o caminho do arquivo CSV de saída
csv_file_path = 'vendas_cerveja.csv'

# Lê os dados do arquivo JSON e os carrega em um DataFrame do pandas
df = pd.read_json(json_file_path)

# Remove linhas onde a coluna 'vendas' possui valores ausentes
df = df.dropna(subset=['vendas'])

# Exporta os dados transformados para um arquivo CSV, sem incluir o índice do DataFrame
df.to_csv(csv_file_path, index=False)

# Imprime uma mensagem indicando que a transformação foi concluída e o arquivo CSV foi salvo
print(f"Transformação concluída e dados salvos em {csv_file_path}")
