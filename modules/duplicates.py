# Drop Duplicates (DUPLICATES SHOULD BE DROPPED ONLY AFTER SPEAKING W/ CLIENT AND BASED ON SUBSET!)

# DROP DUPLICATES (Can be dropped on dataframe or series!)
# API: https://pandas.pydata.org/docs/reference/api/pandas.Series.drop_duplicates.html#pandas.Series.drop_duplicates
def drop_duplicates(df_2):
    try:
        df_2.drop_duplicates(subset=["email"], keep="first", inplace=True)
    except:
        print("An error ocurred in duplicates.drop_duplicates() function")
    return df_2

# SHOW DUPLICATES: DataFrame.duplicated(subset=None, keep='first')
# API guidance: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.duplicated.html
def show_duplicates(df_2):
    try:
        df_2["IS_DUPLICATE"]=df_2.duplicates(subset=["email"], keep="first", inplace=True)
    except:
        print("An error ocurred in duplicates.show_duplicates() function")
    return df_2