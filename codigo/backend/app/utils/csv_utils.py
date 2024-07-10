import pandas as pd

def validate_csv(df):
    expected_columns = ["INDICE", "LATITUDE", "LONGITUDE", "CODIGO_ROTA", "SEQUENCIA", "LOGRADOURO", "NUMERO"]
    return list(df.columns) == expected_columns
