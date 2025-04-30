"""
DAG de exemplo para o pipeline de análise de voos.
Este pipeline extrai dados de APIs de voos, processa e carrega em um Data Warehouse.
"""

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.providers.http.sensors.http import HttpSensor
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
import json
import requests
import pandas as pd

# Argumentos padrão para todas as tasks
default_args = {
    'owner': 'modern_data_stack',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Funções auxiliares
def _processar_dados_voos(**context):
    """
    Processa os dados brutos de voos e salva em CSV.
    """
    # Obter dados da task anterior
    ti = context['task_instance']
    dados_brutos = ti.xcom_pull(task_ids='extrair_dados_voos')
    
    # Processar dados (exemplo simplificado)
    df = pd.DataFrame(dados_brutos)
    df['data_processamento'] = datetime.now()
    
    # Salvar em CSV
    df.to_csv('/tmp/voos_processados.csv', index=False)
    return '/tmp/voos_processados.csv'

def _enviar_notificacao(**context):
    """
    Envia notificação de conclusão do pipeline.
    """
    data_execucao = context['execution_date']
    print(f"Pipeline de voos concluído com sucesso! Data de execução: {data_execucao}")

# Definição da DAG
with DAG(
    'pipeline_voos',
    default_args=default_args,
    description='Pipeline para análise de dados de voos',
    schedule_interval='@daily',
    catchup=False,
    tags=['voos', 'exemplo'],
) as dag:

    # Task 1: Verificar disponibilidade da API
    verificar_api = HttpSensor(
        task_id='verificar_api',
        http_conn_id='api_voos',
        endpoint='status',
        poke_interval=60,
        timeout=600,
    )

    # Task 2: Extrair dados da API
    extrair_dados_voos = SimpleHttpOperator(
        task_id='extrair_dados_voos',
        http_conn_id='api_voos',
        endpoint='voos',
        method='GET',
        response_filter=lambda response: json.loads(response.text),
        log_response=True,
    )

    # Task 3: Processar dados
    processar_dados = PythonOperator(
        task_id='processar_dados',
        python_callable=_processar_dados_voos,
        provide_context=True,
    )

    # Task 4: Criar tabelas no PostgreSQL
    criar_tabelas = PostgresOperator(
        task_id='criar_tabelas',
        postgres_conn_id='postgres_default',
        sql="""
            CREATE TABLE IF NOT EXISTS voos (
                voo_id SERIAL PRIMARY KEY,
                numero_voo VARCHAR(10),
                origem VARCHAR(3),
                destino VARCHAR(3),
                data_partida TIMESTAMP,
                data_chegada TIMESTAMP,
                preco DECIMAL(10,2),
                data_processamento TIMESTAMP
            );
        """
    )

    # Task 5: Processar com Spark
    processar_spark = SparkSubmitOperator(
        task_id='processar_spark',
        application='/opt/airflow/dags/spark/processar_voos.py',
        conn_id='spark_default',
        conf={
            'spark.driver.memory': '2g',
            'spark.executor.memory': '2g'
        },
        application_args=['--input', '/tmp/voos_processados.csv'],
    )

    # Task 6: Executar transformações DBT
    dbt_run = BashOperator(
        task_id='dbt_run',
        bash_command='cd /usr/app && dbt run --models voos',
    )

    # Task 7: Executar testes DBT
    dbt_test = BashOperator(
        task_id='dbt_test',
        bash_command='cd /usr/app && dbt test --models voos',
    )

    # Task 8: Enviar notificação
    notificar = PythonOperator(
        task_id='notificar',
        python_callable=_enviar_notificacao,
        provide_context=True,
    )

    # Definir dependências
    verificar_api >> extrair_dados_voos >> processar_dados >> criar_tabelas
    criar_tabelas >> processar_spark >> dbt_run >> dbt_test >> notificar 