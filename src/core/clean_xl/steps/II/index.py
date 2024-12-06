import pandas as pd


def concatenate_columns(df):
    try:
        new_df = first_concatenate(df)
        new_df = second_concatenate(df)
        return new_df
    except Exception as e:
        return f"Erro ao concatenar as colunas (PASSO II): {str(e)}"


def first_concatenate(df):
    try:
        unnamed_columns = [col for col in df.columns if "Unnamed" in col]

        for col in unnamed_columns:
            prev_col = df.columns[df.columns.get_loc(col) - 1]

            df[prev_col] = df[prev_col].fillna("")
            df[col] = df[col].fillna("")

            df[prev_col] = df[prev_col].astype(str) + df[col].astype(str)

            df[prev_col] = df[prev_col].replace("nannan", "")

            df.drop(columns=[col], inplace=True)

        return df

    except Exception as e:
        return f"Erro ao concatenar as colunas com sinal de '>' (PASSO II): {str(e)}"


def second_concatenate(df):
    try:
        df["Data da coleta"] = pd.to_datetime(df["Data da coleta"])

        df["Hora"] = df["Hora"].astype(str)

        df["Data e Hora da Coleta"] = pd.to_datetime(
            df["Data da coleta"].dt.strftime("%Y-%m-%d") + " " + df["Hora"]
        )
        return df
    except Exception as e:
        return (
            f"Erro ao concatenar a coluna de data e hora da coleta (PASSO II): {str(e)}"
        )
