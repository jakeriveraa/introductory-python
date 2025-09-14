# Python Collections
# group of data elements in python that allows us to store multiple
# data in a single variable
# lists, tuples, dictionaries, set, array

# 1. Lists - may're used to store multiple items in a single variable
# and they are defined by square brackets []
# note: Lists are ordered, changeable (or mutable), and allow duplicates

empty_list = []
print(f"collection data type: {type(empty_list)}")

fruits_list = ["apple", "banana", "cherry", "orange", "banana"] # this is a list wiht defauly values
#
print(f"Empty list: {empty_list}")
print(f"List: {fruits_list}")
print(f"Retrieving a value: {fruits_list[0]}")
print(f"List length: {len(fruits_list)}")