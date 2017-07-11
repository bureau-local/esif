import csv, glob

csvfiles = glob.glob("*.csv")

outputfile = open("fts_1315_uk.csv", "wb")
csv_writer = csv.writer(outputfile)

for file_index, filename in enumerate(csvfiles):
	inputfile = open(filename, "rU")
	csv_reader = csv.reader(inputfile)

	for row_index, row in enumerate(csv_reader):
		# this will print the header
		if row_index == 0 and file_index == 0:
			csv_writer.writerow(row)
		if row[8] == "United Kingdom":
			csv_writer.writerow(row)
