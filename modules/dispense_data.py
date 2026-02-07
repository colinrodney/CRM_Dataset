def dispense_data(df_2, filename):
    import os
        
    # output_folder = r"C:\Users\Cessn\OneDrive\Desktop\data_cleansing_automations\CRM_Dataset\data\cleaned_data\cleaned_messy_crm_dataset_after_cleansing.csv"
    output_folder = r"data/cleaned_data/cleaned_messy_crm_dataset_after_cleansing.csv"

    try:
        # Create output folder if it doesn't exist already
        if not os.path.exists(output_folder):
            os.makedirs(output_folder, exist_ok=True)
            print(f"Created new directory at: {output_folder}")

        # Construct full file path
        output_path = os.path.join(output_folder, f"cleaned_{filename}")
        print("OUTPUT_PATH: " '\n', output_path)

        # Write DataFrame to a CSV file in the output folder
        df_2.to_csv(output_folder, index=False)
        print(f"SUCCESS! File is now at: {output_path}")

        return df_2
    
    except Exception as e:
        print(f"FAILED to write file. Error: {e}")
