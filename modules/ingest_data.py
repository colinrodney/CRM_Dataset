# DO NOT DELETE
# def ingest_data():
#         try:
#             import pandas as pd
#             print("Pandas imported successfully!")
#         except:
#              print("EXCEPTION - Pandas import not successfull.")
#         else:
#             # df = pd.read_csv("test_directory/dirty_cafe_sales-csv.csv")
#             df = pd.read_csv(r"data/raw_data/messy_crm_dataset_before_cleansing.csv")
#             df_2 = df.copy()
#             df_2.info()
#             print("ingest data function ran successfully! RETURNING file to function!")
#             return df_2

def ingest_data():
        try:
            import pandas as pd
            print("Pandas imported successfully!")

        except:
             print("EXCEPTION - Pandas import not successfull.")
        else:
            # DEFINE INPUT / OUPUT DIRECTORIES
            input_folder = "raw_data"
            output_folder = "cleaned_data"

            # Create output folder if it doesn't exist
            os.makedirs(output_folder, exist_ok=True)
            
            # df = pd.read_csv("test_directory/dirty_cafe_sales-csv.csv")
            df = pd.read_csv(r"data/raw_data/messy_crm_dataset_before_cleansing.csv")
            df_2 = df.copy()
            df_2.info()
            print("ingest data function ran successfully! RETURNING file to function!")
            return df_2
