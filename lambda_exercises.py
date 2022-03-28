''' 1)
Write a Python program to filter a list of integers using Lambda. Go to the editor
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers from the said list:
[2, 4, 6, 8, 10]
Odd numbers from the said list:
[1, 3, 5, 7, 9]
'''
from unittest import result

original_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Even numbers from said list:")
even_nums = list(filter(lambda num: num%2 == 0, original_nums))
print(even_nums)
print("Odd numbers from said list:")
odd_nums = list(filter(lambda num: num%2 == 1, original_nums))
print(odd_nums)

''' 2)
find which days of the week have exactly 6 characters.
'''

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

print("Days of the week with 6 characters")
six_days = list(filter(lambda day: len(day) == 6, weekdays))
print(six_days)







''' 3)
remove specific words from a given list 
Original list:
['orange', 'red', 'green', 'blue', 'white', 'black']

Remove words:
['orange', 'black']

After removing the specified words from the said list:
['red', 'green', 'blue', 'white']

'''
def remove_words(list1, remove_words):
    result = list(filter(lambda word: word not in remove_words, list1))
    return result
        
colors = ['orange', 'red', 'green', 'blue', 'white', 'black']
remove_colors = ['orange','black']
print("Original list:")
print(colors)
print("\nRemove words:")
print(remove_colors)
print("\nAfter removing the specified words from the said list:")
print(remove_words(colors, remove_colors))




''' 4)
 remove all elements from a given list present in another list
Original lists:
list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2: [2, 4, 6, 8]

Remove all elements from 'list1' present in 'list2:
[1, 3, 5, 7, 9, 10]
 '''

def removed_element(list1,list2):
    result = list(filter(lambda x: x not in list2, list1))
    return result 

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [2, 4, 6, 8]

print("Original lists:")
print("List1:" , list1)
print("List2:" , list2)
print("\nRemoved all elements from list1 present in list2")
print(removed_element(list1,list2))



''' 5)
find the elements of a given list of strings that contain specific substring using lambda
Original list:
['red', 'black', 'white', 'green', 'orange']
Substring to search:
ack
Elements of the said list that contain specific substring:
['black']
Substring to search:
abc
Elements of the said list that contain specific substring:
[]

'''
def find_substring(str1, sub_str):
    result = list(filter(lambda i: sub_str in i, str1))
    return result

colors = ['red', 'black', 'white', 'green', 'orange']
print("Original List:" , colors)

sub_str = "ack"
print("\nSubstring to search:\n", sub_str)
print("Elements of the said list that contain specific substring: ")
print(find_substring(colors, sub_str))

sub_str = "abc"
print("\nSustring to search:\n", sub_str)
print("Elements of the said list that contain specific substring:")
print(find_substring(colors, sub_str))



''' 6)
check whether a given string contains a capital letter, a lower case letter, a number and a minimum length of 8 characters.
(This is like a password verification function, HINT: Python function 'any' may be useful)
'''


def check_string(s):
    message = []
    if not any(x.isupper() for x in s):
        message.appends('String must have 1 upper case character.')
    if not any(x.islower() for x in s):
        message.appends('String must have 1 lower case character.')
    if not any(x.isdigit() for x in s):
        message.appends('String must have 1 number.')
    if len(s) < 8: 
        message.append('String length should be at least 8.')
    if not message: 
        message.append('Valid String.')
    return message 

s= input('Input the string: ')
print(check_string(s))

''' 7)
Write a Python program to sort a list of tuples using Lambda.

# Original list of tuples:
original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# Expected Result:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
'''
original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
print("Original list of tuples:")
print(original_scores)
original_scores.sort(key = lambda x: x[1])
print('\nSorting the List of Tuples:')
print(original_scores)