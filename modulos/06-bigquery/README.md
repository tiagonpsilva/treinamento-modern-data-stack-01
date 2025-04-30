# 📊 Módulo 6: BigQuery e Data Warehouse

## 🔍 Sobre este Módulo
Este módulo aborda os conceitos e práticas de Data Warehouse usando o Google BigQuery, focando na modelagem dimensional, otimização de consultas e controle de custos.

## 📋 Índice

- [Objetivos](#-objetivos-do-módulo)
- [Fundamentos de Data Warehouse](#1-fundamentos-de-data-warehouse)
- [BigQuery Fundamentals](#2-bigquery-fundamentals)
- [Otimização de Performance e Custos](#3-otimização-de-performance-e-custos)
- [Integração com Modern Data Stack](#4-integração-com-modern-data-stack)
- [Exercícios Práticos](#-exercícios-práticos)

## 🎯 Objetivos do Módulo
- Compreender os fundamentos de Data Warehouse
- Dominar o BigQuery para análise de dados
- Implementar modelagem dimensional eficiente
- Otimizar consultas e custos

## 📋 Conteúdo

### 1. Fundamentos de Data Warehouse

```
+---------+     +---------+     +---------------+     +-----------+     +-------------+
| Fontes  | --> | Staging | --> |Data Warehouse | --> |Data Marts | --> |Visualização |
+---------+     +---------+     +---------------+     +-----------+     +-------------+
```

#### 1.1 Conceitos Básicos
- Arquitetura de DW
- Modelagem Dimensional
- ETL vs ELT
- Data Marts
- Data Lake vs Data Warehouse

#### 1.2 Modelagem Dimensional

```
                  +----------------+
                  |  Dimensão     |
                  |    Tempo      |
                  +----------------+
                         ▲
                         |
+----------------+  +----------+  +----------------+
|   Dimensão     |  |          |  |   Dimensão     |
|   Cliente      |◄-|   FATO   |->|   Produto     |
+----------------+  |          |  +----------------+
                   +----------+
                         |
                         ▼
                  +----------------+
                  |   Dimensão     |
                  |    Local       |
                  +----------------+
```

### 2. BigQuery Fundamentals

#### 2.1 Estrutura do BigQuery
```sql
-- Criar Dataset
CREATE SCHEMA `projeto.dataset`
OPTIONS (
  location = 'US',
  description = 'Dataset para análise de voos'
);

-- Criar Tabela
CREATE TABLE `projeto.dataset.voos`
(
  voo_id STRING,
  data_partida TIMESTAMP,
  origem STRING,
  destino STRING,
  preco FLOAT64
)
PARTITION BY DATE(data_partida)
CLUSTER BY origem, destino;
```

#### 2.2 Consultas Otimizadas
```sql
-- Consulta com particionamento
SELECT 
  origem,
  destino,
  AVG(preco) as preco_medio
FROM `projeto.dataset.voos`
WHERE DATE(data_partida) BETWEEN '2024-01-01' AND '2024-01-31'
GROUP BY 1, 2;

-- Consulta com subquery
WITH voos_dia AS (
  SELECT 
    DATE(data_partida) as data,
    COUNT(*) as total_voos
  FROM `projeto.dataset.voos`
  GROUP BY 1
)
SELECT 
  data,
  total_voos,
  AVG(total_voos) OVER (
    ORDER BY data
    ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
  ) as media_movel_7d
FROM voos_dia
ORDER BY data;
```

### 3. Otimização de Performance e Custos

#### 3.1 Estratégias de Otimização
- Particionamento
- Clustering
- Materialização
- Cache
- Slot Reservation

#### 3.2 Controle de Custos
```sql
-- Visualizar estimativa de processamento
SELECT 
  *
FROM `projeto.dataset.voos`
WHERE DATE(data_partida) = '2024-01-01'
AND origem = 'GRU';

-- Criar tabela particionada a partir de não particionada
CREATE TABLE `projeto.dataset.voos_particionado`
PARTITION BY DATE(data_partida)
CLUSTER BY origem, destino
AS SELECT * FROM `projeto.dataset.voos`;
```

### 4. Integração com Modern Data Stack

#### 4.1 BigQuery com DBT
```yaml
# models/staging/schema.yml
version: 2

sources:
  - name: voos
    database: projeto
    schema: dataset
    tables:
      - name: voos_raw
        columns:
          - name: voo_id
            tests:
              - unique
              - not_null

models:
  - name: stg_voos
    columns:
      - name: voo_id
        tests:
          - unique
          - not_null
```

#### 4.2 BigQuery com Airflow
```python
from airflow.providers.google.cloud.operators.bigquery import BigQueryOperator

create_table = BigQueryOperator(
    task_id='create_table',
    sql='''
    CREATE TABLE IF NOT EXISTS `projeto.dataset.voos`
    (
      voo_id STRING,
      data_partida TIMESTAMP,
      origem STRING,
      destino STRING,
      preco FLOAT64
    )
    PARTITION BY DATE(data_partida)
    ''',
    use_legacy_sql=False,
)
```

## 💻 Exercícios Práticos

### Exercício 1: Modelagem Básica
1. Criar estrutura no BigQuery:
   - Datasets
   - Tabelas particionadas
   - Views
   - Funções UDF

### Exercício 2: Análises Avançadas
1. Desenvolver consultas para:
   - Análise temporal
   - Agregações complexas
   - Window functions
   - Otimização de custos

### Exercício 3: Integração
1. Implementar pipeline completo:
   - Ingestão com Airflow
   - Transformação com DBT
   - Análise no BigQuery
   - Visualização no Metabase

## 📚 Recursos Adicionais

### Documentação
- [BigQuery Documentation](https://cloud.google.com/bigquery/docs)
- [Best Practices](https://cloud.google.com/bigquery/docs/best-practices-performance-overview)
- [Pricing](https://cloud.google.com/bigquery/pricing)

### Artigos
- [BigQuery Performance Tuning](https://cloud.google.com/blog/topics/developers-practitioners/bigquery-explained-working-with-partitioned-tables)
- [Cost Optimization](https://cloud.google.com/blog/topics/developers-practitioners/bigquery-admin-reference-guide-cost-optimization)

### Vídeos
- [BigQuery Fundamentals](https://www.youtube.com/watch?example1)
- [Advanced BigQuery Features](https://www.youtube.com/watch?example2)

## ✅ Quiz

1. Quais são as vantagens do particionamento no BigQuery?
2. Como funciona o modelo de preços do BigQuery?
3. Qual a diferença entre clustering e particionamento?
4. Como otimizar consultas para melhor performance?
5. Quando usar tabelas materializadas vs views?

## 🎯 Projeto do Módulo

### Data Warehouse para Análise de Voos

Desenvolva um projeto completo que:

1. Modelagem
   - Modelo dimensional para voos
   - Hierarquias de análise
   - Histórico temporal
   - Métricas calculadas

2. Otimização
   - Estratégia de particionamento
   - Política de clustering
   - Controle de custos
   - Cache e materialização

3. Análises
   - Dashboard operacional
   - Análise de tendências
   - Previsão de demanda
   - Relatórios automáticos

Requisitos:
- Modelo dimensional correto
- Consultas otimizadas
- Documentação completa
- Controle de custos
- Integração com stack

## 📝 Avaliação
- Exercícios práticos: 30%
- Quiz: 20%
- Projeto do módulo: 50%

## 🔄 Próximos Passos
No próximo e último módulo, desenvolveremos um Projeto Final Integrado que utilizará todos os conceitos e ferramentas aprendidos no treinamento. 