a = True
b = False
# True => 1
# False => 0
print(int(a))
print(int(b))

print(bool(""))
print(bool("test string"))

first_value = 6
second_value = 9
print(first_value < second_value)
print(first_value <= second_value)
print(first_value > second_value)
print(first_value >= second_value)
print(first_value == second_value)
print(first_value != second_value)

test_str_1 = "aa"
test_str_2 = "a"

print(test_str_1 < test_str_2)
print(test_str_1 <= test_str_2)
print(test_str_1 > test_str_2)
print(test_str_1 >= test_str_2)
print(test_str_1 == test_str_2)
print(test_str_1 != test_str_2)

import datetime

first_date = datetime.datetime.now()
print(first_date)
second_date = datetime.datetime(2023, 2, 19)
print(second_date)

print(first_date < second_date)
print(first_date <= second_date)
print(first_date > second_date)
print(first_date >= second_date)
print(first_date == second_date)
print(first_date != second_date)

# and, or, not

# true true => true
# true false => false
# false true => false
# false false => false

# or
# true true => true
# true false => true
# false true => true
# false false => false

# not
# true => false
# false => true


print((7 < 10) and (6 < 9))
print((3 < 5) and (16 < 9))
print((3 == 5) or (16 == 16))
print((2 + 2 == 4) and not (2 + 2 == 5) and (2 + 2 == 2 * 2))

while True:
    x = int(input("enter value: "))
    if x < 10:
        print("Value less than 10")
    elif x == 10:
        print("Value is 10")
    else:
        print("Value bigger than 10")