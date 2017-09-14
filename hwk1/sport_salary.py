import numpy as np
import requests
import csv
from StringIO import StringIO
from urllib import urlopen
from zipfile import ZipFile

#Read from the web
zip_url = "http://seanlahman.com/files/database/lahman-csv_2014-02-14.zip"

url = urlopen(zip_url)
zipfile = ZipFile(StringIO(url.read()))

#with zipfile.ZipFile('archive.zip') as z:
with zipfile as z:
    for filename in z.namelist():
        with z.open(filename) as f:
            for line in f:
                print line

'''
url = urlopen(zip_url)
zipfile = ZipFile(StringIO(url.read()))
zipfile.infolist()
for line in zipfile.open(file).readlines():
    print line

r = requests.get(zip_url)
print r
zipfile = ZipFile(StringIO(url.read()))
for line in zipfile.open(file).readlines():
    print line
'''

'''
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
'''
#Filter data in memory to put into an array and then a np array do a dict of lists approach













