import pandas as pd


def new_header(dataframe, file):
    try:
        header_row = None
        for index, row in dataframe.iterrows():
            if row.astype(str).str.contains("Endereço", na=False).any():
                header_row = index
                break

        if header_row is not None:
            df = pd.read_excel(file, header=header_row)
            return df
    except Exception as e:
        return f"Erro ao concatenar as colunas: {str(e)}"
