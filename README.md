# python_alpha

- [python_alpha](#python_alpha)
    - [python](#python)
    - [Workspace setup](#workspace-setup)
    - [First program](#first-program)
    - [Variables](#variables)
    - [Data-types in python](#data-types-in-python)
    - [Strings](#strings)
    - [String formatting](#string-formatting)
    - [User Input](#user-input)
    - [Simple app to calculate age in months and seconds](#simple-app-to-calculate-age-in-months-and-seconds)
    - [List, tuples and Sets](#list-tuples-and-sets)
      - [List](#list)
      - [Tuple](#tuple)
      - [set](#set)
    - [Set operations](#set-operations)
    - [Booleans and comparison](#booleans-and-comparison)
    - [If and corresponding operations](#if-and-corresponding-operations)
      - [In keyword](#in-keyword)
    - [Loops](#loops)
      - [While](#while)
      - [For](#for)
    - [List Comprehension](#list-comprehension)
    - [Dictionaries](#dictionaries)
    - [Variable destructuring](#variable-destructuring)
    - [Functions](#functions)
    - [Function parameters](#function-parameters)
    - [Lambda](#lambda)
    - [Dictionary comprehension](#dictionary-comprehension)
    - [Unpacking arguments](#unpacking-arguments)
    - [Unpacking keyword Arguments](#unpacking-keyword-arguments)
    - [Object oriented programming](#object-oriented-programming)

### python

- A scripting language, which can be used for automating tasks
- Extension of python program files is `.py`.
- Python installation will give an ide called as idle which can be used to run a python program.
- to check if python is installed in your machine, type in the word **python** in command prompt. it will show the version of python installed.

### Workspace setup

- Download it from python website and install using the exe, check add python to path.
- vscode can be used for development.
- install python extension from microsoft.
- In settings check for, execute in file dir and check the checkbox available under python. (This will enable terminal to run scripts from current terminal)
- Update debug options add current working directory and stop on entry.

### First program

- python uses functions to perform operations.
- `print` is used to print a line to console. `print ('Console is active');`
- To take user input you can use a function called input. ` var1 = input('Enter your name : ');`
- To execute a python script in windows command prompt, use `python <<filename with entire path>>`
  `python c:/folder1/myapp.py`

> Single line Comments in python will start with `#` , for multi lines use `#` for every line.

### Variables

- Should start with an alphabet, should not contain space.
- variables starting with '\_' and '\_\_' are python reserved keywords should not use them for your programs.
- variables can be assigned in many ways

```python
    var = "testdata" // assigning string to var
    a = 5 // assigning 5 to variable a
    a=b=c= 10 // assigning the variables a,b,c to 10
    a,b,c = 1,2,3 // assigning multiple variable at once, a to 1, b to 2, c to 3
```

- function id is used to get the memory location of an attribute. example id(a) will give the memory location of a.

### Data-types in python

- The following are the data types in python
  - strings
  - numbers
  - booleans
  - lists
  - sets
  - frozensets
  - tuples
  - ranges
  - dictionaries
  - None
- Few are mutable (lists, dictionaries, sets), these can be modified after creation and few are immutable (Strings, numbers, tuples and frozensets) these cannot be modified after creation.

### Strings

- A sequence of characters, python uses index to identify each character.
- index start from left from 0 and -1 from right.
- Some of the string operations are performed in variables.py

### String formatting

- **F string** allows embedding variable in a string. Character f is added in front of a string.

```python
message = "hello"
finalMessage = f"{message} world"
```

- Templates can also be used for string formatting an empty `{}` is defined with in a string, it can be replaced by using `format` function.

```python
message01 = "This message is for {}."
message02 = message01.format("developers")
print(message02)
```

### User Input

- The input function is used to get user input with a user prompt embedded to it.
- The input function always returns a string
- Input need to be converted to strings if it is used to run arithmetic operations.

```python
user_name = input("What is your name? ") # user will be prompted with What is your name?
print(f"Hello {user_name}, welcome!")

square_feet = input("Enter the square feet of the room: ")
square_feet = int(square_feet)
square_meters = square_feet / 10.8
print(f"The provided {square_feet} square feet is {square_meters} square meters.")

# we can also format numbers example below
print(f"The provided {square_feet} square feet is {square_meters:.2f} square meters with 2 decimal points.")
```

> Additional number formatting info can be found at https://blog.teclado.com/python-formatting-numbers-for-printing/

### Simple app to calculate age in months and seconds

```python
user_age = int(input("What is your age (in years)? "))
print(f"You are {user_age} years old.")
print(f"You are {user_age * 12} months old.")
print(f"You are {user_age * 365 * 24 * 60 * 60} seconds old.")
```

### List, tuples and Sets

- All these are used to store groups of values.
- We can use sum function to get sum of integers in a list, tuple or set

#### List

- A list is defined with as square braces like `list_example = ["this", "is", "list"]`
- Preserves the order of values
- Data can be retrieved by index like `list_example[0]' returns `this`
- Data can be added by append function
- List is mutable
- Other functions are explained in the example

#### Tuple

- A list is defined with as normal braces like `tuple_example = ("this", "is", "tuple")`
- Preserves the order of values
- Data can be retrieved by index like `tuple_example[0]' returns `this`
- immutable
- Other functions are explained in the example

#### set

- A list is defined with as curly braces like `set_example = ("this", "is", "set")`
- Does not preserve the order of values
- Data cannot be retrieved by index
- Mutable, adding data can be done using add function.
- Other functions are explained in the example

```python
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
```

### Set operations

We can get difference between two sets the common elements in both sets, elements which are present in one set and not present in another.
These functions are present in the example below.

```python
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
```

### Booleans and comparison

- A boolean has two values true or false
- It will start with capital case True or False
- Comparisons like >, <, >=, <=, ==, != will result in boolean values
- 'is' can be used to check if the memory location is same, explained in below example

> Do not use `is` unless it is a memory location check.

```python
# Boolean is a data type that can only have two values: True or False
# In python boolean will start with capital case
boolean_example = True
print(boolean_example)

hero = "Batman"
villain = "Joker"
print(hero == villain) # False
print(hero != villain) # True
# We have other comapisions like >, <, >=, <=, !=

marvel_set = {"Spider-man", "ironman","hulk"}
dc_set = {"batman", "superman", "flash", "wonder-woman"}
marvel_genesis_set = {"Spider-man","ironman","hulk"}

print(marvel_set == marvel_genesis_set) # true
print(marvel_set is marvel_genesis_set) # false
# The 'is' keyword will check the exact value with memory location hence it returns false
marvel_genesis_set = marvel_set
print(marvel_set == marvel_genesis_set) # true
# As both are the same it will return true
```

### If and corresponding operations

- any `if` statement is used for conditional checks
- general syntax will appear as below

```python
if conditional-statement :
    print("condition satisfied so this will be print")
```

- colon after condition and indentation in the next-line is required for python to understand that this is an if statement.
- like other languages we can use else block as below.

```python
if conditional-statement :
    print("condition satisfied so this will be print")
else :
    print("when condition is not met this will be executed")
```

- we can also use else if for secondary conditions as 'elif`

```python
if conditional-statement :
    print("condition satisfied so this will be print")
elif secondary-condition :
    print("secondary condition satisfied")
else :
    print("None of the conditions satisfied")
```

**Example**

```python
day_of_week = input("Enter a day of the week: ").lower()
if day_of_week == "monday":
    print("Today is Monday")
elif day_of_week == "tuesday":
    print("Today is Tuesday")
else:
    print("Today is not Monday or Tuesday")
```

#### In keyword

- in keyword is used to see if a value is present in set or list or tuple or string

```python
movies_set = {"The Matrix", "The Matrix Reloaded", "The Matrix Revolutions"}
if "The Matrix" in movies_set:
    print("The Matrix is in the set")

if "hi" in "hi how are you":
    print("hi is in the string")

number_entered = int(input("Enter a number: "))
if number_entered == 7:
    print("you guessed it right")
elif number_entered - 7 in (-1,1):
    print("Missed it by 1")
else:
    print("incorrect")

# The same class above can be rewritten using abs function
number_entered = int(input("Enter a number: "))
if number_entered == 7:
    print("you guessed it right")
elif abs(number_entered - 7) == 1:
    print("Missed it by 1")
else:
    print("incorrect")
```

### Loops

#### While

- While will be executed until the condition fails
- if you never want a while loop to exit just use while true, to break the flow use break keyword.

#### For

- Is used when you have a list of values to iterate through like a list set or tuple
- It is used in conjunction with the `in` keyword.

```python
number = 9
player_opinion = input("Do you wish to play? (Y/n): ")

while player_opinion != "n":
    player_guess = int(input("Enter a number: "))
    if player_guess == number:
        print("You guessed it right")
    elif abs(player_guess - number) == 1:
        print("You missed it by 1")
    else:
        print("You guessed it wrong")

    player_opinion = input("Do you wish to play? (Y/n): ")

# The same can be executed as below
# while True:

another_number = 7
while True:
    second_game_check = input("Do you wish to guess another number? (Y/n): ")
    if second_game_check == "n":
        break
    player_guess = int(input("Enter a number: "))
    if player_guess == another_number:
        print("You guessed it right")
    elif abs(player_guess - another_number) == 1:
        print("You missed it by 1")
    else:
        print("You guessed it wrong")

movies_seen = {"up", "red", "conair", "matrix", "independence"}
for movie in movies_seen:
    print(movie)

# We can also use range ust to iterate for a certain number of times
for i in range(10):
    print(i)
```

### List Comprehension

- Minor operations on lists can be performed using them
- We can perform operations on integer and string

```python
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
```

### Dictionaries

- Used to store key and value pairs.
- Can use subscript to get value of a specific key.
- To get lists of values use the values() function.
- To get list of keys use keys() function
- To get list of keys and values use items() function

```python
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
```

### Variable destructuring

While declaring a tuple we don't have to provide braces, only while declaring it as part of collection or
inside some other datatype we have to mention the braces. `x = 2,3` is considered as tuple,

- multi variable declaration `a,d = 1,2` we can also declare as

```python
x=2,3
a,b = x
```

- we can destructure a dictionary as list of tuples by using items function
- To ignore a variable use `_` this is a common notation used across all python developers.
- head and tail can be used to destructure a list
- Some other examples are mentioned below

```python
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
```

### Functions

- A reusable piece of code
- use keyword 'def' to create a function and define function name add parenthesis aster that with a colon.
- Below it provide indentation and write your code.

```python
def derive_age_in_seconds():
    user_age = input("Enter your age:")
    age_in_seconds = int(user_age) *365 * 24 * 60 * 60
    print("Your age in seconds is:", age_in_seconds)

derive_age_in_seconds()
```

- Define global variables used in functions before the function definition
- do not use the same variable name in the function definition and the global variable

### Function parameters

- We can pass parameters to a function and provide set default values to them
- Functions can also return values by using the `return` keyword.

```python
# Function with parameters
def greet_a_user(name):
    print("Hello", name)

greet_a_user("dexter")
# Function parameters with default values
def select_payment_method(payment_method = "paypal"):
    print("You have selected payment method as: ", payment_method)

select_payment_method()
select_payment_method("debit_card")
# Returning values from a function
def add_numbers(num1, num2):
    return num1 + num2
print(add_numbers(2, 3))
# function with multiple parameters
def add_numbers(num1, num2, num3=6):
    return num1 + num2 + num3
print(add_numbers(2, 3))
```

### Lambda

- A function with out a name is called lambda function
- Generally used to shorten the code of a function
- These are single line functions, do not cram too much implementation write a separate function if the implementation is large.
- Use map function when and all possible.
- As map returns an object always encapsulate it.

```python
def add(x,y):
    return x+y
# Above function can be converted to lambda as below
addition = lambda x,y: x+y
print(add(2,3))
print(addition(2,3))
# If we do not want to assign lambda to a variable then we can use below
print((lambda x,y: x+y)(2,3))
# Using list comprehensions with lambda
example_list = [1,2,3,4,5]
def double(x):
    return x*2
# doubled_list = [double(x) for x in example_list] can be rewritten as
doubled_list = [(lambda x: double(x))(x) for x in example_list]
print(doubled_list)
# using map function same can be achieved
doubled_data = list(map(double,example_list)) # map returns a map object so we need to surround it with a list
print(doubled_data)
```

### Dictionary comprehension

- converting different data to dictionaries example below

```python
user_data = [
    (0,'alpha','dev'),
    (1,'bravo','qa'),
    (2,'charlie','prod'),
    (3,'delta','dev')
]
user_name_map = {user[1]: user for user in user_data} # splitting a tuple list to dictionary
print(user_name_map)
users_details = [
    ('alpha','alpha01'),
    ('beta','beta01')
]
username_map = {user[0]: user for user in users_details} # splitting a tuple list to dictionary
username = input("enter username:")
password = input("enter password:")
user_info = username_map[username]
if user_info[0] == username and user_info[1] == password:
    print("login successful")
else:
    print("login failed")
```

### Unpacking arguments

- Python allows to send n number of arguments with out knowing how many are being sent really
- Few examples are shown below

```python

def dynamic_arguments(*args):
    print(len(args))
dynamic_arguments('alpha','bravo','charlie','delta')

def add(x,y):
    return x+y
nums = {'x':10,'y':25}
print(add(x=nums['x'],y=nums['y']))
# The above can be written as
print(add(**nums))
def multiply(*args):
    total = 1
    for i in args:
        total *= i
    return total
print(multiply(1,2,3,4,5))

# We should always call this with a named argument operator else this will not work
def operations(*args, operator):
    if operator == '+':
        return sum(args)
    elif operator == '-':
        return args[0] - sum(args[1:])
    elif operator == '*':
        return multiply(*args)

print(operations(1,2,3,4,5,operator='-'))
```

### Unpacking keyword Arguments

- Function paramater preceding with \* will accept any number of arguments and will be unpacked into a tuple.
- Function paramater preceding with \*\* will accept any number of keyword arguments and will be unpacked into a dictionary.
- Function paramater preceding with \* and \*\* will accept any number of arguments and will be unpacked into a tuple and a dictionary.

```python
# Function paramater preceding with * will accept any number of arguments
# and will be unpacked into a tuple.
def dynamic_arguments(*args):
    print(len(args))
    for arg in args:
        print(arg)
dynamic_arguments('alpha','bravo','charlie','delta')
# Function paramater preceding with ** will accept any number of keyword arguments
# and will be unpacked into a dictionary.
def dynamic_keyword_arguments(**kwargs):
    print(len(kwargs))
    print(kwargs)
    for key, value in kwargs.items():
        print(key, value)
dynamic_keyword_arguments(alpha='01',bravo='02',charlie='03',delta='04')
# Function paramater preceding with * and ** will accept any number of arguments
# and will be unpacked into a tuple and a dictionary.
def dynamic_arguments_and_keyword_arguments(*args, **kwargs):
    print(len(args))
    print(args)
    print(len(kwargs))
    print(kwargs)
    for arg in args:
        print(arg)  # unpacked into a tuple
    for key, value in kwargs.items():
        print(key, value)
dynamic_arguments_and_keyword_arguments('alpha','bravo','charlie','delta',alpha='01',bravo='02',charlie='03',delta='04')
```
### Object oriented programming
- Treating code like real world objects and extracting methods to perform operations on it.
- Create a class using the class keyword.
- Every class in python has a default method called as `__init__` which will be run while instantiating a object of class.
- init method takes `self` as default input parameter.
- Any properties can be created inside init method and used across class.
- Any behavior can be extracted by defining new methods.
As sample class can be defined as below
```python
class Student:
    def __init__(self):
        self.name ="dexter"
        self.standard =12
        self.marks=[89,86,84,96,90]
    
    def average(self):
        return sum(self.marks)/len(self.marks)
```
Average method can be called in two ways:
```python
student = Student()
print(Student.average(student))
print(student.average())
```
- a class cna also be created with init method accepting parameters an example is present below
**Magic methods**
**str**
- an str method is used to print the class in a string format.
- Generally used to print in a file
- Signature of str method ```def __str__(self):```
**repr**
- an repr method is used to print the class in a string format.
- Generally used to print in console while debugging
- Signature of str method ```def __repr__(self):```
- If both repr and str method is present only str method will be invoked.

```python
class Student:
    def __init__(self,name,standard,marks):
        self.name =name
        self.standard =standard
        self.marks = marks
    def average(self):
        return sum(self.marks)/len(self.marks)
    def __str__(self):
        return f"{self.name} is {self.standard}th std and has average {self.average()}"
    def __repr__(self):
        return f"{self.name} is {self.standard}th std and has average {self.average()}"

student = Student("dexter",12,[89,86,84,96,90])
print(Student.average(student))
print(student.average())

# Once after creating str method when we call the student class it will print the return of str method
print(student)

# If str function is not present and a repr method is present it will return the return of repr method
# repr is generally used to print the object in the console
# str is used for printing the object in the file
```