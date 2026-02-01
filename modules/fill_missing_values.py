# FILL BLANKS/ NULLS (This function may be used multiple times on a dataset - may need to be decoupled from original)
def fill_missing_values(df_2):
    try:
        import numpy as np       
    except:
        print("EXCEPTION - numpy import not successfull.")
    else:
        df_2 = df_2.replace("nan", np.nan)
        df_2.fillna("unknown")
        # df_2["phone_number"] = df_2["phone_number"].replace("nan", np.nan)
        # df_2["mobile_phone"] = df_2["mobile_phone"].fillna("NONE")
        # df_2["office_phone"] = df_2["office_phone"].fillna("NONE")
        # df_2["sales_ytd"] = df_2["sales_ytd"].fillna(0)


        # # All other empty fields filled w/ np.nan
        # # df_2 = df_2.fillna("NONE_NEW")
        # df_2 = df_2.fillna(np.nan)
        print("fill_missing_values function ran successfully! RETURNING file to function!")
        df_2.info()
        # print(df_2)
        return df_2