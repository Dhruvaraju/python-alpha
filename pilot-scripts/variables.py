# Numbers

initialPrice = 10
discount = 0.2
finalPrice = initialPrice * (1 - discount)
print(finalPrice)

# Strings
initialText = "Hello World"
finalText = initialText * 2 # when we multiple a string, it will be repeated
print("Final Text:" + finalText)

# String Formatting
message = "hello"
finalMessage = f"{message} world" # f is a string formatting operator which allows us to format strings

message01 = "This message is for {}."
message02 = message01.format("developers")
print(message02)

# User input
# The input function is used to get user input with a user prompt embedded to it.
# The input function always returns a string
user_name = input("What is your name? ")
print(f"Hello {user_name}, welcome!")

square_feet = input("Enter the square feet of the room: ")
square_feet = int(square_feet)
square_meters = square_feet / 10.8
print(f"The provided {square_feet} square feet is {square_meters} square meters.")

# we can also format numbers example below
print(f"The provided {square_feet} square feet is {square_meters:.2f} square meters with 2 decimal points.")

# Ask the user for their name. You can store this in a variable.
user_name = input("What is yourname? ")
# Then, print "Hello, NAME", where NAME is the user's name
user_message = "Hello, {}"
print(user_message.format(user_name))