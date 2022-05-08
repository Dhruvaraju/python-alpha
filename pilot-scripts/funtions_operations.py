def derive_age_in_seconds():
    user_age = input("Enter your age:")
    age_in_seconds = int(user_age) *365 * 24 * 60 * 60
    print("Your age in seconds is:", age_in_seconds)

derive_age_in_seconds()

# Define global variables used in functions before the function definition
# do not use the same variable name in the function definition and the global variable

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