# 📚 Módulo 1: Fundamentos da Modern Data Stack

## 🔍 Sobre este Módulo
Este módulo aborda os conceitos fundamentais da Modern Data Stack, apresentando a evolução das arquiteturas de dados e os principais componentes que formam uma stack moderna de dados.

## 📋 Índice

- [Objetivos](#-objetivos-do-módulo)
- [Evolução das Arquiteturas](#1-evolução-das-arquiteturas-de-dados)
- [Componentes da Modern Data Stack](#2-componentes-da-modern-data-stack)
- [Conceitos Fundamentais](#3-conceitos-fundamentais)
- [Exercícios Práticos](#-exercícios-práticos)
- [Recursos Adicionais](#-recursos-adicionais)
- [Quiz](#-quiz)
- [Projeto do Módulo](#-projeto-do-módulo)

## 🎯 Objetivos do Módulo
- Compreender a evolução das arquiteturas de dados
- Identificar os componentes principais da Modern Data Stack
- Entender os conceitos de Data Lakehouse
- Conhecer as melhores práticas de arquitetura de dados

## 📋 Conteúdo

### 1. Evolução das Arquiteturas de Dados

```
+-------------------------------------------------------------------------+
|                    Evolução das Arquiteturas de Dados                    |
+------+--------------------------------------------------------+
| 1990 | ► Data Warehouse Tradicional                            |
|      | ► Processos Batch                                       |
|      | ► ETL Clássico                                         |
+------+--------------------------------------------------------+
| 2000 | ► Data Lake                                            |
|      | ► Hadoop                                               |
|      | ► MapReduce                                            |
+------+--------------------------------------------------------+
| 2010 | ► Cloud Data Warehouse                                 |
|      | ► Big Data                                             |
|      | ► Spark                                                |
+------+--------------------------------------------------------+
| 2020 | ► Modern Data Stack                                    |
|      | ► Data Lakehouse                                       |
|      | ► ELT & Streaming                                      |
+------+--------------------------------------------------------+
```

#### 1.1 Desafios Históricos
- Escalabilidade
- Custos de infraestrutura
- Complexidade de manutenção
- Tempo de processamento
- Qualidade dos dados

#### 1.2 Soluções Modernas
- Cloud-first
- Serverless
- Pay-as-you-go
- Automação
- Governança integrada

### 2. Componentes da Modern Data Stack

```
+----------------+     +------------+     +----------------+     +-------------+
| Fontes de Dados| --> | Data Lake  | --> |Data Warehouse | --> | BI/Analytics|
+----------------+     +------------+     +----------------+     +-------------+
                           ▲  ▲                  ▲
                           |  |                  |
              +-----------+   +----------+       |
              |                         |        |
    +------------------+     +------------------+|
    |Orquestração      |     |Processamento     ||
    |(Airflow)         |     |(Spark)           ||
    +------------------+     +------------------+|
                                               ||
                            +------------------+|
                            |Transformação     |
                            |(DBT)             |
                            +------------------+
```

#### 2.1 Camadas Principais

1. **Ingestão de Dados**
   - **Batch vs Streaming**
     - Batch: Processamento em lotes programados, ideal para grandes volumes de dados históricos
     - Streaming: Processamento em tempo real, essencial para dados que precisam ser analisados imediatamente
   
   - **APIs e Conectores**
     - REST APIs: Integração com sistemas modernos via endpoints HTTP
     - Conectores Nativos: Ferramentas especializadas como Fivetran e Airbyte que oferecem integrações prontas
     - CDC (Change Data Capture): Captura de mudanças em tempo real em bancos de dados
   
   - **Formatos de Dados**
     - Estruturados: CSV, JSON, Parquet, Avro
     - Semi-estruturados: XML, logs
     - Não estruturados: Imagens, áudios, documentos

2. **Armazenamento**
   - **Data Lake**
     - Armazenamento de baixo custo para grandes volumes
     - Suporte a dados brutos em qualquer formato
     - Tecnologias: AWS S3, Azure Data Lake Storage, Google Cloud Storage
     - Ideal para exploração e ciência de dados
   
   - **Data Warehouse**
     - Otimizado para consultas analíticas
     - Esquema estruturado e dados processados
     - Tecnologias: Snowflake, BigQuery, Redshift
     - Ideal para BI e relatórios
   
   - **Data Lakehouse**
     - Combina o melhor dos dois mundos
     - Formatos otimizados como Delta Lake e Iceberg
     - Suporte a ACID em dados brutos
     - Ideal para análises avançadas e ML

3. **Processamento**
   - **ETL vs ELT**
     - ETL: Transformação antes do carregamento, ideal para dados sensíveis
     - ELT: Transformação após carregamento, mais flexível e escalável
   
   - **Batch Processing**
     - Processamento em lotes programados
     - Ferramentas: Apache Spark, Apache Flink
     - Ideal para transformações complexas em grandes volumes
   
   - **Stream Processing**
     - Processamento em tempo real
     - Ferramentas: Kafka Streams, Apache Flink
     - Ideal para análises em tempo real e detecção de anomalias

4. **Transformação**
   - **SQL vs Python**
     - SQL: Linguagem padrão para transformações em data warehouses
     - Python: Flexibilidade para transformações complexas e ML
   
   - **DBT (Data Build Tool)**
     - Transformações modulares em SQL
     - Testes e documentação integrados
     - Versionamento e CI/CD para dados
     - Lineage e governança
   
   - **Data Quality**
     - Validação de dados
     - Monitoramento de qualidade
     - Alertas e notificações
     - Ferramentas: Great Expectations, dbt tests

5. **Visualização**
   - **Business Intelligence**
     - Dashboards interativos
     - KPIs e métricas de negócio
     - Ferramentas: Looker, Power BI, Tableau
   
   - **Dashboards**
     - Visualizações customizadas
     - Auto-serviço para usuários finais
     - Compartilhamento e colaboração
   
   - **Self-service Analytics**
     - Exploração ad-hoc de dados
     - SQL notebooks
     - Ferramentas: Metabase, Mode, Preset

6. **Governança e Segurança**
   - **Catálogo de Dados**
     - Metadados e documentação
     - Descoberta de dados
     - Ferramentas: Amundsen, DataHub
   
   - **Linhagem de Dados**
     - Rastreamento de origem e transformações
     - Impacto de mudanças
     - Conformidade e auditoria
   
   - **Controle de Acesso**
     - Autenticação e autorização
     - Mascaramento de dados sensíveis
     - Políticas de segurança

7. **Orquestração**
   - **Workflow Management**
     - Agendamento de jobs
     - Dependências entre tarefas
     - Ferramentas: Apache Airflow, Dagster
   
   - **Monitoramento**
     - Alertas e notificações
     - SLAs e métricas
     - Logs e debugging
   
   - **Recuperação de Falhas**
     - Retry policies
     - Backfill de dados
     - Rollback de mudanças

### 3. Conceitos Fundamentais

#### 3.1 Data Lake
Um Data Lake é um repositório centralizado que permite armazenar todos os seus dados estruturados e não estruturados em qualquer escala. Diferentemente de um data warehouse tradicional, um data lake pode armazenar dados em seu formato bruto, sem necessidade de primeiro estruturar os dados.

```
Fonte de Dados     Ingestão          Data Lake         Consumidores
     |                |                  |                  |
     |  Dados Brutos  |                  |                  |
     |--------------->|                  |                  |
     |                |   Armazena Raw   |                  |
     |                |----------------->|                  |
     |                |                  |                  |
     |  + Dados       |                  |                  |
     |--------------->|                  |                  |
     |                |    Append Raw    |                  |
     |                |----------------->|                  |
     |                |                  |                  |
     |                |                  |  Query Raw Data  |
     |                |                  |<-----------------|
     |                |                  |                  |
     |                |                  |   Return Data    |
     |                |                  |----------------->|
     |                |                  |                  |
```

#### 3.2 Data Warehouse
Um Data Warehouse é um sistema projetado para análise e relatórios de dados. É um repositório central de dados integrados de uma ou mais fontes diferentes.

```
Fonte de Dados    ETL/ELT       Data Warehouse       Analistas
     |              |                |                   |
     | Dados Brutos |                |                   |
     |------------->|                |                   |
     |              | Transforma     |                   |
     |              |--------------->|                   |
     |              |               |                    |
     |              | Carrega DW    |                   |
     |              |-------------->|                   |
     |              |              |                    |
     |              |              | Query Estruturada  |
     |              |              |<------------------|
     |              |              |                   |
     |              |              | Retorna Análise   |
     |              |              |------------------>|
     |              |              |                   |
```

#### 3.3 ETL vs ELT

##### ETL (Extract, Transform, Load)
```
Fonte    Ambiente ETL    Staging    Transformação    Data Warehouse
  |           |             |             |               |
  | Extract   |             |             |               |
  |---------->|             |             |               |
  |           | Load Staging|             |               |
  |           |------------>|             |               |
  |           |             |             |               |
  |           |             | Transform   |               |
  |           |             |------------>|               |
  |           |             |             |               |
  |           |             |             | Load Final    |
  |           |             |             |-------------->|
  |           |             |             |               |
```

##### ELT (Extract, Load, Transform)
```
Fonte    Data Warehouse    Transformação    Consumo
  |            |                |              |
  | Extract    |                |              |
  |----------->|                |              |
  |            | Load Raw       |              |
  |            |--------------->|              |
  |            |                |              |
  |            |    Transform   |              |
  |            |<-------------->|              |
  |            |                |              |
  |            |                | Consumo      |
  |            |                |------------->|
  |            |                |              |
```

#### 3.4 Data Mesh
Uma abordagem descentralizada para gerenciamento de dados que trata dados como um produto e aplica princípios de arquitetura distribuída.

```
Domínio A     Plataforma     Domínio B     Governança    Consumidores
    |             |              |             |              |
    | Dados A     |              |             |              |
    |------------>|              |             |              |
    |             | Registro     |             |              |
    |             |--------------------------->|              |
    |             |              |             |              |
    |             |              | Dados B     |              |
    |             |<-------------|             |              |
    |             | Registro     |             |              |
    |             |--------------------------->|              |
    |             |              |             |              |
    |             |              |             | Políticas    |
    |             |<----------------------------|              |
    |             |              |             |              |
    |             | Dados Governados           |              |
    |             |----------------------------------------->|
    |             |              |             |              |
    |             | Feedback     |             |              |
    |             |<-----------------------------------------|
    |             |              |             |              |
```

## 💻 Exercícios Práticos

### Exercício 1: Análise de Arquitetura
Analise a arquitetura de dados da sua empresa ou de um caso de estudo e identifique:
- Componentes principais
- Pontos de melhoria
- Oportunidades de modernização

### Exercício 2: Design de Solução
Desenhe uma arquitetura Modern Data Stack para um e-commerce que precisa:
- Processar dados de vendas em tempo real
- Análise de comportamento do cliente
- Recomendações de produtos
- Relatórios financeiros

## 📚 Recursos Adicionais

### Artigos
- [The Modern Data Stack](https://www.thoughtworks.com/insights/blog/data-strategy/modern-data-stack)
- [Evolution of the Data Lake](https://www.databricks.com/blog/2020/01/30/what-is-a-data-lakehouse.html)

### Vídeos
- [Modern Data Stack Explained](https://www.youtube.com/watch?example1)
- [Data Lakehouse Architecture](https://www.youtube.com/watch?example2)

### Documentação
- [Databricks Delta Lake](https://docs.databricks.com/delta/index.html)
- [Apache Iceberg](https://iceberg.apache.org/)

## ✅ Quiz

1. Qual a principal diferença entre ETL e ELT?
2. Como o conceito de Data Lakehouse resolve os problemas do Data Lake tradicional?
3. Quais são os benefícios da arquitetura Medallion?
4. Por que a Modern Data Stack é considerada mais ágil que arquiteturas tradicionais?
5. Como a governança de dados se integra com a Modern Data Stack?

## 🎯 Projeto do Módulo

Desenvolva um documento de arquitetura para uma Modern Data Stack que inclua:
1. Diagrama de arquitetura
2. Justificativa para escolha de componentes
3. Estratégia de governança
4. Estimativa de custos
5. Plano de implementação

## 📝 Avaliação
- Participação nas discussões: 20%
- Exercícios práticos: 30%
- Quiz: 20%
- Projeto do módulo: 30%

## 🔄 Próximos Passos
No próximo módulo, mergulharemos no Docker para ambientes de dados, onde você aprenderá a containerizar e orquestrar seus serviços de dados. 

## Arquiteturas Modernas

### 1. Arquitetura Lambda

A arquitetura Lambda é um paradigma de processamento de dados que visa lidar com grandes quantidades de dados combinando processamento em batch e em tempo real.

```
+----------------+     +-----------+
|                |     |           |     +---------------+
| Fontes de      +---->| Ingestão  +---->|  Camada Batch |
| Dados          |     |           |     |   Processing  |
|                |     |           |     +-------+-------+
+----------------+     |           |             |
                      |           |     +--------v--------+
                      |           +---->|  Batch Views    |
                      |           |     |                 |
                      |           |     +--------+--------+
                      |           |              |
                      |           |     +--------v--------+
                      |           |     |                 |
                      |           +---->| Camada Speed    |
                      |           |     |  Processing     |
                      +-----------+     +--------+--------+
                                                |
                                       +--------v--------+
                                       | Realtime Views  |
                                       |                 |
                                       +--------+--------+
                                                |
                                       +--------v--------+
                                       |   Serving       |
                                       |    Layer        |
                                       +--------+--------+
                                                |
                                       +--------v--------+
                                       |  Aplicações     |
                                       |                 |
                                       +----------------+
```

### 2. Arquitetura Kappa

A arquitetura Kappa é uma simplificação da arquitetura Lambda, tratando todos os dados como streams.

```
+----------------+     +------------------+     +------------------+
|                |     |                  |     |                  |
| Fontes de      +---->|  Stream          +---->|  Real-time       |
| Dados          |     |  Processing      |     |  Layer           |
|                |     |                  |     |                  |
+----------------+     +------------------+     +--------+---------+
                                                        |
                                               +--------v---------+
                                               |                  |
                                               |  Serving Layer   |
                                               |                  |
                                               +--------+---------+
                                                        |
                                               +--------v---------+
                                               |                  |
                                               |   Aplicações     |
                                               |                  |
                                               +------------------+
```

### 3. Modern Data Stack

A Modern Data Stack é uma arquitetura que utiliza ferramentas modernas e cloud-native para construir pipelines de dados.

```
+------------------+     +------------------+     +------------------+
|                  |     |   Ferramentas    |     |                  |
|  Fontes de       +---->|   de Ingestão    +---->|  Data Warehouse  |
|  Dados           |     |  Fivetran/Airbyte|     | Snowflake/BigQ  |
|                  |     |                  |     |                  |
+------------------+     +------------------+     +--------+---------+
                                                          |
                                                 +--------v---------+
                                                 |  Transformação   |
                                                 |      (dbt)       |
                                                 |                  |
                                                 +--------+---------+
                                                          |
                                                 +--------v---------+
                                                 |   Analytics/BI   |
                                                 | Looker/Metabase  |
                                                 |                  |
                                                 +------------------+
```

## Exercícios

Para acessar os exercícios deste módulo, consulte os seguintes arquivos:
- [Exercício 1: Conceitos Básicos](exercicios/exercicio-01.md)
- [Exercício 2: Arquiteturas de Dados](exercicios/exercicio-02.md)
- [Exercício 3: Análise Comparativa](exercicios/exercicio-03.md) 