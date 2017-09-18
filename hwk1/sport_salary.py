import numpy as np
import requests
import csv
from StringIO import StringIO
from urllib import urlopen
from zipfile import ZipFile

#Read from the web
zip_url = "http://seanlahman.com/files/database/lahman-csv_2014-02-14.zip"

'''
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
'''

#Process the data once in the right data structure


# Problem 1(b) Summarize the Salaries DataFrame to show the total salaries for each team for each year. Show the head of the new summarized DataFrame.
#Read file from path
salary_path = 'data/Salaries.csv'
with open(salary_path, 'rb') as csvfile:
    salary_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in salary_reader:
        print row


    #Create a feature vector [team, year, salary)




# Problem 1(c) Merge the new summarized Salaries DataFrame and Teams DataFrame together to create a new DataFrame showing wins and total salaries for each team for each year year. Show the head of the new merged DataFrame.
#Hint: Merge the DataFrames using teamID and yearID.


    #Create a feature vector [team, year, salary, wins)



#Problem 1(d) How would you graphically display the relationship between total wins and total salaries for a given year? What kind of plot would be best? Choose a plot to show this relationship and specifically annotate the Oakland baseball team on the on the plot. Show this plot across multiple years. In which years can you detect a competitive advantage from the Oakland baseball team of using data science? When did this end?
#Hints: Use a for loop to consider multiple years. Use the teamID (three letter representation of the team name) to save space on the plot.


    #For each year
        #Show each team as a point, graph salary on x axis and wins on y axis as y is the dependent variable



#Problem 1(e): For AC209 Students: Fit a linear regression to the data from each year and obtain the residuals. Plot the residuals against time to detect patterns that support your answer in 1(d).

    #For each year
        #Train linear classifier where the features are just the salary, and label is wins






