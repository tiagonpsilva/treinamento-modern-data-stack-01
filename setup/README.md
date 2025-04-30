# 🛠️ Setup do Ambiente de Desenvolvimento

Este guia fornece instruções detalhadas para configurar seu ambiente de desenvolvimento para o treinamento Modern Data Stack.

## 📋 Requisitos de Sistema

### Hardware Mínimo
- Processador: 2 cores
- Memória RAM: 8GB
- Espaço em Disco: 20GB livre

### Software Base
- Python 3.8+
- Docker Desktop
- Git
- VS Code ou PyCharm (recomendado)
- Terminal (bash/zsh)

## 🔧 Instalação Passo a Passo

### 1. Python e Ambiente Virtual
```bash
# Instalar Python (caso não tenha)
# MacOS
brew install python@3.8

# Linux
sudo apt-get update
sudo apt-get install python3.8 python3.8-venv

# Criar ambiente virtual
python3.8 -m venv .venv
source .venv/bin/activate

# Instalar dependências base
pip install -r requirements.txt
```

### 2. Docker
1. Baixe e instale o [Docker Desktop](https://www.docker.com/products/docker-desktop)
2. Verifique a instalação:
```bash
docker --version
docker-compose --version
```

### 3. Ferramentas Específicas

#### Apache Airflow
```bash
# Será configurado via Docker Compose
docker-compose -f airflow/docker-compose.yaml up -d
```

#### DBT
```bash
pip install dbt-core dbt-bigquery
```

#### Apache Spark
```bash
# Será utilizado via Docker
docker pull jupyter/pyspark-notebook
```

#### Google Cloud SDK
1. Instale o [Google Cloud SDK](https://cloud.google.com/sdk/docs/install)
2. Configure o acesso:
```bash
gcloud init
gcloud auth application-default login
```

## 📝 Arquivo requirements.txt

```txt
apache-airflow==2.7.1
dbt-core==1.6.0
dbt-bigquery==1.6.0
google-cloud-bigquery==3.11.4
pyspark==3.4.1
requests==2.31.0
python-dotenv==1.0.0
pytest==7.4.2
jupyter==1.0.0
```

## ✅ Verificação do Ambiente

Execute o script de verificação para garantir que tudo está configurado corretamente:

```bash
python setup/verify_environment.py
```

## 🔐 Configuração de Credenciais

1. Crie um arquivo `.env` na raiz do projeto
2. Adicione suas credenciais:

```env
GOOGLE_APPLICATION_CREDENTIALS=path/to/your/credentials.json
AIRFLOW_UID=50000
AIRFLOW_HOME=/opt/airflow
```

## 🆘 Resolução de Problemas Comuns

### Docker
- **Erro de permissão**: Execute `sudo usermod -aG docker $USER`
- **Memória insuficiente**: Aumente a memória nas configurações do Docker Desktop

### Python
- **Conflitos de versão**: Certifique-se de usar o ambiente virtual
- **Erro de dependências**: Execute `pip install --upgrade pip setuptools wheel`

### BigQuery
- **Erro de autenticação**: Verifique se as credenciais estão corretamente configuradas
- **Permissões**: Verifique as IAM roles no console do GCP

## 📞 Suporte

Em caso de problemas:
1. Consulte a [documentação oficial](./docs/troubleshooting.md)
2. Abra uma issue no repositório
3. Entre em contato com o suporte 