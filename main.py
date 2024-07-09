# def add_numbers(a, b):
#     print(a + b)
#
# add_numbers(1, 2)


# Required vs Optional
# for number in range(0, 11):
#     print(number)

# for number in range(0, 11, 2):
#     print(number)

# def greet(name="World"):
#     print(f"Hello {name}!")

# greet()
# greet("Ron")


# Positional vs Keyword
# def subtract_numbers(number1, number2):
#     print(number1 - number2)
#
# subtract_numbers(number1=10, number2=5)
# subtract_numbers(number2=5, number1=10)
#
# subtract_numbers(10, 5)
# subtract_numbers(5, 10)

# *args and **kwargs
# def print_items(*args):
#     for item in args:
#         print(item)
#
# print("Hello", "my", "name", "is", "Joms")

# def multiply(*args):
#     product = 1
#     for item in args:
#         product *= item
#     print(product)
#
# multiply(1,2,3,4,5)

# def print_items(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key} == {value}")
#
# print_items(name="Mary", gender="Female", age=25)

# def sample_function(a, b=None, *args, **kwargs):
#     pass


# Don’t use mutable object in optional parameter
# def append_to_list(a, l=[]):
#     l.append(a)
#     return l
#
# print(append_to_list(1))
# print(append_to_list(2))
# print(append_to_list(3))
#
#
# def append_to_list(a, l=None):
#     l = l or []
#     l.append(a)
#     return l
#
# print(append_to_list(1))
# print(append_to_list(2))
# print(append_to_list(3))