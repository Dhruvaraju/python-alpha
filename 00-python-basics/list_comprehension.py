example_numbers = [1,2,3,4,5,6]
# List comprehension is used to create a new list from an existing list
# The following is a list comprehension that creates a new list from the existing list
new_number_list = []
for number in example_numbers:
    new_number_list.append(number * 2)
print(new_number_list)

# The same can be achieved by below code
list_com_from_example = [number * 6 for number in example_numbers]
print(list_com_from_example)

# List comprehension on strings
# The following is a list comprehension that creates a new list from the existing list
friends = ["John", "Paul", "George", "Ringo", "Rango", "Ronald"]
friends_name_starting_with_r = [friend for friend in friends if friend.startswith("R")]
print(friends_name_starting_with_r)