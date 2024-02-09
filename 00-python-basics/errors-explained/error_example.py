# A method with possibility of throwing an error.
def division(x, y):
    if (y == 0):
        raise ValueError("Division by zero")
    result = x / y

# Try and except block
# When value error occurs the except block will be invoked.
# If no errors else block will be executed.
# Finally will be executed in all scenarios.
# 'e' will hold the error message that is added to the error.
try:
    division(1, 0)
except ValueError as e:
    print("Error due to zero as divisor, Stack Trace:",e)
else:
    print("No error")   # This will be executed if no error is raised
finally:
    print("This will be executed no matter what", "Process completed")