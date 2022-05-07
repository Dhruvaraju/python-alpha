# Boolean is a data type that can only have two values: True or False
# In python boolean will start with capital case
boolean_example = True
print(boolean_example)

hero = "Batman"
villain = "Joker"
print(hero == villain) # False
print(hero != villain) # True
# We have other comapisions like >, <, >=, <=, !=

marvel_set = {"Spider-man", "ironman","hulk"}
dc_set = {"batman", "superman", "flash", "wonder-woman"}
marvel_genesis_set = {"Spider-man","ironman","hulk"}

print(marvel_set == marvel_genesis_set) # true
print(marvel_set is marvel_genesis_set) # false
# The 'is' keyword will check the exact value with memory location hence it returns false
marvel_genesis_set = marvel_set
print(marvel_set == marvel_genesis_set) # true
# As both are the same it will return true