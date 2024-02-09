
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