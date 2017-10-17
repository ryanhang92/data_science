import numpy as np
import requests
import csv
from StringIO import StringIO
from urllib import urlopen
from zipfile import ZipFile
from collections import defaultdict

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
'''
salary_path = 'data/Salaries.csv'
with open(salary_path, 'rb') as csvfile:
    salary_reader = csv.reader(csvfile, delimiter=',', quotechar='|')

    #Create a feature vector [team, year, salary)
    feature_vectors = []
    for i, row in enumerate(salary_reader):
        if i > 0:
            team_name = row[1]
            year = int(row[0])
            salary = int(row[4])
            feature_vector = np.array([team_name, year, salary])
            feature_vectors.append(feature_vector)

    print feature_vectors
'''


# Problem 1(c) Merge the new summarized Salaries DataFrame and Teams DataFrame together to create a new DataFrame showing wins and total salaries for each team for each year year. Show the head of the new merged DataFrame.
#Hint: Merge the DataFrames using teamID and yearID.
teams_path = 'data/Teams.csv'
win_lookup = defaultdict(int)
with open(teams_path, 'rb') as csvfile:
    teams_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for i, row in enumerate(teams_reader):
        if i > 0:
            year = int(row[0])
            team_name = row[2]
            num_wins = int(row[8])
            win_lookup[(team_name, year)] = int(num_wins)

#print win_lookup

salary_path = 'data/Salaries.csv'
with open(salary_path, 'rb') as csvfile:
    salary_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    #Create a feature vector [team, year, salary), and with wins
    player_feature_vectors = []
    for i, row in enumerate(salary_reader):
        if i == 0:
            continue

        team_name = row[1]
        year = int(row[0])
        salary = int(row[4])

        #Add data including win data
        feature_key = (team_name, year)
        win_value = win_lookup[feature_key]

        if win_value > -1:
            player_feature_vector = np.array([team_name, year, salary, win_value])
        else:
            player_feature_vector = np.array([team_name, year, salary])

        player_feature_vectors.append(player_feature_vector)

print player_feature_vectors

def parse_team_salary_wins_by_year(player_feature_vectors, year):
    team_salary_by_wins_vectors = []
    team_salary_in_year = defaultdict(int)
    team_win_in_year = defaultdict(int)
    for i, player_data in enumerate(player_feature_vectors):
        #print player_data, "player data"
        year_of_data = int(player_data[1])
        if year == year_of_data:
            team = player_data[0]
            salary_of_player = int(player_data[2])
            wins = int(player_data[3])

            team_salary_in_year[team] += salary_of_player
            team_win_in_year[team] = wins

    # Process the two lookups
    for key in team_salary_in_year:
        team_salary_by_win_vector = np.array([key, year, team_salary_in_year[key], team_win_in_year[key]])
        team_salary_by_wins_vectors.append(team_salary_by_win_vector)

    return team_salary_by_wins_vectors


#Problem 1(d) How would you graphically display the relationship between total wins and total salaries for a given year? What kind of plot would be best? Choose a plot to show this relationship and specifically annotate the Oakland baseball team on the on the plot. Show this plot across multiple years. In which years can you detect a competitive advantage from the Oakland baseball team of using data science? When did this end?
#Hints: Use a for loop to consider multiple years. Use the teamID (three letter representation of the team name) to save space on the plot.


import matplotlib.pyplot as plt
# Label point in the plot
def plot_wins_salaries_for_year(feature_vectors):
    x_datas = []
    y_datas = []
    max_wins = 0
    max_salary = 0

    for data in feature_vectors:
        print data
        team, year, salary, wins = data[0], data[1], data[2], data[3]
        x_datas.append(salary)
        y_datas.append(wins)
        if salary > max_salary:
            max_salary = salary
        if wins > max_wins:
            max_wins = wins

    print(len(x_datas), len(y_datas), x_datas, y_datas)

    # print x_datas, y_datas, max_wins, max_salary
    plt.plot(x_datas, y_datas, 'ro')
    #plt.axis([0, max_salary, 0, max_wins])
    plt.show()

def plot_data_over_years(player_feature_vectors, years_list):
    for year in years_list:
        feature_vectors = parse_team_salary_wins_by_year(player_feature_vectors, year)
        plot_wins_salaries_for_year(feature_vectors)


# plot_data_over_years(player_feature_vectors, [1999, 2000])




#Problem 1(e): For AC209 Students: Fit a linear regression to the data from each year and obtain the residuals. Plot the residuals against time to detect patterns that support your answer in 1(d).

from sklearn import linear_model
def get_regression_coefficients_for_year(player_feature_vector, year):
    features = []
    labels = []

    feature_vectors = parse_team_salary_wins_by_year(player_feature_vectors, year)
    for data in feature_vectors:
        salary = data[2]
        wins = data[3]
        features.append(np.array([salary]))
        labels.append(wins)

    reg = linear_model.Ridge(alpha = .5)

    model_features = np.array(features).reshape(-1, 1).astype(np.float)
    model_labels = np.array(labels).astype(np.float)
    print model_features, model_labels, "input model data"
    reg.fit(model_features, model_labels)
    print reg.coef_, "regression coef"
    print reg.intercept_, "regression intercept"


def get_regression_coefficients_over_years(player_feature_vectors, years):
    for year in years:
        get_regression_coefficients_for_year(player_feature_vectors, year)


get_regression_coefficients_over_years(player_feature_vectors, [1995, 2000, 2005])


