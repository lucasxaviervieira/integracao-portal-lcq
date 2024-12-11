from datetime import datetime
from core.insert_df.database_integration.index import PainelBordoDB
from dotenv import load_dotenv
import os

load_dotenv(override=True)


def insert_dataframe(df):
    try:
        db = PainelBordoDB(
            os.getenv("DATABASE_SERVER"),
            os.getenv("DATABASE_NAME"),
            os.getenv("DATABASE_USERNAME"),
            os.getenv("DATABASE_PASSWORD"),
        )

        for index, row in df.iterrows():
            id_ponto_analise = db.get_id_ponto_analise(index)

            current_month_datetime = get_first_day_of_current_month()

            id_amostra = db.get_id_amostra(
                id_ponto_analise, current_month_datetime, row["Data e Hora da Coleta"]
            )

            analisys_data = create_analisys_data(db, row)

            if id_ponto_analise and verify_analisys_data(analisys_data):
                if id_amostra:
                    db.put_dados_analise(id_amostra, analisys_data)
                else:
                    new_id_amostra = db.post_amostra(
                        id_ponto_analise,
                        current_month_datetime,
                        row["Data e Hora da Coleta"],
                    )
                    db.post_dados_analise(new_id_amostra, analisys_data)
        return "Dados inseridos/atualizados com sucesso."
    except Exception as e:
        return f"Ocorreu algum erro ao tentar atualizar as informações: {e}."


def get_first_day_of_current_month():
    now = datetime.now()
    first_day = datetime(now.year, now.month, 1)
    return first_day.strftime("%Y-%m-%d 00:00:00.000")


def verify_analisys_data(analisys_data):
    for i, values in enumerate(analisys_data):
        if not all(values):
            return False
    return True


def create_analisys_data(db, row):
    id_parametro_cloro = db.get_id_parametro("Cloro Residual")
    id_parametro_coli_totais = db.get_id_parametro("Coliformes Totais")
    id_parametro_cor = db.get_id_parametro("Cor Aparente")
    id_parametro_e_coli = db.get_id_parametro("Escherichia Coli")
    id_parametro_turbidez = db.get_id_parametro("Turbidez")

    analisys_data = [
        (id_parametro_cloro, row["Cloro"]),
        (id_parametro_coli_totais, row["Coliformes Totais"]),
        (id_parametro_cor, row["Cor"]),
        (id_parametro_e_coli, row["E Coli"]),
        (id_parametro_turbidez, row["Turbidez"]),
    ]

    return analisys_data
