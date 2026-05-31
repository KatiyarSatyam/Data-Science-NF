#1. Given two sets, check if one set is a subset of another. 
set1 = {1, 2, 3, 4}
set2 = {2, 3}
if set2.issubset(set1):
    print("Set2 is a subset of Set1.")
else:
    print("Set2 is not a subset of Set1.")

#2. Write a program to check whether two lists have at least one common element using sets. 
list1 = [1, 2, 3, 4]
list2 = [4, 5, 6]
set1 = set(list1)
set2 = set(list2)
if set1.intersection(set2):
    print("The lists have at least one common element.")
else:
    print("The lists do not have any common elements.")
    