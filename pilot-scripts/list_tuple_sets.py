# Lists 
list_example = [1, 2, 3, 4, 5]
tuple_example = (1, 2, 3, 4, 5)
set_example = {1, 2, 3, 4, 5}

print(list_example[2])
list_example.append(8) # append function is used to add an element to the end of the list
print(list_example)
list_example.insert(2, 9) # insert function is used to add an element to a specific index of the list
print(list_example)
list_example.remove(3) # remove function is used to remove an element from the list
print(list_example)
list_example.pop() # pop function is used to remove the last element from the list
print(list_example)
list_example.pop(2) # pop function is used to remove an element from a specific index of the list
print(list_example)
list_example.clear() # clear function is used to remove all elements from the list
print(list_example)
list_example.extend([10, 11, 12]) # extend function is used to add a list to the end of the list
print(list_example)
list_example.sort() # sort function is used to sort the list
print(list_example)

print(tuple_example[2]) # to get specific value at an index provided
print(tuple_example[2:]) # to get a slice of the tuple
print(tuple_example[:2]) # to get a slice of the tuple
print(tuple_example[::2]) # to get a slice of the tuple
print(tuple_example[::-1]) # to get a slice of the tuple in reverse order
print(tuple_example[::-2]) # to get a slice of the tuple in reverse order

set_example.add(6) # add function is used to add an element to the set
print(set_example)
set_example.remove(4) # remove function is used to remove an element from the set
print(set_example)
set_example.pop() # pop function is used to remove the last element from the set
print(set_example)
set_example.clear() # clear function is used to remove all elements from the set
print(set_example)

# Set operations
local_brands = {"Nike", "Adidas", "Reebok", "Puma", "Asics", "sketchers"}
foreign_brands = {"Nike", "Adidas", "Reebok", "Puma", "Asics", "New Balance"}

# Both sets have common values to get, the unique value which is present in local_brand and not in foreign_brand
# we use the difference function
print(local_brands.difference(foreign_brands)) # retruns sketchers
print(foreign_brands.difference(local_brands)) # retruns New Balance

# to get the list of values which are present in both the sets we use union function
print(local_brands.union(foreign_brands)) # retruns {'Nike', 'Adidas', 'Reebok', 'Puma', 'Asics', 'sketchers', 'New Balance'}

# to get the list of values which are present in both the sets we use intersection function
print(local_brands.intersection(foreign_brands)) # retruns {'Nike', 'Adidas', 'Reebok', 'Puma', 'Asics'}

# to get the list of values  other than the values which are present in both the sets we use symmetric_difference function
print(local_brands.symmetric_difference(foreign_brands)) # retruns {'New Balance', 'sketchers'}

# Updated the set on left side to have only values which are not present in right side set
print(local_brands.difference_update(foreign_brands)) # local_brands will be updated to {'sketchers'}
print(local_brands)

# updates the left side set to have only values which are present in both the sets
print(local_brands.intersection_update(foreign_brands)) # local_brands will become blank 
print(local_brands)
