# 1. Write a program to find the largest and smallest elements in a list.  
numbers = [3, 1, 4, 1, 5, 9]
largest = max(numbers)
smallest = min(numbers)
print("Largest element:", largest)
print("Smallest element:", smallest)

# 2. Write a program to remove duplicate elements from a list.  
my_list = [1, 2, 3, 4, 5, 2, 3]
unique_list = list(set(my_list))
print("List with duplicates removed:", unique_list)

# 3. Write a program to reverse a list without using built-in reverse functions.  
my_list = [1, 2, 3, 4, 5]
reversed_list = []
for i in range(len(my_list)-1, -1, -1):
    reversed_list.append(my_list[i])
print("Reversed list:", reversed_list)

# 4. Write a program to count even and odd numbers in a list.  
numbers = [1, 2, 3, 4, 5, 6]
even_count = 0
odd_count = 0
for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even numbers:", even_count)
print("Odd numbers:", odd_count)

# 5. Write a program to merge two lists and sort the final list.  
list1 = [1, 3, 5]
list2 = [2, 4, 6]
merged_list = list1 + list2
merged_list.sort()
print("Merged and sorted list:", merged_list)

# 6. Write a program to find the second largest element in a list.
numbers = [3, 1, 4, 1, 5, 9]
unique_numbers = list(set(numbers))
unique_numbers.sort(reverse=True)
if len(unique_numbers) >= 2:
    print("Second largest element:", unique_numbers[1])
else:
    print("Not enough unique elements")
    
