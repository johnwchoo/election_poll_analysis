import csv
import os

csvpath = os.path.join('Resources','election_data.csv')

with open(csvpath, newline = '') as csvfile:
	csvreader = csv.reader(csvfile, delimiter = ',')

	print(csvreader)

	csv_header = next(csvreader)
	print(f"CSV Header: {csv_header}")

	voter_count = 0
	Khan = 0
	Correy = 0
	Li = 0
	OTooley = 0

	for row in csvreader:
		voter_count += 1
		if row[2] == "Khan":
			Khan += 1

		elif row[2] == "Correy":
			Correy += 1

		elif row[2] == "Li":
			Li += 1

		else:
			OTooley += 1
print(" ")
print("Election Results")
print("-------------------------")	
print(f"Total Votes: {voter_count}")
print("-------------------------")	
print(f"Khan: {round(Khan*100/voter_count, 4)}% ({Khan})")
print(f"Correy: {round(Correy*100/voter_count, 4)}% ({Correy}")
print(f"Li: {round(Li*100/voter_count, 4)}% ({Li})")
print(f"O'Tooley: {round(OTooley*100/voter_count, 4)}% ({OTooley})")
print("-------------------------")	
# ^ I have to round these numbers

if int(Khan) > int(Correy):
	if int(Khan) > int(Li):
		if int(Khan) > int(OTooley):
			print("Winner: Khan")

# ^ Khan wins


if int(Correy) > int(Khan):
	if int(Correy) > int(Li):
		if int(Correy) > int(OTooley):
			print("Winner: Correy")

# ^ Correy wins

if int(Li) > int(Khan):
	if int(Li) > int(Correy):
		if int(Li) > int(OTooley):
			print("Winner: Li")

# ^ Li wins

if int(OTooley) > int(Khan):
	if int(OTooley) > int(Correy):
		if int(OTooley) > int(Li):
			print("Winner: OTooley")

# ^ OTooley wins
print("-------------------------")	







# Second quesiton: print(f"{percentage(total_votes)}, (total_votes)")

