import csv

# as an array of data in order

with open('nfl_teams.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        print(row)

# as an dictionary in order

with open('nfl_teams.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        print(row)

# appends information, adds a new line
# defines fieldnames for the fields to keep order
# returns information on a newline

with open('nfl_teams.csv', mode='a') as csv_file:
    fieldnames = ['id', 'team', 'wins', 'losses']
    nfl_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    nfl_writer.writerow({'id': 4,'team': 'Giants', 'wins': 6, 'losses': 4})
    nfl_writer.writerow({'id': 5,'team':'Lions','wins': 8,'losses': 2})