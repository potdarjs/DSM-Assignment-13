"""
Assignment 11
Data Science Masters

"""
"""
Take this monstrosity as the DataFrame to use in the following puzzles:
df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm',
'Budapest_PaRis', 'Brussels_londOn'],
'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
'12. Air France', '"Swiss Air"']})
"""
#%%
# Import libraries
import pandas as pd
import numpy as np
from IPython.display import display

#%%
# Create Dataframe
df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm', 'Budapest_PaRis', 'Brussels_londOn'], 
                   'FlightNumber': [10045, np.nan, 10065, np.nan, 10085], 
                   'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]], 
                   'Airline': ['KLM(!)', ' (12)', '(British Airways. )', '12. Air France', '"Swiss Air"']})
df.head()  # Check created dataframe

#%%
""" Problem 1. 
Some values in the the FlightNumber column are missing. These numbers are meant to increase by 10 
with each row so 10055 and 10075 need to be put in place. 
Fill in these missing numbers and make the column an integer column (instead of a float column).
"""
df['FlightNumber'] = df['FlightNumber'].interpolate().astype(int)
display(df)

"""
Problem 2. The FromTo column would be better as two separate columns! Split each string on the 
underscore delimiter to give a new temporary DataFrame with the correct values. 
Assign the correct column names to this temporary DataFrame. """
df['From'] = df['From_To'].str.split('_').str[0]
df['To'] = df['From_To'].str.split('_').str[1]
display(df)

"""
Problem 3. Notice how the capitalisation of the city names is all mixed up in this temporary DataFrame. 
Standardise the strings so that only the first letter is uppercase (e.g. "londON" should become "London".)"""
df['From'] = df['From'].str.capitalize()
df['To'] = df['To'].str.capitalize()
display(df)

"""
Problem 4. Delete the From_To column from df and attach the temporary DataFrame from the previous questions."""

df.drop('From_To', axis=1, inplace=True)
display(df)

"""
Problem 5. In the RecentDelays column, the values have been entered into the DataFrame as a list. 
We would like each first value in its own column, each second value in its own column, and so on. 
If there isn't an Nth value, the value should be NaN. """

delayFlights = pd.DataFrame(df['RecentDelays'].values.tolist())
display(delayFlights)

"""

Expand the Series of lists into a DataFrame named delays, rename the columns delay_1, delay_2, etc. 
and replace the unwanted RecentDelays column in df with delays."""
delayFlights = delayFlights.rename(columns = {0: "Delay_1", 1: "Delay_2", 2: "Delay_3"})
display(delayFlights)

df = pd.concat([df,delayFlights], axis=1)
display(df)

df.drop('RecentDelays', axis=1, inplace=True)
display(df)
