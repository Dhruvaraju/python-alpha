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