import pandas as pd

# Your code goes here. Create a dataframe matching the above diagram and assign it to the variable fruits.

fruits = pd.DataFrame({"Apples":[30],"Bananas":[21]}) 
# Apples	Bananas
# 0	30	21

# Your code goes here. Create a dataframe matching the above diagram and assign it to the variable fruit_sales.

fruit_sales = pd.DataFrame({"Apples":[35,41],"Bananas":[21,34]},index=["2017 Sales","2018 Sales"])
# 	Apples	Bananas
# 2017 Sales	35	21
# 2018 Sales	41	34

ingredients = pd.Series(["4 cups","1 cup","2 large","1 can"],index=["Flour","Milk","Eggs","Spam"],name="Dinner")
# Create a variable ingredients with a Series that looks like:

# Flour     4 cups
# Milk       1 cup
# Eggs     2 large
# Spam       1 can
# Name: Dinner, dtype: object

# read dataset
reviews = pd.read_csv("../input/wine-reviews/winemag-data_first150k.csv",index_col=0)

# In the cell below, write code to save this DataFrame to disk as a csv file with the name cows_and_goats.csv.
animals = pd.DataFrame({'Cows': [12, 20], 'Goats': [22, 19]}, index=['Year 1', 'Year 2'])
animals

# animals.to_csv("cows_and_goats.csv")

