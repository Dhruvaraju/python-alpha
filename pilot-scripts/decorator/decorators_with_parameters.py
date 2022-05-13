import functools
user = {"user_name": "John", "access_level":"admin"}

def check_access_level(access_level):
    def simple_decorator(function_passed):
        @functools.wraps(function_passed)
        def secure_pwd_function():
            if user["access_level"] == access_level:
                return function_passed()
            else:
                return "Not allowed"

        return secure_pwd_function
    return simple_decorator

@check_access_level("admin")
def get_admin_access():
        return "2345"

@check_access_level("user")
def get_user_access():
        return "2345"
    
print(get_admin_access())
print(get_user_access())
