def concatenate_columns(df):
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
        return f"Erro ao concatenar as colunas: {str(e)}"
