import math
import random


# first_name = "Mariia"
# print(hex(id(first_name)))
# first_name = "Oleg"
# print(hex(id(first_name)))
# last_name = "Oleg"
# print(hex(id(last_name)))

# object: id, type, value

# is, is not

a = 3
b = 5

print(a == b)
print(a is not b)

# a = 5
print(a is b)

# type()

print(type(a))

print(a + b)
print(a - b)
print(a * b)
print(a / b)

print(a // b)
print(a % b)
print(a**2)

print((8 - 5 + 4/3 * 2)**2)


float_value = 5.0
print(type(float_value))
print(round(float_value, 3))

# dir()
print(dir(math))
print(math.sqrt(4))

print(dir(random))
# randint
# randrange
# choice

print(random.randint(2, 7))
# from 0 to 14
print(random.randrange(15))

print(random.choice(['python', 'c++', 'c#']))



# strings

demo_string = "Python automatIOn course started"
print(demo_string.title())
print(demo_string.upper())
print(demo_string.lower())

first_name = "Mariia"
last_name = "Levytska"
#  whitespaces: " ", "\n", "\t"
full_name = "\n\t" + first_name + "\n\t" + last_name + "\t\n"
print(full_name)
# rstrip(), lstrip(), strip()

print(full_name.lstrip())
full_name = full_name.lstrip()
print(full_name)

print(full_name.rstrip())
full_name = full_name.rstrip()
print(full_name)

print(full_name.strip())
full_name = full_name.strip()
print(full_name)

number_string = "1,23 3,34 6,7"
replaced_string = number_string.replace(',', '.')
print(replaced_string)

main_string = "main this is main string main"
sub_string = "main"
print(sub_string in main_string)

# True is ALL symbols is in lower/upper
print(sub_string.islower())
print(sub_string.isupper())

print(main_string.startswith(sub_string))
print(main_string.endswith(sub_string))

# isalpha()
# only letter
print(sub_string.isalpha())

# numbers and letters
print(sub_string.isalnum())


c = '34'
b = "\u00B2"
print(b.isdecimal())
print(b.isdigit())


main_string = "abfg_gba_baa_sfgd aaa"
print(type(main_string))
print(main_string.count('aaa'))
print(main_string.index('aaa'))

print(len(main_string))
split_string = main_string.split('_')
print(split_string)
print(type(split_string))
for el in split_string:
    print(el)

# s1.join(s2)
print("".join([sub_string, " ", main_string]))

# string[index]
print(sub_string[-1])
# [n1: n2]
print(sub_string[:])

print(sub_string[::-1])


name = "Mariia"
age = 23
# Old style
print("My name is %s , age = %d" %(name, age))

# str.format
print("My name is {0}, age = {1}".format(name, age))

# f-strings

print(f"My name is {name}, age = {age}")

full_string = f"My name is {name}, age = {age}"
print(full_string)
