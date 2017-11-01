import numpy as np
import requests
import csv
from collections import defaultdict

'''
expr_url = 'https://raw.githubusercontent.com/cs109/2014_data/master/exprs_GSE5859.csv'
sample_url = 'https://raw.githubusercontent.com/cs109/2014_data/master/sampleinfo_GSE5859.csv'

r = requests.get(expr_url)
reader = csv.reader(r.iter_lines(), delimiter=',', quotechar='"')
for i, row in enumerate(reader):
    if i == 0:
        print row

r = requests.get(sample_url)
reader = csv.reader(r.iter_lines(), delimiter=',', quotechar='"')
for i, row in enumerate(reader):
    if i == 0:
        print row
'''

# Problem 1

# read this into a pandas dataframe, read the column data indexed by header
# parse this into a dict of arrays first

expr_key_map = defaultdict()
sample_key_map = defaultdict()

expr_data = defaultdict(list)
sample_data = defaultdict(list)

expr_path = 'data/exprs_GSE5859.csv'
with open(expr_path, 'rb') as csvfile:
    expr_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for i, row in enumerate(expr_reader):
        for j in range(len(row)):
            if i == 0:
                expr_key_map[j] = row[j]
            else:
                column_index = expr_key_map[j]
                data_point = row[j]
                expr_data[column_index].append(data_point)

sample_path = 'data/sampleinfo_GSE5859.csv'
with open(sample_path, 'rb') as csvfile:
    sample_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for i, row in enumerate(sample_reader):
        for j in range(len(row)):
            if i == 0:
                sample_key_map[j] = row[j]
            else:
                column_index = expr_key_map[j]
                data_point = row[j]
                sample_data[column_index].append(data_point)


# create a dataframe (matrix) where the columns in the gene expression data frame match the order of the file names sample annotation data frame



# create a list of year and month as integers from the sample info table, cast into datetime obj?




# create new data frame, where the date columns are now dates since Oct 3rd, 2002




# 1(d) exploratory analysis and SVD, if date of processing has large efffect on variability in the data
    # Graph relationship/correlation, correlation, SVD, calculate entropy





