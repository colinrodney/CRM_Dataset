# Drop Duplicates (DUPLICATES SHOULD BE DROPPED ONLY AFTER SPEAKING W/ CLIENT AND BASED ON SUBSET!)
def drop_duplicates(df_2):
    try:
        df_2.drop_duplicates(subset=["email"], keep="first", inplace=True)
    except:
        print("An error ocurred in drop_duplicates module")