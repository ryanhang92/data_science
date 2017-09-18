#if group A has larger values than group B on average, does this mean the largest values are from group A? Discuss after completing each of the problems below.


#Assume you have two list of numbers, X and Y, with distribution approximately normal.X and Y have standard deviation equal to 1, but the average of X is different from the average of Y.If the difference in the average of X and the average of Y is larger than 0, how does the proportion of X > a compare to the proportion of Y > a?


#Write a function that #analytically calculates the ratio of these two proportions: Pr(X > a) / Pr(Y > a) as functionofthedifference in thejaverageofX and theaverageofY.
#Hint: Usethescipy.statsmodulefor useful functions related to a normal random variable such as the probability density function, cumulative distribution function and survival function.



#Update: Assume Y is normallydistributedwith mean equal to 0.Showthecurvefor different values of a (a = 2, 3, 4 and 5).
"""
Function
--------
ratioNormals

Return ratio of these two proportions: 
    Pr(X > a)/Pr(Y > a) as function of 
    the difference in the average of X 
    and the average of Y. 

Parameters
----------
diff : difference in the average of X 
    and the average of Y. 
a : cutoff value

Returns
-------
Returns ratio of these two proportions: 
    Pr(X > a)/Pr(Y > a)

Example
-------
$>>> ratioNormals(diff = 1, a = 2)
"""
# your code here
#3(b) Nowc onsider the distribution of income per person from two regions: Asia and South America. Estimate the average income perperson across the countries in thosetworegions.Whichregionhasthelargeraverageofincomeperpersonacrossthecountries in thatregion?
#Update: Use the year 2012.

#Calculate the proportion of countries with income per person that is greater than 10, 000 dollars.Which region has a larger proportion of countries with income per person greater than 10, 000 dollars? If the answer here is different from the answer in 3(b), explain why in light of your answer to 3(a).

#Update: Use the year2012.

#3 (d) For AC209 Students: Re - run this analysis in Problem 3 but compute the average income per
# person for each region, instead of the average of the reported incomes per person across countries in the region.Why are these two different? Hint: use this data set.