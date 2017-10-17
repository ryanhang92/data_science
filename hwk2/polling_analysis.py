import csv

poll_path = 'data/election.csv'
with open(poll_path, 'rb') as csvfile:
    poll_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for i, row in enumerate(poll_reader):
        if i == 0:
            print row, i


