
# Import test_directory package
import modules

# Import modules
# import modules.module1
import modules.fill_missing_values
import modules.ingest_data

# Invoke functions
# modules.module1.func1()
df_2 = modules.ingest_data.ingest_data()
modules.fill_missing_values.fill_missing_values(df_2)

