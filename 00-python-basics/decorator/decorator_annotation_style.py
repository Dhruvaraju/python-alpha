import functools
user = {"user_name": "John", "access_level":"guest"}

def simple_decorator(function_passed):
    @functools.wraps(function_passed)
    def secure_pwd_function():
        if user["access_level"] == "admin":
            return function_passed()
        else:
            return "Not allowed"

    return secure_pwd_function

# Because of @simple_decorator, get_admin_access will be now named as the internal function in decorator
# to avoid this we need to use functools module on the internal function
@simple_decorator
def get_admin_access():
    return "1234"

# Instead of using the below line we can use @simple_decorator on getadminaccess function
# get_admin_access = simple_decorator(get_admin_access)
# Without functools wraps name will be secure_pwd_function
print(get_admin_access.__name__)
