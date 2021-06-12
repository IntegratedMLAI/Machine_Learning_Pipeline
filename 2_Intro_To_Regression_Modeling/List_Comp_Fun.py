# Accomplish something in 4 lines of Python Code
my_list_1 = []

for i in range(10):
    if i % 2 == 0:
        my_list_1.append(i)

# Do same with 1 line using list comprehension
my_list_2 = [i for i in range(10) if i % 2 == 0]

# Store boolean state of the lists being equal
status = my_list_1 == my_list_2

# Assert equal lists with stored boolean
assert status, 'lists do not equal'

# Report boolean state of lists being equal
print(f'T/F: The lists are equal: {status}')
