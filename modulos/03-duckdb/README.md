# 🦆 Módulo 3: DuckDB - SQL Analítico Local

## 🔍 Sobre este Módulo
Este módulo apresenta o DuckDB como solução de banco de dados analítico local, ideal para prototipagem, laboratório de SQL, integração com Python e workloads analíticos sem necessidade de infraestrutura de cloud.

## 📋 Índice
- [Objetivos](#-objetivos-do-módulo)
- [Fundamentos do DuckDB](#1-fundamentos-do-duckdb)
- [Comandos e Consultas Básicas](#2-comandos-e-consultas-básicas)
- [Integração com Python e Pandas](#3-integração-com-python-e-pandas)
- [Funções UDF e SQL Avançado](#4-funções-udf-e-sql-avançado)
- [Otimização e Boas Práticas](#5-otimização-e-boas-práticas)
- [Integração com dbt](#6-integração-com-dbt)
- [Exercícios Práticos](#-exercícios-práticos)

## 🎯 Objetivos do Módulo
- Entender o papel do DuckDB na Modern Data Stack
- Executar queries analíticas locais com alta performance
- Integrar DuckDB com Python e Pandas
- Utilizar UDFs e recursos avançados de SQL
- Preparar o ambiente para uso com dbt

## 📋 Conteúdo

### 1. Fundamentos do DuckDB

DuckDB é um banco de dados analítico embutido, orientado a colunas, projetado para processamento OLAP local. Ideal para:
- Laboratórios de SQL
- Prototipagem de pipelines
- Testes rápidos sem infraestrutura

### 2. Comandos e Consultas Básicas

```sql
-- Criar tabela
CREATE TABLE voos (
  id INTEGER,
  origem VARCHAR,
  destino VARCHAR,
  data_partida DATE,
  preco DOUBLE
);

-- Inserir dados
INSERT INTO voos VALUES (1, 'GRU', 'JFK', '2024-01-01', 2500.0);

-- Consultar dados
SELECT origem, destino, AVG(preco) as preco_medio
FROM voos
GROUP BY origem, destino;
```

### 3. Integração com Python e Pandas

```python
import duckdb
import pandas as pd

# Criar DataFrame
voos = pd.DataFrame({
    'id': [1, 2],
    'origem': ['GRU', 'JFK'],
    'destino': ['JFK', 'LHR'],
    'data_partida': ['2024-01-01', '2024-01-02'],
    'preco': [2500.0, 3200.0]
})

# Query SQL sobre DataFrame
result = duckdb.query('SELECT * FROM voos WHERE preco > 2600').to_df()
print(result)
```

### 4. Funções UDF e SQL Avançado

```python
def desconto(preco):
    return preco * 0.9

duckdb.create_function('desconto', desconto, [duckdb.FLOAT], duckdb.FLOAT)

# Usar UDF em SQL
result = duckdb.query('SELECT preco, desconto(preco) as preco_com_desconto FROM voos').to_df()
print(result)
```

#### Exemplo de janela analítica
```sql
SELECT origem, destino, preco,
       AVG(preco) OVER (PARTITION BY origem) as media_origem
FROM voos;
```

### 5. Otimização e Boas Práticas
- Prefira formatos colunares (Parquet) para grandes volumes
- Use consultas diretas em arquivos: `read_parquet('dados/*.parquet')`
- Aproveite integração com Pandas para prototipagem

### 6. Integração com dbt

DuckDB pode ser usado como engine local para projetos dbt. Exemplo de configuração do `profiles.yml`:
```yaml
modern_data_stack:
  target: dev
  outputs:
    dev:
      type: duckdb
      path: ./banco_local.duckdb
      threads: 4
```

### 💻 Exercícios Práticos

#### Exercício 1: Consultas Básicas
- Crie uma tabela de voos e insira dados fictícios
- Calcule o preço médio por origem e destino

#### Exercício 2: Consultas em Arquivos Parquet
- Baixe um arquivo Parquet público e consulte diretamente via DuckDB

#### Exercício 3: Integração com Pandas
- Gere um DataFrame Pandas e execute queries SQL usando DuckDB

#### Exercício 4: UDF e SQL Avançado
- Crie uma função Python customizada e utilize em uma query SQL
- Implemente uma janela analítica (window function)

#### Exercício 5: Integração com dbt
- Configure um projeto dbt local usando DuckDB como engine
- Execute um modelo simples e valide o resultado

---

> Consulte também o notebook `setup/duckdb_lab_avancado.ipynb` para exemplos práticos avançados. 