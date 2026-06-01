# 7. Write a program to check whether an element exists in a tuple.
my_tuple = (1, 2, 3, 4, 5)
element = int(input("Enter an element to check: "))
if element in my_tuple:
    print(element, "exists in the tuple.")
else:
    print(element, "does not exist in the tuple.")

# 8. Write a program to count the occurrence of an element in a tuple.  
my_tuple = (1, 2, 3, 4, 5, 2, 3, 2)
element = int(input("Enter an element to count: "))
count = my_tuple.count(element)
print(element, "occurs", count, "times in the tuple.")

# 9. Write a program to sort a list of tuples based on tuple values.  
list_of_tuples = [(3, 'Alice'), (1, 'Bob'), (2, 'Charlie')]
sorted_list = sorted(list_of_tuples, key=lambda x: x[0])
print("Sorted list of tuples:", sorted_list)
    
# 10. Write a program to convert a tuple into a list and a list into a tuple. 
my_tuple = (1, 2, 3, 4, 5)
my_list = list(my_tuple)
print("Tuple to List:", my_list)
my_list = [1, 2, 3, 4, 5]
my_tuple = tuple(my_list)
print("List to Tuple:", my_tuple)
