def clean_data(df):
    try:
        new_df = first_clean(df)
        new_df = second_clean(new_df)
        new_df = third_clean(new_df)
        new_df = fourth_clean(new_df)
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


def third_clean(df):
    try:
        df["Cloro"] = df["Cloro"].astype("string")
        df["Turbidez"] = df["Turbidez"].astype("string")
        df["Cor"] = df["Cor"].astype("string")
        df["Coliformes Totais"] = df["Coliformes Totais"].astype("string")
        df["E Coli"] = df["E Coli"].astype("string")
        return df
    except Exception as e:
        return f"Erro ao tratar os dados na terceira limpeza (PASSO IV): {str(e)}"


def fourth_clean(df):
    try:
        df["Ponto"] = df["Ponto"].str.rstrip("N")
        df = df.set_index("Ponto")
        return df
    except Exception as e:
        return f"Erro ao tratar os dados na quarta limpeza (PASSO IV): {str(e)}"
