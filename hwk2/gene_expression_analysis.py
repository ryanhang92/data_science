import numpy as np
import requests
import csv

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


expr_path = 'data/exprs_GSE5859.csv'
with open(expr_path, 'rb') as csvfile:
    expr_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in expr_reader:
        print row


sample_path = 'data/sampleinfo_GSE5859.csv''
with open(sample_path, 'rb') as csvfile:
    sample_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in sample_path:
        print row


t


