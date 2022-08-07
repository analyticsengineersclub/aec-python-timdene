
x = 2

print(x)

print(x+5)

print(x**2)

y = 'hello'

print(y)

my_first_list = ['apple',1,'banana',2]

cal_lookup = {'apple': 95, 'banana': 105, 'orange': 45}

my_fruit_list = ['apple', 'banana', 'orange']
for f in my_fruit_list:
    print(f)

def sq_int(x):
    y = x**2
    return y


def is_even(x):
    return x % 2 == 0

def is_odd(x):
    return x % 2 == 1

x = 4
y = 5

def describe_evenness(y):
    if is_even(y):
        print("It's even!")
    elif is_odd(y):
        print("It's odd!")
    else:
        print("It's neither even nor odd")

my_first_list = ['apple',1,'banana',2]

i = 0
while i < 10:
    print(i)
    i += 1


cal_lookup = {'apple': 95, 'banana': 105, 'orange': 45}

for fruit in cal_lookup:
    print(cal_lookup[fruit])


# square or calories
my_first_list = ['apple',1,'banana',2]
cal_lookup = {'carrot': 95, 'banana': 105, 'orange': 45}

def square_or_calories(nonsensical_list):
    for item in nonsensical_list:
        if isinstance(item, int):
            print(f'{item} squared = {item**2}')
            print(f"{item =}")
        elif isinstance(item, str):
            print(f'calories in {item}: {cal_lookup.get(item)}')
        else:
            print('Not a string or an integer')

# loop dict
cal_lookup = {'apple': 95, 'banana': 105, 'orange': 45}
def dict_loop(dict):
    for i in dict:
        print(dict[i])