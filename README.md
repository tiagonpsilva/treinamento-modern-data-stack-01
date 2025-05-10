# 🚀 Treinamento Modern Data Stack

## 🔍 Sobre este Projeto
Este treinamento completo sobre Modern Data Stack foi desenvolvido para profissionais que desejam dominar as principais ferramentas e práticas do ecossistema moderno de dados. Com foco em casos práticos de análise de voos e hospedagens, o treinamento oferece uma experiência hands-on com as tecnologias mais relevantes do mercado.

## 📋 Índice

- [Objetivos](#-objetivos)
- [Público-Alvo](#-público-alvo)
- [Pré-requisitos](#-pré-requisitos)
- [Tecnologias Abordadas](#%EF%B8%8F-tecnologias-abordadas)
- [Cronograma](#-cronograma)
- [Estrutura do Treinamento](#%EF%B8%8F-estrutura-do-treinamento)
- [Módulos](#-módulos)
- [Setup do Ambiente](#%EF%B8%8F-setup-do-ambiente)
- [Avaliação](#-avaliação)
- [Recursos Adicionais](#-recursos-adicionais)
- [Suporte](#-suporte)

## 🎯 Objetivos
- Dominar os fundamentos da Modern Data Stack
- Desenvolver pipelines de dados completos
- Implementar boas práticas de engenharia de dados
- Criar soluções escaláveis e manuteníveis

## 🔍 Público-Alvo
- Engenheiros de Dados
- Analistas de Dados
- Cientistas de Dados
- Desenvolvedores interessados em dados

## 📚 Pré-requisitos
- Conhecimento básico de Python
- Familiaridade com SQL
- Noções de linha de comando
- Conceitos básicos de Cloud Computing

## ⚙️ Tecnologias Abordadas
- Docker e Docker Compose
- Apache Airflow
- Apache Spark
- Google BigQuery
- DBT (Data Build Tool)
- DuckDB (banco de dados analítico local)
- Metabase

## 📅 Cronograma

```
+------------------------------------------------------------------------------+
|                           Cronograma do Treinamento                           |
+---------------+---------------------------+--------------------------------+
| Módulo        | Data Início              | Duração                        |
+---------------+---------------------------+--------------------------------+
| Fundamentos   | 2024-01-01               | ███ 3 dias                     |
| Docker        | 2024-01-04               | ███ 3 dias                     |
| Airflow       | 2024-01-07               | ███ 3 dias                     |
| DBT           | 2024-01-10               | ███ 3 dias                     |
| Spark         | 2024-01-13               | ███ 3 dias                     |
| BigQuery      | 2024-01-16               | ███ 3 dias                     |
| Projeto Final | 2024-01-19               | ███ 3 dias                     |
+---------------+---------------------------+--------------------------------+
```

## 🗺️ Estrutura do Treinamento

```
                    +-------------------+
                    | Modern Data Stack |
                    +-------------------+
                             |
         +------------------+------------------+
         |        |        |        |         |         |         |
         v        v        v        v         v         v         v
+----------------+  +----------+  +---------+  +-----+  +-------+  +---------+  +-------------+
| 1. Fundamentos |  | 2.Docker |  |3.Airflow|  |4.DBT|  |5.Spark|  |6.BigQuery|  |7.Proj.Final |
+----------------+  +----------+  +---------+  +-----+  +-------+  +---------+  +-------------+
```

## 📂 Módulos

### [Módulo 1: Fundamentos da Modern Data Stack](modulos/01-fundamentos)
- Introdução à Modern Data Stack
- Arquitetura de Dados Moderna
- Conceitos Fundamentais
- Setup do Ambiente

### [Módulo 2: Docker para Ambientes de Dados](modulos/02-docker)
- Fundamentos do Docker
- Containerização de Aplicações
- Docker Compose
- Boas Práticas

### [Módulo 3: Apache Airflow - Orquestração de Dados](modulos/03-airflow)
- Fundamentos do Airflow
- Desenvolvimento de DAGs
- Operadores e Sensores
- Monitoramento

### [Módulo 4: DBT - Transformação de Dados](modulos/04-dbt)
- Fundamentos do DBT
- Modelagem de Dados
- Testes e Documentação
- Boas Práticas

### [Módulo 5: Apache Spark - Processamento Distribuído](modulos/05-spark)
- Fundamentos do Spark
- PySpark
- Otimização
- Integração

### [Módulo 6: BigQuery e Data Warehouse](modulos/06-bigquery)
- Fundamentos de DW
- BigQuery
- Otimização
- Custos

### [Módulo 7: Projeto Final Integrado](modulos/07-projeto-final)
- Sistema Completo
- Integração
- Documentação
- Apresentação

## 🛠️ Setup do Ambiente

### Requisitos de Sistema
- Docker 24.0+
- Python 3.8+
- Git
- 8GB RAM (mínimo)
- 50GB espaço em disco

### Instalação
1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/modern-data-stack-training.git
cd modern-data-stack-training
```

2. Configure o ambiente
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

3. Inicie os serviços
```bash
docker-compose up -d
```

4. Verifique a instalação
```bash
python verify_environment.py
```

## 📊 Avaliação
- Exercícios Práticos: 30%
- Quizzes: 20%
- Projeto Final: 50%

## 📚 Recursos Adicionais
- [Modern Data Stack Blog](https://www.moderndatastack.xyz/blog)
- [Data Engineering Roadmap](https://roadmap.sh/data-engineer)
- [DBT Best Practices](https://docs.getdbt.com/best-practices)
- [Airflow Documentation](https://airflow.apache.org/docs/)

## 👨‍🏫 Suporte
- Discord: [Link para servidor]
- GitHub Issues: [Link para issues]
- Email: suporte@moderndatastack.com

## 🦆 DuckDB: SQL Analítico Local e Prototipagem

O DuckDB é um banco de dados analítico embutido, orientado a colunas, projetado para processamento analítico local (OLAP) de alta performance. Ele é ideal para:
- Laboratórios de SQL
- Prototipagem de pipelines
- Testes rápidos sem necessidade de infraestrutura

### Instalação
O DuckDB já está incluído no `requirements.txt`. Para instalar manualmente:
```bash
pip install duckdb
```

### Exemplo rápido de uso em Python
```python
import duckdb

# Cria um banco em memória e executa uma query
con = duckdb.connect()
con.execute("CREATE TABLE voos (id INTEGER, origem VARCHAR, destino VARCHAR)")
con.execute("INSERT INTO voos VALUES (1, 'GRU', 'JFK'), (2, 'JFK', 'LHR')")
result = con.execute("SELECT * FROM voos").fetchdf()
print(result)
```

### Documentação
- [Documentação oficial do DuckDB](https://duckdb.org/docs/)
- [dbt-duckdb adapter](https://docs.getdbt.com/reference/warehouse-setups/duckdb-setup) 