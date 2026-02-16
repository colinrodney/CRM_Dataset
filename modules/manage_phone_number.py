# # STANDARDIZE PHONE NUMBERS
# def standardize_phone_numbers(df_2):

# DO NOT DELETE!
#     # IMPORT REGEX MODULE
#     import re
#     phone_number_pattern = re.compile(r"[\+\s\(\)-.]")

#     #Show data type of phone number column
#     df_2.info()

#     # REMOVE ALL NON-DIGIT CHARS FROM PHONE NUMBERS
#     # Overwrite the original phone number column with the cleaned version
#     # df_2["columnName"] = df_2["columnName"].apply(lambda x: re.sub(r'[(),\s\.\-]', '', x))
#     df_2["phone_number"] = df_2["phone_number"].apply(lambda x: re.sub(r'[(),\s\.\-]', '',x))


#     # # REMOVE +1 FROM BEGINNING OF PHONE NUMBERS
#     # plus_one = r"^\+\d"
#     # plus_one_formatted = ""
#     # # df_2["phone_number"] = df_2["phone_number"].apply(lambda x: re.sub(plus_one, plus_one_formatted, x))
#     # df_2["office_phone"] = df_2["office_phone"].apply(lambda x: re.sub(plus_one, plus_one_formatted, x))
#     # df_2["mobile_phone"] = df_2["mobile_phone"].apply(lambda x: re.sub(plus_one, plus_one_formatted, x))

#     # Add +1 TO BEGINNING OF PHONE NUMBERS
#     number_pattern = r"(\d{3})(\d{3})(\d{4})"
#     plus_one_prefix = "+1"
#     formatted_number = plus_one_prefix + number_pattern
#     # df_2["columnName"] = df_2["columnName"].apply(lambda x: re.sub(number_pattern, formatted_number, x))
#     df_2["phone_number"] = df_2["phone_number"].apply(lambda x: re.sub(number_pattern, formatted_number, x))


#     #Format numbers E164 Format
#     # # INSERT HYPHENS INTO PHONE NUMBERS USING BACK REFERENCES IN FORMATTED / REPLACEMENT PATTERN
#     # search_pattern = r"(\d{3})(\d{3})(\d{4})"
#     # formatted_pattern = r"\1-\2-\3"
#     # # df_2["phone_number"] = df_2["phone_number"].apply(lambda x: re.sub(search_pattern, formatted_pattern, x))
#     # df_2["office_phone"] = df_2["office_phone"].apply(lambda x: re.sub(search_pattern, formatted_pattern, x))
#     # df_2["mobile_phone"] = df_2["mobile_phone"].apply(lambda x: re.sub(search_pattern, formatted_pattern, x))

#     return df_2

def standardize_phone_numbers(df_2):
    import re
    
    # Ensure the column exists and convert to string to avoid 'NoneType' errors
    if "phone_number" in df_2.columns:
        # 1. Strip all non-digit characters
        df_2["phone_number"] = df_2["phone_number"].astype(str).str.replace(r'[(),\s\.\-,\+]', '', regex=True)

                
        # # Check that first 2 digits of phone number are not 10 which indicates an invalid country code
        # # NOTE tilde (~ bitwise negative operator in Python) is used to negate the condition, so it returns True for valid phone numbers and False for invalid ones
        # df_2['is_valid_phone_number'] = ~df_2['phone_number'].astype(str).str.startswith('10')

        # df_2["phone_number"] = df_2["phone_number"].astype(str).str.replace(r'[\D]', '', regex=True) DO NOT DELETE!

        # 3. Add +1 using back-references (\1\2\3) for numbers that do not already start with 1 (to avoid adding +1 to numbers that already have it)
        # We look for 10 digits and wrap them in groups
        if df_2["phone_number"].str.startswith("1").all():
            search_pattern = r"(\d{3})(\d{3})(\d{4})"
            replacement = r"+1\1\2\3"
        # else:
        #     # 2. Clean: Collapse leading 1s (Captures numbers such as 11056744898 and converts them to 1056744898)
        #     df_2['phone_number'] = df_2['phone_number'].astype(str).str.replace(r'^1+', '1', regex=True)
            

    df_2["phone_number"] = df_2["phone_number"].str.replace(search_pattern, replacement, regex=True)

    return df_2