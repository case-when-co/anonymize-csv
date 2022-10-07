#!/usr/bin/env python3

"""
Anonymize CSV

Reads an input CSV file, anonymizes any specified fields with an MD5 hash, and
copies the result to your clipboard. Can optionally write the result to an
output CSV file as well.

Author: Austin Levine
"""

import pandas as pd
import argparse
import hashlib


def parse_arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument('infile', nargs=1)
	parser.add_argument(
		'--anonymize-fields',
		dest='anonymize_fields',
		nargs='+')
	parser.add_argument(
		'--header-lines',
		dest='header_lines',
		nargs='?',
		default='1')
	parser.add_argument(
		'--outfile',
		dest='outfile',
		nargs='?',
		default=None)

	return parser.parse_args()


def hash_field(df, field_name):
	return [hashlib.md5(val.encode('utf-8')).hexdigest()
			for val in df[field_name]]


if __name__ == '__main__':

	parsed_args = parse_arguments()

	# Read the infile CSV
	df = pd.read_csv(parsed_args.infile[0])
	fields_to_anonymize = parsed_args.anonymize_fields or []

	# Anonymize all selected fields
	if len(fields_to_anonymize) > 0:
		for field_name in fields_to_anonymize:
			df[field_name] = hash_field(df, field_name)

	# Write the hashed output to the outfile CSV if desired
	if parsed_args.outfile:
		df.to_csv(parsed_args.outfile, index=False)

	# Copy the hashed output to the clipboard as CSV
	df.to_clipboard(sep=',', index=False)
