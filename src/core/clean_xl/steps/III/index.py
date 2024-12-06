def required_columns(df):
    try:
        columns_required = [
            "Ponto",
            "Data e Hora da Coleta",
            "Cloro",
            "Turbidez",
            "Cor",
            "Coliformes Totais",
            "E Coli",
            "Responsável Técnico",
            "Data da Avaliação e Liberação",
        ]
        return df[columns_required]
    except Exception as e:
        return f"Erro ao extrair as colunas desejadas (PASSO III): {str(e)}"
