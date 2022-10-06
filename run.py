#!/usr/bin/env python3

"""
Anonymize CSV

Reads an input CSV file, anonymizes any specified fields with an MD5 hash, and
writes the result to an output CSV file.

Author: Austin Levine
"""

import pandas as pd
import argparse
import hashlib


def parse_arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument('infile', nargs='?')
	parser.add_argument('outfile', nargs='?')
	parser.add_argument(
		'--anonymize-fields',
		dest='anonymize_fields',
		nargs='*')
	parser.add_argument(
		'--header-lines', 
		dest='header_lines',
		nargs='?',
		default='1')

	return parser.parse_args()


def hash_field(df, field_name):
	return [hashlib.md5(val.encode('utf-8')).hexdigest()
			for val in df[field_name]]


if __name__ == '__main__':

	parsed_args = parse_arguments()

	# Read the infile CSV
	df = pd.read_csv(parsed_args.infile)
	fields_to_anonymize = parsed_args.anonymize_fields or []

	# Anonymize all selected fields
	if len(fields_to_anonymize) > 0:
		for field_name in fields_to_anonymize:
			df[field_name] = hash_field(df, field_name)

	# Write the hashed output to the outfile CSV
	df.to_csv(parsed_args.outfile, index=False)
