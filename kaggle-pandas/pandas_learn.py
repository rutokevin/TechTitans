# import pandas
import pandas as pd

# Creating data
# There are two core objects in pandas: the DataFrame and the Series.

# DataFrame¶
# A DataFrame is a table. It contains an array of individual entries, each of which has a certain value. Each entry corresponds to a row (or record) and a column.

pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})

# DataFrame entries are not limited to integers. For instance, here's a DataFrame whose values are strings:

pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']})

# The dictionary-list constructor assigns values to the column labels, but just uses an ascending count from 0 (0, 1, 2, 3, ...) for the row labels. Sometimes this is OK, but oftentimes we will want to assign these labels ourselves.

# The list of row labels used in a DataFrame is known as an Index. We can assign values to it by using an index parameter in our constructor:

pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])



# Series
# A Series, by contrast, is a sequence of data values. If a DataFrame is a table, a Series is a list. And in fact you can create one with nothing more than a list:

pd.Series([1, 2, 3, 4, 5])

# A Series is, in essence, a single column of a DataFrame. So you can assign row labels to the Series the same way as before, using an index parameter. However, a Series does not have a column name, it only has one overall name:

pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')

# The Series and the DataFrame are intimately related. It's helpful to think of a DataFrame as actually being just a bunch of Series "glued together". We'll see more of this in the next section of this tutorial.

# Reading data files
# Being able to create a DataFrame or Series by hand is handy. But, most of the time, we won't actually be creating our own data by hand. Instead, we'll be working with data that already exists.

# Data can be stored in any of a number of different forms and formats. By far the most basic of these is the humble CSV file. When you open a CSV file you get something that looks like this:

# Product A,Product B,Product C,
# 30,21,9,
# 35,34,1,
# 41,11,11
# So a CSV file is a table of values separated by commas. Hence the name: "Comma-Separated Values", or CSV.

# Let's now set aside our toy datasets and see what a real dataset looks like when we read it into a DataFrame. We'll use the pd.read_csv() function to read the data into a DataFrame. This goes thusly:


wine_reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv")

# We can use the shape attribute to check how large the resulting DataFrame is:
wine_reviews.shape #(129971, 14)


# So our new DataFrame has 130,000 records split across 14 different columns. That's almost 2 million entries!

# We can examine the contents of the resultant DataFrame using the head() command, which grabs the first five rows:

wine_reviews.head()

# The pd.read_csv() function is well-endowed, with over 30 optional parameters you can specify. For example, you can see in this dataset that the CSV file has a built-in index, which pandas did not pick up on automatically. To make pandas use that column for the index (instead of creating a new one from scratch), we can specify an index_col.

wine_reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
wine_reviews.head()
