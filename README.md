# Anonymize CSV

Reads an input CSV file, anonymizes one or more specified fields with an MD5 hash, and writes the result to an output CSV file.


#### Example:
```bash
python run.py ~/my_data.csv ~/my_data_anonymized.csv --anonymize-fields full_name email_address
```
