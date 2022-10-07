# Anonymize CSV

Reads an input CSV file, anonymizes any specified fields with an MD5 hash, and copies the result to your clipboard. Can optionally write the result to an output CSV file as well.


#### Example uses:
```
python run.py ~/my_data.csv --anonymize-fields full_name email_address
```

```
python run.py ~/my_data.csv --anonymize-fields full_name email_address --outfile ~/my_data_anonymized.csv
```
