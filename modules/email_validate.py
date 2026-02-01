# EMAIL VALIDATION MODULE

def email_formatted_properly(df_2):

    # Regex pattern to validate email properly formatted (DOES NOT DETERMINE ACTIVE/INACTIVE STATE OF EMAIL ADDY)
    email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    # Write results to new column named "EMAIL_VALID"
    df_2["EMAIL_VALID"] = df_2["email"].str.match(email_pattern, na=False)

    return df_2