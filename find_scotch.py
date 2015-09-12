# Alison Y. Chang | ayc2135 | Databases HW0

csv_file = open('iowa-liquor-sample.csv')

counter = 0
for line in csv_file:
	if 'single malt scotch' in line.lower():
		counter += 1
print counter

csv_file.close()

