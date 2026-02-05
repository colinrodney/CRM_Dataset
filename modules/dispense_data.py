import os
import pandas as pd

def dispense_data(df_2, filename):
    try:
        # 1. Get the directory where THIS script is located
        script_dir = os.path.dirname(os.path.abspath(__file__))
        print("SCRIPT_DIRECTORY: " '\n', script_dir)
        
        # 2. Join it with your desired output path
        output_folder = os.path.join(script_dir, "data", "cleaned_data")
        print("OUTPUT_DIRECTORY: " '\n', output_folder)

        # 3. Create the folder (now with a guaranteed absolute path)
        os.makedirs(output_folder, exist_ok=True)

        # 4. Define the full output file path
        output_path = os.path.join(output_folder, f"cleaned_{filename}")
        
        # 5. Write the file
        df_2.to_csv(output_path, index=False)
        
        print(f"SUCCESS: File written to:\n{output_path}")

    except Exception as e:
        print(f"ERROR: An issue occurred during data dispensation: {e}")

# Note: Ensure you are passing a string for filename and a DataFrame for df_2



# *** DO NOT DELETE! ***
# def dispense_data(df_2, filename):
#         try:
#             # import pandas as pd
#             # print("Pandas imported successfully!")

#             import os
#             print("os module imported successfully")

#         except:
#             #  print("EXCEPTION - Pandas import not successfull.")
#              print("EXCEPTION -os module import not successfull.")
#         else:
#             # DEFINE INPUT / OUPUT DIRECTORIES
#             # input_folder = r"data/raw_data" 
#             output_folder = r"data/cleaned_data"

#             # Create output folder if it doesn't exist
#             os.makedirs(output_folder, exist_ok=True)

#             # PROCESS EACH CSV IN FOLDER

#         # for filename in os.listdir(input_folder):
#         #     print("FILENAME:'\n'",filename)
#         #     if filename.endswith(".csv"):
#         #         file_path = os.path.join(input_folder, filename)
#         #         print("FILEPATH: " '\n', file_path)

#         #     # df = pd.read_csv("test_directory/dirty_cafe_sales-csv.csv")
#         #     # df = pd.read_csv(r"data/raw_data/messy_crm_dataset_before_cleansing.csv")
#         #     df = pd.read_csv(file_path)
#         #     df_2 = df.copy()
#         #     df_2.info()
#         #     print("ingest data function ran successfully! RETURNING file to function!")

#             output_path = os.path.join(output_folder, f"cleaned_{filename}")
#             print("OUTPUT_PATH: " '\n', output_path)
#             df_2.to_csv(output_path, index=False)

#             return df_2
