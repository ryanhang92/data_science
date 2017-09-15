import numpy as np
import requests
import csv
from StringIO import StringIO
from urllib import urlopen
from zipfile import ZipFile

#Read from the web
zip_url = "http://seanlahman.com/files/database/lahman-csv_2014-02-14.zip"

#Wtih url library
url = urlopen(zip_url)
zipfile = ZipFile(StringIO(url.read()))
#with zipfile.ZipFile('archive.zip') as z:
with zipfile as z:
    for filename in z.namelist():
        print filename
        if filename == "Salaries.csv":
            with z.open(filename) as f:
                for line in f:
                    print line

#With Requests Library
r = requests.get(zip_url)
f = StringIO()
f.write(r.content)
def extract_zip(input_zip):
    zipped_file = ZipFile(input_zip)
    for filename in zipped_file.namelist():
        if filename == "Salaries.csv":
            with zipped_file.open(filename) as f:
                for line in f:
                    print line
    #return {i: input_zip.read(i) for i in input_zip.namelist()}
extracted = extract_zip(f)


#Read file from path
salary_path = 'data/Salaries.csv'
with open(salary_path, 'rb') as csvfile:
    salary_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in salary_reader:
        print row

teams_path = 'data/Teams.csv'
with open(teams_path, 'rb') as csvfile:
    teams_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in teams_reader:
        print row

#Process the data once in the right data structure











