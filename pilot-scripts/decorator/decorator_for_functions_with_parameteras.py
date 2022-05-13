import functools
user = {"user_name": "John", "access_level":"admin"}

def simple_decorator(function_passed):
    # Take *args and *kwargs as input
    @functools.wraps(function_passed)
    def secure_pwd_function(*args, **kwargs):
        if user["access_level"] == "admin":
            return function_passed(*args, **kwargs)
        else:
            return "Not allowed"

    return secure_pwd_function

@simple_decorator
def get_admin_access(department):
    if department == "IT":
        return "2345"
    else:
        return "1234"

# Call with proper values
print(get_admin_access("IT"))
