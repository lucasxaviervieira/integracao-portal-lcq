import pyodbc


class PainelBordoDB:

    def __init__(self, db_server, db_name, db_username, db_password):
        self.conn_str = (
            "Driver={SQL Server};"
            f"Server={db_server};"
            f"Database={db_name};"
            f"UID={db_username};"
            f"PWD={db_password};"
        )

    def get_id_amostra(self, id_ponto_analise, dt_analise, dt_coleta):
        try:
            query = """
                SELECT id_amostra
                FROM LAB_Amostra
                WHERE id_ponto_analise = ?
                    AND dt_analise = ?
                    AND dt_coleta = ?
            """
            with pyodbc.connect(self.conn_str) as conn:
                cursor = conn.cursor()
                cursor.execute(query, (id_ponto_analise, dt_analise, dt_coleta))
                result = cursor.fetchone()
                if result:
                    return result[0]
                else:
                    return None
        except Exception as e:
            return f"Error in get_id_amostra: {e}"

    def get_id_ponto_analise(self, nr_ponto):
        try:
            with pyodbc.connect(self.conn_str) as conn:
                cursor = conn.cursor()

                query = "SELECT id_ponto_analise FROM [dbo].[LAB_Ponto_Analise] WHERE nr_ponto = ?;"
                cursor.execute(query, (nr_ponto,))
                result = cursor.fetchone()
                if result:
                    return result[0]
                else:
                    return f"No id_ponto_analise found for nr_ponto '{nr_ponto}'."

        except Exception as e:
            return f"Error in get_id_ponto_analise: {e}"

    def get_id_parametro(self, nm_parametro):
        try:
            with pyodbc.connect(self.conn_str) as conn:
                cursor = conn.cursor()

                query = "SELECT id_parametro FROM [dbo].[LAB_Parametro_Analise] WHERE nm_parametro = ?;"
                cursor.execute(query, (nm_parametro,))
                result = cursor.fetchone()
                if result:
                    return result[0]
                else:
                    return f"No id_parametro found for nm_parametro '{nm_parametro}'."

        except Exception as e:
            return f"Error in get_id_parametro: {e}"

    def post_amostra(self, id_ponto_analise, dt_analise, dt_coleta):
        try:
            with pyodbc.connect(self.conn_str) as conn:
                cursor = conn.cursor()

                insert_query = """
                INSERT INTO [dbo].[LAB_Amostra] ([id_ponto_analise], [dt_analise], [dt_coleta], [fl_recoleta])
                OUTPUT INSERTED.id_amostra
                VALUES (?, ?, ?, ?);
                """
                cursor.execute(
                    insert_query, (id_ponto_analise, dt_analise, dt_coleta, "N")
                )
                id_amostra = cursor.fetchone()[0]
                return id_amostra

        except Exception as e:
            return f"Error in post_amostra: {e}"

    def post_dados_analise(self, id_amostra, dados_analise):
        try:
            with pyodbc.connect(self.conn_str) as conn:
                cursor = conn.cursor()

                insert_query = """
                INSERT INTO [dbo].[LAB_Dado_Analise] ([id_parametro], [vl_analise], [id_amostra])
                VALUES (?, ?, ?);
                """

                data_with_amostra = [
                    (item[0], item[1], id_amostra) for item in dados_analise
                ]

                cursor.executemany(insert_query, data_with_amostra)
                conn.commit()

        except Exception as e:
            print(f"Error in post_dados_analise: {e}")

    def put_dados_analise(self, id_amostra, dados_analise):
        try:
            query = """
                UPDATE LAB_Dado_Analise
                SET vl_analise = ?
                WHERE id_amostra = ? AND id_parametro = ?
            """
            with pyodbc.connect(self.conn_str) as conn:
                cursor = conn.cursor()

                for item in dados_analise:
                    id_parametro = item[0]
                    vl_analise = item[1]
                    cursor.execute(query, (vl_analise, id_amostra, id_parametro))

                conn.commit()
        except Exception as e:
            print(f"Error in put_dados_analise: {e}")
