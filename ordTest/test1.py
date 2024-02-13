multiline_input = 'hi>>'
translation_table_quotes = str.maketrans("‘’", "''")
translation_table_greater_than = str.maketrans(">", " ")
translation_table_combined = {}
translation_table_combined.update(translation_table_quotes)
translation_table_combined.update(translation_table_greater_than)

result = multiline_input.translate(translation_table_combined)

