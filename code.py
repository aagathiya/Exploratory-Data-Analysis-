# --------------
import pandas as pd

# Code starts here

#### Data 1
# Load the data
data = pd.read_csv(path)
print(data.head())
print('X'*33)

print('Info of the data is:', data.info())
print('X'*33)
print(data.describe(), 'Description of data is:')
print('Shape of the data is:', data.shape)
print('X'*33)
print('Size of the data is:', data.size)
print('X'*33)
data.hist(column = ['price'], bins = 10, figsize = (5,5))




# Overview of the data


# Histogram showing distribution of car prices


# Countplot of the make column


# Jointplot showing relationship between 'horsepower' and 'price' of the car


# Correlation heat map


# boxplot that shows the variability of each 'body-style' with respect to the 'price'


#### Data 2

# Load the data


# Impute missing values with mean


# Skewness of numeric features



# Label encode 



# Code ends here


