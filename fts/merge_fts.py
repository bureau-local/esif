import csv, glob

csvfiles = glob.glob("*.csv")

outputfile = open("fts1315.csv", "wb")
csv_writer = csv.writer(outputfile)

print csvfiles

for file_index, filename in enumerate(csvfiles):
	inputfile = open(filename, "rU")
	csv_reader = csv.reader(inputfile)

	print file_index

	for row_index, row in enumerate(csv_reader):
		# this will make sure headers only get writed ounce
		if row_index == 0 and file_index != 0:
			continue
		csv_writer.writerow(row)
