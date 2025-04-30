"""
Script Spark para processamento dos dados de voos.
Este script lê os dados brutos, aplica transformações e salva os resultados.
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_timestamp, round, avg, count
from pyspark.sql.types import StructType, StructField, StringType, TimestampType, DecimalType
import argparse

def criar_spark_session():
    """
    Cria e configura a sessão Spark.
    """
    return SparkSession.builder \
        .appName("ProcessamentoVoos") \
        .config("spark.sql.warehouse.dir", "/tmp/spark-warehouse") \
        .config("spark.executor.memory", "2g") \
        .config("spark.driver.memory", "2g") \
        .getOrCreate()

def definir_schema():
    """
    Define o schema para os dados de voos.
    """
    return StructType([
        StructField("numero_voo", StringType(), True),
        StructField("origem", StringType(), True),
        StructField("destino", StringType(), True),
        StructField("data_partida", TimestampType(), True),
        StructField("data_chegada", TimestampType(), True),
        StructField("preco", DecimalType(10,2), True),
        StructField("data_processamento", TimestampType(), True)
    ])

def ler_dados(spark, input_path):
    """
    Lê os dados do CSV usando o schema definido.
    """
    return spark.read \
        .option("header", "true") \
        .schema(definir_schema()) \
        .csv(input_path)

def aplicar_transformacoes(df):
    """
    Aplica transformações nos dados:
    1. Calcula duração do voo
    2. Calcula preço médio por rota
    3. Agrega estatísticas por origem/destino
    """
    # Calcular duração do voo em horas
    df_duration = df.withColumn(
        "duracao_horas",
        round((col("data_chegada").cast("long") - col("data_partida").cast("long")) / 3600, 2)
    )
    
    # Calcular preço médio por rota
    df_preco_medio = df_duration.groupBy("origem", "destino") \
        .agg(
            round(avg("preco"), 2).alias("preco_medio"),
            count("*").alias("total_voos")
        )
    
    # Estatísticas por origem
    df_stats_origem = df_duration.groupBy("origem") \
        .agg(
            count("*").alias("voos_partida"),
            round(avg("preco"), 2).alias("preco_medio_partida")
        )
    
    # Estatísticas por destino
    df_stats_destino = df_duration.groupBy("destino") \
        .agg(
            count("*").alias("voos_chegada"),
            round(avg("preco"), 2).alias("preco_medio_chegada")
        )
    
    return {
        "voos_detalhados": df_duration,
        "preco_medio_rota": df_preco_medio,
        "stats_origem": df_stats_origem,
        "stats_destino": df_stats_destino
    }

def salvar_resultados(dataframes, output_path):
    """
    Salva os resultados em formato parquet.
    """
    for nome, df in dataframes.items():
        output = f"{output_path}/{nome}"
        df.write.mode("overwrite").parquet(output)
        print(f"Dados salvos em: {output}")

def main():
    # Configurar argumentos da linha de comando
    parser = argparse.ArgumentParser(description='Processamento de dados de voos com Spark')
    parser.add_argument('--input', required=True, help='Caminho do arquivo CSV de entrada')
    parser.add_argument('--output', default='/tmp/voos_processados', help='Diretório de saída para os resultados')
    args = parser.parse_args()

    # Criar sessão Spark
    spark = criar_spark_session()
    
    try:
        # Ler dados
        print(f"Lendo dados de: {args.input}")
        df_voos = ler_dados(spark, args.input)
        
        # Aplicar transformações
        print("Aplicando transformações...")
        resultados = aplicar_transformacoes(df_voos)
        
        # Salvar resultados
        print(f"Salvando resultados em: {args.output}")
        salvar_resultados(resultados, args.output)
        
        print("Processamento concluído com sucesso!")
        
    except Exception as e:
        print(f"Erro durante o processamento: {str(e)}")
        raise
    
    finally:
        spark.stop()

if __name__ == "__main__":
    main() 