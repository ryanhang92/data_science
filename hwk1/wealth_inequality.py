#Using the list of countries by continent from World Atlas data, load in the countries.csv file into a pandas DataFrame and name this data set as countries. This data set can be found on Github in the 2014_data repository here.


#Using the data available on Gapminder, load in the Income per person (GDP/capita, PPP$ inflation-adjusted) as a pandas DataFrame and name this data set as income.


#Hint: Consider using the pandas function pandas.read_excel() to read in the .xlsx file directly.


#Transform the data set to have years as the rows and countries as the columns. Show the head of this data set when it is loaded.


#Graphically display the distribution of income per person across all countries in the world for any given year (e.g. 2000). What kind of plot would be best?


#Write a function to merge the countries and income data sets for any given year.
"""
Function
--------
mergeByYear

Return a merged DataFrame containing the income, 
country name and region for a given year. 

Parameters
----------
year : int
    The year of interest

Returns
-------
a DataFrame
   A pandas DataFrame with three columns titled 
   'Country', 'Region', and 'Income'. 

Example
-------
#>>> mergeByYear(2010)
"""


#Use exploratory data analysis tools such as histograms and boxplots to explore the distribution of the income per person by region data set from 2(c) for a given year. Describe how these change through the recent years?
#Hint: Use a for loop to consider multiple years.