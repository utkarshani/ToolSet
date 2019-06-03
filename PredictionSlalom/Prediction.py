import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
#import mpl_toolkits

#print ("Hello World")

#Read the input file as pandas dataframe
file = pd.read_csv('/Users/Utkarshani/Desktop/Slalom/SalesbyHour.csv')
#print (file.head())

print ("\n Describing the file \n")
print (file.describe())

file['SalesRevenue'].value_counts().plot(kind='bar')
plt.title('Sales Revenue')
plt.xlabel('Revenue')
plt.ylabel('Sales')
plt.show()