
def divide(a: int, b: int)-> float:
    return a / b

# A function to make use of other functions
# If incorrect number of parameters are passed then error will occur
# If variables causing errors are passed stack trace will be printed
def calculate(*values, operator):
    return operator(*values)

# divide function is passed as an argument making it a first class function
result = calculate(25,5,operator=divide)
print(result)

# List of friends
friends = [
    {"name": "John", "age": 30},
    {"name": "Mary", "age": 27},
    {"name": "Mark", "age": 28},
    {"name": "Jane", "age": 29}
]

# get_friend_details is passed as an argument making it a first class function
def search_friend(sequence, name, find_details):
    for friend in sequence:
        if friend["name"] == name:
            return find_details(friend)
        else:
            raise Exception("Friend not found")

def get_friend_details(friend):
    return friend["name"], friend["age"]

# Invoking get friend details as a first class function
print (search_friend(friends, "John", get_friend_details))