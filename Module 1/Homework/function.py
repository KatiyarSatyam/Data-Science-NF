# 1. Create a Function to Check Whether Two Strings are Anagrams Problem 
# Write a function that accepts two strings and returns True if both are anagrams, otherwise False. 
def are_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    return sorted(str1) == sorted(str2)

# 2. Create a Function to Find Second Largest Number in a List Problem 
# Write a function that accepts a list and returns the second largest number.
def second_largest(numbers):
    if len(numbers) < 2:
        return None  # Not enough elements for second largest
    unique_numbers = list(set(numbers))  # Remove duplicates
    unique_numbers.sort()  # Sort the unique numbers
    return unique_numbers[-2]  # Return the second last element (second largest)

# 3. Create a Function to Count Vowels in a Sentence Problem 
# Write a function that accepts a sentence and returns the count of each vowel.
def count_vowels(sentence):
    vowels = 'aeiouAEIOU'
    vowel_count = {vowel: 0 for vowel in vowels}
    
    for char in sentence:
        if char in vowels:
            vowel_count[char] += 1
        return vowel_count

# 4. Create a Function to Check Whether a Number is an Armstrong Number Problem 
# Write a function that returns True if a number is an Armstrong number. 
def is_armstrong_number(num):
    num_str = str(num)
    num_digits = len(num_str)
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    return armstrong_sum == num

# 5. Create a Function to Find Common Elements Between Multiple Lists Problem 
# Write a function that accepts three lists and returns common elements. 
def common_elements(list1, list2, list3):
    return list(set(list1) & set(list2) & set(list3))