
# * Lists and Dictionary Comprehensions

# * Basic usage: new_list = [new_item for item in list]
# * Examples:
numbers = [1,2, 3, 4, 5]
new_numbers = [n +1 for n in numbers]
print(new_numbers)

name = "Keerthi"
letters_list = [letter for letter in name]
print(letters_list)

new_range = [x *2 for x in range(1,5)]
print(new_range)

# * Conditional List Comprehensions: new_list = [new_item for item in list if test]
# * Examples:
names = ['pilot','baku', 'shiro', 'chopper', 'felix', 'miya', 'hiki']
short_names = [name for name in names if len(name) < 5]
long_names = [name.upper() for name in names if len(name) >= 5]  
print(short_names)
print(long_names)

# * Dictionary Comprehensions: new_dict = {new_key: new_value for item in list} 
# OR 
# * new_dict = {new_key: new_value for (key, value) in dict.items()} 
# AND
# * Conditional Dictionary Comprehensions: new_dict = {new_key: new_value for item in list if test}