#1. Write a program to create a dictionary from two lists: one of keys and one of values.
keys = ['name', 'age', 'city']
values = ['Alice', 30, 'New York']
my_dict = dict(zip(keys, values))
print(my_dict)

#2. Merge two dictionaries into one 
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged_dict = {**dict1, **dict2}
print(merged_dict)

#3. Write a program to sort a dictionary by its values. 
my_dict = {'Alice': 85, 'Bob': 90, 'Charlie': 78}
sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print(sorted_dict)
