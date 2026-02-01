
# Import test_directory package
import modules


import modules.ingest_data
import modules.schema_validate
import modules.duplicates
import modules.email_validate
import modules.fill_missing_values

# Invoke functions
# modules.module1.func1()
df_2 = modules.ingest_data.ingest_data()
modules.schema_validate.validate_schema(df_2)
df_2 = modules.duplicates.show_duplicates(df_2)
# df_2 = modules.duplicates.drop_duplicates()
df_2 = modules.email_validate.email_formatted_properly(df_2)
df_2 = modules.fill_missing_values.fill_missing_values(df_2)

print(df_2)

