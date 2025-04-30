# 🐳 Módulo 2: Docker para Ambientes de Dados

## 🔍 Sobre este Módulo
Este módulo aborda os conceitos e práticas essenciais do Docker para ambientes de dados, focando na containerização de aplicações e orquestração de serviços com Docker Compose.

## 📋 Índice

- [Objetivos](#-objetivos-do-módulo)
- [Fundamentos do Docker](#1-fundamentos-do-docker)
- [Dockerfile para Aplicações](#2-dockerfile-para-aplicações-de-dados)
- [Docker Compose](#3-docker-compose)
- [Containerização de Ferramentas](#4-containerização-de-ferramentas-de-dados)
- [Exercícios Práticos](#-exercícios-práticos)

## 🎯 Objetivos do Módulo
- Compreender os fundamentos do Docker e containers
- Aprender a containerizar aplicações de dados
- Dominar Docker Compose para orquestração local
- Implementar boas práticas de containerização

## 📋 Conteúdo

### 1. Fundamentos do Docker

```mermaid
%%{init: { "themeVariables": { "fontFamily": "Arial", "fontSize": "10px" } }}%%
graph TD
    A[Container] --> B[Image]
    B --> C[Dockerfile]
    C --> D[Base Image]
    
    E[Volume] --> A
    F[Network] --> A
    G[Environment] --> A
    
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#bbf,stroke:#333,stroke-width:2px
    style C fill:#bfb,stroke:#333,stroke-width:2px
    style D fill:#fbf,stroke:#333,stroke-width:2px
```

#### 1.1 Conceitos Básicos
- Containers vs VMs
- Images
- Volumes
- Networks
- Docker Registry

#### 1.2 Comandos Essenciais
```bash
# Gerenciamento de Imagens
docker pull
docker build
docker push
docker images

# Gerenciamento de Containers
docker run
docker exec
docker logs
docker stop
docker rm

# Gerenciamento de Volumes
docker volume create
docker volume ls
docker volume rm
```

### 2. Dockerfile para Aplicações de Dados

#### 2.1 Estrutura Básica
```dockerfile
# Base Image
FROM python:3.8-slim

# Variáveis de Ambiente
ENV PYTHONUNBUFFERED=1

# Diretório de Trabalho
WORKDIR /app

# Dependências do Sistema
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Dependências Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Código da Aplicação
COPY . .

# Comando de Execução
CMD ["python", "app.py"]
```

#### 2.2 Boas Práticas
- Multi-stage builds
- Layer caching
- Minimal base images
- Security best practices
- Environment variables

### 3. Docker Compose

```mermaid
%%{init: { "themeVariables": { "fontFamily": "Arial", "fontSize": "10px" } }}%%
graph LR
    A[Docker Compose] --> B[Services]
    B --> C[Networks]
    B --> D[Volumes]
    B --> E[Environment]
    
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#bbf,stroke:#333,stroke-width:2px
```

#### 3.1 Estrutura do docker-compose.yaml
```yaml
version: '3.8'

services:
  jupyter:
    image: jupyter/pyspark-notebook
    ports:
      - "8888:8888"
    volumes:
      - ./notebooks:/home/jovyan/work
    environment:
      - JUPYTER_ENABLE_LAB=yes

  postgres:
    image: postgres:13
    environment:
      - POSTGRES_PASSWORD=secret
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

#### 3.2 Comandos Principais
```bash
docker-compose up
docker-compose down
docker-compose ps
docker-compose logs
docker-compose exec
```

### 4. Containerização de Ferramentas de Dados

#### 4.1 Jupyter com PySpark
```dockerfile
FROM jupyter/pyspark-notebook:latest

USER root

# Instalar dependências adicionais
COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt

USER $NB_UID

EXPOSE 8888
```

#### 4.2 Airflow
```yaml
version: '3.8'
services:
  airflow-webserver:
    image: apache/airflow:2.7.1
    command: webserver
    ports:
      - "8080:8080"
    environment:
      - AIRFLOW__CORE__SQL_ALCHEMY_CONN=postgresql+psycopg2://airflow:airflow@postgres/airflow
    volumes:
      - ./dags:/opt/airflow/dags
```

## 💻 Exercícios Práticos

### Exercício 1: Containerização Básica
1. Crie um Dockerfile para uma aplicação Python simples
2. Construa a imagem e execute o container
3. Mapeie um volume para persistência de dados
4. Exponha uma porta para acesso externo

### Exercício 2: Docker Compose
1. Crie um ambiente com:
   - Jupyter Notebook
   - PostgreSQL
   - Adminer
2. Configure volumes para persistência
3. Defina variáveis de ambiente
4. Teste a comunicação entre containers

### Exercício 3: Airflow Local
1. Configure um ambiente Airflow completo com:
   - Webserver
   - Scheduler
   - PostgreSQL
   - Redis
2. Monte volumes para DAGs e logs
3. Configure conexões externas

## 📚 Recursos Adicionais

### Documentação
- [Docker Documentation](https://docs.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Jupyter Docker Stacks](https://jupyter-docker-stacks.readthedocs.io/)

### Artigos
- [Docker Best Practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
- [Container Security](https://docs.docker.com/engine/security/)

### Vídeos
- [Docker for Data Science](https://www.youtube.com/watch?example1)
- [Docker Compose in Practice](https://www.youtube.com/watch?example2)

## ✅ Quiz

1. Qual a diferença entre `CMD` e `ENTRYPOINT` no Dockerfile?
2. Como funciona o cache de layers no Docker?
3. Por que usar multi-stage builds?
4. Como garantir a segurança em containers Docker?
5. Quais as vantagens do Docker Compose sobre comandos Docker puros?

## 🎯 Projeto do Módulo

### Modern Data Stack Local
Desenvolva um ambiente Docker Compose completo com:

1. Jupyter Lab com PySpark
2. PostgreSQL como fonte de dados
3. Airflow para orquestração
4. DBT para transformações
5. Metabase para visualização

Requisitos:
- Persistência de dados
- Configuração via variáveis de ambiente
- Documentação clara
- Scripts de inicialização
- Testes de integração

## 📝 Avaliação
- Exercícios práticos: 40%
- Quiz: 20%
- Projeto do módulo: 40%

## 🔄 Próximos Passos
No próximo módulo, mergulharemos no Apache Airflow, onde você aprenderá a criar e gerenciar pipelines de dados complexos. 