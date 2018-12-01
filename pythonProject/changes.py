#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 20:46:56 2018

@author: maluroldan
"""

import pandas

# changing and saving data

# read the csv data into the dataframe
namesdf = pandas.read_csv("users.csv")
# prints the original dataframe
print()
print("original dataframe")
print(namesdf)
# changes the value of the password correspnding to name mroldan
namesdf.loc[namesdf["name"] == "mroldan", "password"] = "bus9212"
# prints changed dataframe
print()
print("edited dataframe")
print(namesdf)
# read the csv data into the dataframe
namesdf = pandas.read_csv("users.csv")
# prints original data (since changes were not written to the csv file)
print()
print("still the original data since dataframe changes were not written to csv")
print(namesdf)
# changes the password corresponding to the name mroldan
namesdf.loc[namesdf["name"] == "mroldan", "password"] = "bus9213"
# writes the changed data to the csv file
namesdf.to_csv("users.csv", index=False)
# reads the data into the dataframe
namesdf = pandas.read_csv("users.csv")
# prints the changed data since the edited dataframe was written to the
# csv file in line 28
print()
print("prints the edited file after dataframe changes were written to csv")
print(namesdf)
# code below returns the csv file to its original state
namesdf.loc[namesdf["name"] == "mroldan", "password"] = "bus921"
namesdf.to_csv("users.csv", index=False)

"""
more code examples at
https://medium.com/@msalmon00/helpful-python-code-snippets-for-data-exploration-in-pandas-b7c5aed5ecb9
"""

# sorting
# reads the file into the namesdf dataframe
namesdf = pandas.read_csv("users.csv")
print()
print("This is the unsorted dataframe")
print(namesdf)
# sorts the file by last name in decending order
namesdfsorted = namesdf.sort_values("name", ascending=False)
print()
print("This is the dataframe sorted in descending order of name")
print(namesdfsorted)
# sorts the file by last name in ascending order
namesdfsorted2 = namesdf.sort_values("name", ascending=True)
print()
print("This is the dataframe sorted in ascending order of name")
print(namesdfsorted2)
# save the sorted file (ascending) into a new file and check file contents
namesdfsorted2.to_csv("employeessorted.csv", index=False)
namesdfsortedcheck = pandas.read_csv("userssorted.csv")
print()
print("This is the sorted data read from the csv file")
print(namesdfsortedcheck)
