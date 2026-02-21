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

                
        # 2. Check that first digit of phone number is NOT ZERO (Valid Country Codes do NOT start with 0)
        # tilde (~ bitwise NOT operator in Python) - used to negate a condition. Returns True for valid phone numbers / False for invalid numbers
        # df_2['phone_number_starts_with_0'] = ~df_2['phone_number'].astype(str).str.startswith('0') # True = INVALID / False = VALID

        # df_2['phone_number_starts_with_0'] = lambda phone_num: True if phone_num.astype(str).str.startswith('0') else False

        if df_2["phone_number"].str.startswith("0").any():
            df_2["phone_number"] = df_2["phone_number"].str.replace("0", "", regex=False) #replace 0 w/ nothing
            df_2["phone_number"].str.strip() # strip whitespace (all sides)
            # # flag number as starting w/ 0
            # df_2['phone_number_starts_with_0'] = df_2["phone_number"].astype(str).str.startswith('0')
        # elif ~df_2["phone_number"].str.startswith("1").any():
        #     # 2. Clean: Collapse leading 1s (Captures numbers such as 11056744898 and converts them to 1056744898)
        #     # df_2['phone_number'] = df_2['phone_number'].astype(str).str.replace(r'^1+', '1', regex=True)
        #     df_2['phone_number'] = df_2['phone_number'].astype(str).str.replace(search_pattern, replacement_plusOne, regex=True)

        # Number string starts with 1, but does not have + in front of it - add ONLY a + to beginning of number
        elif df_2["phone_number"].str.startswith("1").any():
            search_pattern = r"(\d+)"
            # replacement_plusOne = r"+1\1"

            # back reference capturing number group and adding ONLY a + in front of number string already starting with 1
            replacement_add_Only_Plus = r"+\1"
            # replacement_One = r"+\1" 
            df_2['phone_number'] = df_2['phone_number'].astype(str).str.replace(search_pattern, replacement_add_Only_Plus, regex=True)
        # Number string starts with any number other than 1 or 0 (all other conditions) - DO SAME CODE AS IN ELIF BLOCK!
        else:
            search_pattern = r"(\d+)"
            # replacement_plusOne = r"+1\1"

            # back reference capturing number group and adding ONLY a + in front of number string already starting with 1
            replacement_add_Only_Plus = r"+\1"
            # replacement_One = r"+\1" 
            df_2['phone_number'] = df_2['phone_number'].astype(str).str.replace(search_pattern, replacement_add_Only_Plus, regex=True)

    #  # df_2["phone_number"] = df_2["phone_number"].astype(str).str.replace(r'[\D]', '', regex=True) DO NOT DELETE!

    #     #3 Check length of phone numbers (Valid phone numbers should be between 10 and 15 digits long, depending on country code)
    #     df_2['phone_number_length'] = df_2["phone_number"].astype(str).str.len() # expect numeric result 

    #     # 3. Add +1 using back-references (\1\2\3) for numbers that do not already start with 1 (to avoid adding +1 to numbers that already have it)
    #     # We look for 10 digits and wrap them in groups
    #     # search_pattern = r"(\d{3})(\d{3})(\d{4})"
        
            

    #     # df_2["phone_number"] = df_2["phone_number"].str.replace(search_pattern, replacement, regex=True)

    return df_2


# BEGIN WORKING WIITH GOOGLE PHONENUMBER LIBRARY FOR E164 CONVERSIONS ETC.
def parse_phone_numbers(df_2):
    try:
        # Parse the string (assuming international format with '+')
        parsed_num = phonenumbers.parse(df_2['phone_number'], None)
        
        # Extract the Country Code (it returns an integer, e.g., 1 or 44)
        cc = str(parsed_num.country_code)
        
        # The Core Test: Does it start with '0'?
        if cc.startswith('0'):
            df_2['is_valid_cc'] = df_2['phone_number'].apply(parse_phone_numbers) #False / No
            # return False
        df_2['is_valid_cc'] = df_2['phone_number'].apply(parse_phone_numbers) #True / Yes
    except:
        # If the number can't even be parsed, it's definitely not valid
        # df_2['cannot_parse'] = df_2['phone_number'].apply(parse_phone_numbers) #False / No
        return False
    return df_2



# def parse_phone_numbers(df_2): DO NOT DELETE
#     import phonenumbers
#     import pandas as pd

#     # Ensure the column exists and convert to string to avoid 'NoneType' errors
#     if "phone_number" in df_2.columns:
#         # Parse phone numbers using phonenumbers library - expect boolean value returned
#         df_2["parsed_phone_number"] = df_2["phone_number"].apply(lambda x: phonenumbers.parse(x, None) if pd.notnull(x) else None)

#         # Validate parsed phone numbers - expect boolean value returned
#         df_2["is_valid_phone_number"] = df_2["parsed_phone_number"].apply(lambda x: phonenumbers.is_valid_number(x) if x is not None else False)

#         # Format parsed phone numbers in E164 format
#         df_2["E164_formatted_phone_number"] = df_2["parsed_phone_number"].apply(lambda x: phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.E164) if x is not None else None)

#         # Possible Phone Number
#         df_2["possible_phone_number"] = df_2["parsed_phone_number"].apply(lambda x: phonenumbers.is_possible_number(x))

#     return df_2