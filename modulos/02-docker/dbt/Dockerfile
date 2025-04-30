FROM python:3.8-slim

# Variáveis de ambiente
ENV PYTHONUNBUFFERED=1 \
    DBT_PROFILES_DIR=/usr/app/profiles

# Diretório de trabalho
WORKDIR /usr/app

# Instalar dependências do sistema
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    git \
    ssh-client \
    software-properties-common \
    make \
    build-essential \
    ca-certificates \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Instalar DBT
RUN pip install --no-cache-dir \
    dbt-core==1.6.0 \
    dbt-postgres==1.6.0 \
    dbt-bigquery==1.6.0

# Criar diretório para profiles
RUN mkdir -p /usr/app/profiles

# Copiar arquivos de configuração
COPY profiles.yml /usr/app/profiles/profiles.yml

# Comando padrão
CMD ["dbt", "debug"] 