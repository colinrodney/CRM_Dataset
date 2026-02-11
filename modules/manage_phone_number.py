# STANDARDIZE PHONE NUMBERS
def standardize_phone_numbers(df_2):

    # IMPORT REGEX MODULE
    import re
    phone_number_pattern = re.compile(r"[\+\s\(\)-.]")

    #Show data type of phone number column
    df_2.info()

    # REMOVE ALL NON-DIGIT CHARS FROM PHONE NUMBERS
    # Overwrite the original phone number column with the cleaned version
    # df_2["columnName"] = df_2["columnName"].apply(lambda x: re.sub(r'[(),\s\.\-]', '', x))
    df_2["phone_number"] = df_2["phone_number"].apply(lambda x: re.sub(r'[(),\s\.\-]', '', x))


    # # REMOVE +1 FROM BEGINNING OF PHONE NUMBERS
    # plus_one = r"^\+\d"
    # plus_one_formatted = ""
    # # df_2["phone_number"] = df_2["phone_number"].apply(lambda x: re.sub(plus_one, plus_one_formatted, x))
    # df_2["office_phone"] = df_2["office_phone"].apply(lambda x: re.sub(plus_one, plus_one_formatted, x))
    # df_2["mobile_phone"] = df_2["mobile_phone"].apply(lambda x: re.sub(plus_one, plus_one_formatted, x))

    # Add +1 TO BEGINNING OF PHONE NUMBERS
    number_pattern = r"(\d{3})(\d{3})(\d{4})"
    plus_one_prefix = "+1"
    formatted_number = plus_one_prefix + number_pattern
    # df_2["columnName"] = df_2["columnName"].apply(lambda x: re.sub(number_pattern, formatted_number, x))
    df_2["phone_number"] = df_2["phone_number"].apply(lambda x: re.sub(number_pattern, formatted_number, x))


    #Format numbers E164 Format
    # # INSERT HYPHENS INTO PHONE NUMBERS USING BACK REFERENCES IN FORMATTED / REPLACEMENT PATTERN
    # search_pattern = r"(\d{3})(\d{3})(\d{4})"
    # formatted_pattern = r"\1-\2-\3"
    # # df_2["phone_number"] = df_2["phone_number"].apply(lambda x: re.sub(search_pattern, formatted_pattern, x))
    # df_2["office_phone"] = df_2["office_phone"].apply(lambda x: re.sub(search_pattern, formatted_pattern, x))
    # df_2["mobile_phone"] = df_2["mobile_phone"].apply(lambda x: re.sub(search_pattern, formatted_pattern, x))

    return df_2