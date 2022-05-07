# A dictionary example
students_marks = {"rahul": 90, "sachin": 100, "saurav": 80, "shivam": 70}
print(students_marks["rahul"])

# Adding a new key value pair to the dictionary
students_marks["dexter"] = 94
print(students_marks)
# Deleting a key value pair from the dictionary
del students_marks["sachin"]
print(students_marks)
# Updating a key value pair in the dictionary
students_marks["rahul"] = 88
print(students_marks)

# to get list of values from a dictionary use values() function
print(students_marks.values())
# to get list of keys from a dictionary use keys() function
print(students_marks.keys())
# to get list of keys and values from a dictionary use items() function
print(students_marks.items())

# Iterating manually and using for loop
for key, value in students_marks.items():
    print(key, value)