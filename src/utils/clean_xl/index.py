from utils.clean_xl.steps import *


def clean_excel(df, uploaded_file):
    try:
        # CLEAN EXCEL
        ## STEP I
        new_df = new_header(df, uploaded_file)

        ## STEP II
        new_df = concatenate_columns(new_df)

        ## STEP III
        new_df = required_columns(new_df)

        ## STEP IV
        new_df = clean_data(new_df)

        return new_df

    except Exception as e:
        return f"Erro ao limpar o arquivo: {str(e)}"
