def validate_schema(df_2):
    #  Set theory (Python sets) used to compare columns we need (required columns)
    #   against column names actually found in the dataset (df_test.columns)

    #     '''
    #     Using a set {} instead of a list [] is intentional. 
    #     Sets are optimized for mathematical comparisons (like finding differences/ subtraction), 
    #     which is what happens at the variabl named "missing"
        
    #     The syntax missing = required_columns - set(df_test.columns) is literally
    #     looking at the names of coulmns in dataset and subtracting / removing each located value from
    #     the missing variable.

    #     The penultimate goal of the "missing" variable is to be EMPTY (NO VALUES) which results in a 
    #     "Falsy" (False) result in Python which means that every column name that was expected as
    #     predicated in "required_columns" variable was MATCHED on the inbound dataset and removed (subtracted) from
    #     variable "required_columns" leaving no values in that variable. (AFTER OPERATION ASK YOURSELF IF THERE ARE ANY VALUES
    #     IN THE "MISSING" VARIABLE - IF NO (False) > PROCEED WITH CODE / IF YES (True) > RAISE AN ERROR!

        required_columns = {
        "transaction_id",
        "item",
        "quantity",
        "price_per_unit",
        "total_spent",
        "payment_method",
        "location",
        "transaction_date"} # set containing exact column names needed for code to work

        # Subtract/ remove all names found in dataset from missing variable
        missing = required_columns - set(df_2.columns.str.lower()) 

        # If missing is True (there are values remaining after subtraction operation)
        if missing:
            raise ValueError(f"Missing columns: {missing}")
        else:
            print("All values found in DataFrame!")
        return df_2