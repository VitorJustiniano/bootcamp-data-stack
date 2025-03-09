from time import sleep

from airflow.decorators import dag, task

from datetime import datetime



@dag(
        dag_id="dag_bitcoin",
        description="etl de extracao de cripto",
        schedule="5 0 * 8 *",
        start_date=datetime(2024,3,24),
        catchup=False  #backfill
)
def pipeline():

    @task
    def primeira_atividade():
        print("primeira atividade rodou com sucesso")
        sleep(2)

    @task
    def segunda_atividade():
        print("segunda atividade rodou com sucesso")
    sleep(2)

    @task
    def terceira_atividade():
        print("terceira atividade rodou com sucesso")
        sleep(2)

    
    t1 = primeira_atividade()
    t2 = segunda_atividade()
    t3 = terceira_atividade()

    t1 >> t2 >> t3

pipeline()