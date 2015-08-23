# Set your local path
path_local = '/Users/vamshiguduguntla/Downloads/CouponPrediction/'
import pandas as pd
import csv
import numpy as np
# Browse through the user_list 
user_list = pd.read_csv(path_local+'user_list.csv')
# top 5 rows
user_list.head()
#number of user id's we have in the file
len(user_list.USER_ID_hash.ravel())
# a quick summary
user_list.USER_ID_hash.describe()

# summary of ages
user_list.AGE.describe()

#1.Matplot lib of normal curve of age distribution
#<insert code below>
import matplotlib.pyplot as plt
plt.hist(user_list.AGE)
plt.show()

#2. Code for number of males and number of females.
#<insert code below>
