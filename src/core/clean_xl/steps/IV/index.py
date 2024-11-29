def clean_data(df):
    try:
        new_df = first_clean(df)
        new_df = second_clean(new_df)
        return new_df
    except Exception as e:
        return f"Erro ao tratar os dados: {str(e)}"


def first_clean(df):
    try:
        df["Ponto"] = df["Ponto"].astype("string")
        df = df[df.apply(lambda x: len(x["Ponto"]) == 4, axis=1)]
        return df
    except Exception as e:
        return f"Erro ao tratar os dados na primeira limpeza (PASSO IV): {str(e)}"


def second_clean(df):
    try:
        df = df[df["Data da Avaliação e Liberação"].notna()]
        return df
    except Exception as e:
        return f"Erro ao tratar os dados na segunda limpeza (PASSO IV): {str(e)}"