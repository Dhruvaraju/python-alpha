user_data = [
    (0,'alpha','dev'),
    (1,'bravo','qa'),
    (2,'charlie','prod'),
    (3,'delta','dev')
]
user_name_map = {user[1]: user for user in user_data} # splitting a tuple list to dictionary
print(user_name_map)
users_details = [
    ('alpha','alpha01'),
    ('beta','beta01')
]
username_map = {user[0]: user for user in users_details} # splitting a tuple list to dictionary
username = input("enter username:")
password = input("enter password:")
user_info = username_map[username]
if user_info[0] == username and user_info[1] == password:
    print("login successful")
else:
    print("login failed")