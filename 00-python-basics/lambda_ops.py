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
