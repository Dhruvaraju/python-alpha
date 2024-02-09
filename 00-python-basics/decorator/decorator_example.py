user = {"user_name": "John", "access_level":"guest"}

def get_admin_access():
    return "1234"

# simple_decorator function is a wrapper function also called as decorator
# Takes the function on which restriction need to be imposed.
# Inside the decorator a function with the restriction logic will be placed
def simple_decorator(function_passed):
    def secure_pwd_function():
        if user["access_level"] == "admin":
            return function_passed()
        else:
            return "Not allowed"

    return secure_pwd_function

# Name of the initial function should be initiated with call to decorator function to use it
# If initiation is not present then this will not work.
get_admin_access = simple_decorator(get_admin_access)
print(get_admin_access())
