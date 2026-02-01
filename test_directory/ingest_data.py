def ingest_data():
        try:
            import pandas as pd
            print("Pandas imported successfully!")
        except:
             print("EXCEPTION - Pandas import not successfull.")
        else:
            df = pd.read_csv("test_directory/dirty_cafe_sales-csv.csv")
            df_2 = df.copy()
            df_2.info()
            print("ingest data function ran successfully! RETURNING file to function!")
            return df_2
