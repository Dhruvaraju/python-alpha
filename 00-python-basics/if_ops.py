day_of_week = input("Enter a day of the week: ").lower() # Lower function will turn string to lowercase
if day_of_week == "monday":
    print("Today is Monday")
elif day_of_week == "tuesday":
    print("Today is Tuesday")
else:
    print("Today is not Monday or Tuesday")

# in keyword is used to see if a value is present in set or list or tuple or string
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