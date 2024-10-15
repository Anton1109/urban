values_list = [32, 'hello', True]
values_dict = { 'a': 45, 'b': 'good', 'c': False}
values_list_2 = [65.65, 'bye']

def print_params (a, b, c):
    print(a, b, c)


print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 76)