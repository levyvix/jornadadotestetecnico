### README

# Projeto de ETL: JSON para CSV

## Descrição do Projeto

Este projeto demonstra um processo de ETL (Extract, Transform, Load) simples, onde os dados são extraídos de um arquivo JSON, transformados conforme necessário e carregados em um arquivo CSV. O exemplo utilizado envolve dados de vendas de cerveja por estado durante o Carnaval.

## Objetivo

O objetivo principal deste projeto é transformar dados brutos de um arquivo JSON em um formato estruturado de CSV, facilitando a análise e a manipulação dos dados. Este processo envolve três etapas principais: extração, transformação e carga.

## Importância da Cerveja e do Carnaval

A cerveja é uma das bebidas mais consumidas no Brasil, especialmente durante o Carnaval, que é uma das maiores e mais celebradas festividades do país. O Carnaval atrai milhões de pessoas para festas e eventos, aumentando significativamente o consumo de cerveja. Para a Ambev, entender o comportamento de consumo durante esse período é crucial para estratégias de marketing, logística e vendas.

## Desafio Ambev

Este projeto é parte do desafio Ambev para transformar dados de vendas de cerveja durante o Carnaval em um formato mais acessível e estruturado, utilizando técnicas de ETL. A Ambev busca analisar esses dados para obter insights valiosos sobre o desempenho de suas vendas em diferentes estados.

## Como Rodar o Projeto

1. **Baixe o Projeto:**
   - Faça o download ou clone este repositório para o seu ambiente local.

   ```bash
   git clone https://github.com/lvgalvao/jornadadotestetecnico
   cd jornadadotestetecnico
   git checkout candidato05
   ```

2. **Instale as Bibliotecas:**
   - Assegure-se de que você tem todas as bibliotecas necessárias instaladas. Verifique o arquivo `requirements.txt` para as dependências.

   ```bash
   pip install -r requirements.txt
   ```

3. **Rode o Projeto:**
   - Execute o script principal para iniciar o processo de ETL. Este script irá ler os dados do arquivo JSON, realizar as transformações necessárias e salvar os dados em um arquivo CSV.

   ```bash
   jupyter lab
   ```