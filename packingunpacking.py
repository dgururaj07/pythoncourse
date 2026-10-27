# def greet(name, age):
#     print(f"{name} is {age} years old")

# person = {"name": "Asha", 
#           "age": 30}

# print(greet(**person))   # same as greet(name="Asha", age=30)

#Packing: separate named arguments → dictionary
def show_details_1(**details):
    print(details)

show_details_1(name="Asha", age=30, city="Chennai")
# Output: {'name': 'Asha', 'age': 30, 'city': 'Chennai'}


def show_details(**kwargs):        # packing: collects into a dict
    print(kwargs)

info = {"name": "Asha", "age": 30}
show_details(**info)               # unpacking: spreads the dict out
# Output: {'name': 'Asha', 'age': 30}