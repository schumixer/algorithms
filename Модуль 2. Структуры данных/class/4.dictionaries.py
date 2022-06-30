# my_dict = {"name": "John", "age": 30, "city": "New York"}
# print(my_dict["name"])
# my_dict["weight"] = 78
# my_dict["name"] = "Jane"
# print(my_dict)
# for key, value in my_dict.items():
#     print(key, value)
# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.items())
#########################################################################
# string = "hello world"


# def get_number_of_letters(string):
#     result = {}
#     for char in string:
#         if char in result:
#             result[char] += 1
#         else:
#             result[char] = 1
#     return result


# print(get_number_of_letters(string))
#########################################################################
classes = {
    "class1": ["John", "Jane", "Mary"],
    "class2": ["Bob", "Mary", "Jane"],
    "class3": ["Ivan", "Peter", "Jane"],
}
# for key, val in classes.items():
#     print(key, val)
#     for name in val:
#         print(name)
# How many times each name appears in the classes?
# def get_names_count(classes: dict) -> dict:
#     result = {}
#     for key, val in classes.items():
#         for name in val:
#             if name in result:
#                 result[name] += 1
#             else:
#                 result[name] = 1
#     return result


# print(get_names_count(classes))
#########################################################################
# employees = {
#     "employee1": {"name": "John", "age": 30, "city": "New York", "salary": 1000},
#     "employee2": {"name": "Jane", "age": 25, "city": "London", "salary": 2000},
#     "employee3": {"name": "Mary", "age": 28, "city": "Paris", "salary": 10000},
# }
# # Get the total salary of all employees
# def get_total_salary(employees: dict) -> int:
#     result = 0
#     for key, val in employees.items():
#         result += val["salary"]
#     return result


# print(get_total_salary(employees))
#########################################################################
# employees = {
#     "employee1": {"name": "John", "age": 30, "city": "New York", "salary": 1000},
#     "employee2": {"name": "Jane", "age": 25, "city": "London", "salary": 2000},
#     "employee3": {"name": "Mary", "age": 28, "city": "Paris"},
# }
# # Get the total salary of all employees
# def get_total_salary(employees: dict) -> int:
#     result = 0
#     for key, val in employees.items():
#         result += val.get("salary", 0)
#     return result


# print(get_total_salary(employees))
#########################################################################
input_snake_case_dict = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 30,
    "company_address_name": "123 Main St",
    "user_info": {"user_name": "johndoe", "password": "123456"},
}
# Convert snake_case to camelCase dictionary
# def snake_case_to_camel_case(input_snake_case_dict: dict) -> dict:
#     result = {}
#     for key, val in input_snake_case_dict.items():
#         title_case = key.title().replace("_", "")
#         result[key[0] + title_case[1:]] = val
#     return result
# Convert snake case string to camel case string
def snake_case_to_camel_case(input_snake_case_str: str) -> str:
    title_case = input_snake_case_str.title().replace("_", "")
    return input_snake_case_str[0] + title_case[1:]


def nested_snake_case_to_camel_case(input_snake_case_dict: dict) -> dict:
    result = {}
    for key, val in input_snake_case_dict.items():
        new_key = snake_case_to_camel_case(key)
        if isinstance(val, dict):
            result[new_key] = nested_snake_case_to_camel_case(val)
        else:
            result[new_key] = val
    return result


print(nested_snake_case_to_camel_case(input_snake_case_dict))
# print("hello__world".title())
