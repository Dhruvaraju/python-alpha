# Assigning tuple to multiple variables
tuple_example = 49,94
convergent, divergent = tuple_example
print("Value of convergent",convergent)
print("Value of divergent",divergent)
# Destructuring a dictionary using items()
dictionary_example = {"alpha": 20, "beta": 30, "gamma": 40}
for alphabet in dictionary_example.items():
    print(alphabet)
# We can destructure it further more as
for key, value in dictionary_example.items():
    print(key, value)
# Destructuring list of tuples
list_of_tuples = [("alpha",1,"dev"), ("beta",2,"devops"), ("gamma",3,"security")]
for name, level, role in list_of_tuples:
    print(f"{name} is a level {level} with a {role} role")
# Ignoring a variable in a tuple
person_description = ("John", 25, "developer")
name, _, role = person_description
print("person", name,"is a", role)
# Destructuring a list using head and tail
list_of_number = [1,2,3,4,5,6,7,8,9,10]
head, *tail = list_of_number
print("head", head, "tail", tail)
*head, tail = list_of_number
print("head", head, "tail", tail)