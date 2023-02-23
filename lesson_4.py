# using strings
# 1. generate value
# 2. str()
# 3. int(str[:-1])-> last digit
# 4. for i in range(len(str)):
#         sum += int(str[i])
import struct

# using // and %
# 1. 387
#  last digit = value%10 -> value // 10 -> go to step 2

# Lists
list_1 = []

i = 0
while i < 5:
    list_1 += [i]
    i += 1


print(list_1)

# using list ()

list_2 = list('abc')
print(list_2)

list_3 = list(range(1, 11))
print(list_3)

list_4 = [2.5, 8, 'abc', 8]

for el in list_4:
    print(type(el))

# [index]
print(list_4[0])
print(list_4[-1])

# list.index(element)
print(list_4.index(8))

# list.append(element)
list_4.append([1, 2, 3])
print(list_4)

# list.insert(index, element)
list_4.insert(1, 'test')
print(list_4)

# len()
print(len(list_4))

list_copy = list_4
print(list_copy)
# list.copy()

list_copy = list_4.copy()
list_copy = list(list_4)

# list.remove(element)
list_4.remove('abc')
print(list_4)
# list.pop(index)

list_4.pop(1)
print(list_4)

list_4.pop()
print(list_4)

del list_4[0]
print(list_4)

# list.clear()
list_4.clear()
print(list_4)

print(list_3)
list_3[2] = 5
list_3[-1] = 11
print(list_3)

# list[start_index : end_index]
print(list_3[0:6])
print(list_3[:6])
print(list_3[6:10])
print(list_3[:])
start_index = 0
list_5 = list_3[start_index:6]
print(list_5)

list_3[0:6] = [0, 0, 0, 0, 0, 0]
print(list_3)
del list_3[0:6]
print(list_3)

# list.extend([list])

list_3.extend(list_5)
print(list_3)

list_3.extend([1, 2, 3, 1, 1])
print(list_3)

# list.count(element)
count_of_1 = list_3.count(1)
print(count_of_1)

print(1 in list_3)

# sorted, sort
sorted_list = sorted(list_3)
print(list_3)

for el in sorted_list:
    print(el)

list_3.sort()
print(list_3)

# reverse=True
sorted_list = sorted(list_3, reverse=True)
print(sorted_list)

# list_3.sort(reverse=True)
# print(list_3)

# reverse()
print(list_3)
list_3.reverse()
print(list_3)

str_list = ["abC", "ABc", "ab", "BC", "bcd"]
str_list.sort(key=len)
print(str_list)

even_list = list(range(2, 11, 2))
print(even_list)
# max min sum
print(max(even_list))
print(min(even_list))
print(sum(even_list))

for element in even_list:
    print(element)

for i in range(len(even_list)):
    print(even_list[i])

# tuple()
tuple_1 = ()
tuple_1 = (1,)
print(type(tuple_1))
tuple_1 = (1, 3.5, 'abc', 'bcd', 7, 8)


result = False

i = 0
while i < len(tuple_1):
    if tuple_1[i] == 'bcdhjhgvj':
        result = True
        break
    i += 1

if result:
    print("Yes")
else:
    print("No")

print(tuple_1[:3])
tuple_2 = (1, 2, 3)

tuple_3 = tuple_1 + tuple_2
print(tuple_3)

tuple_4 = tuple_1*2
print(tuple_4)

print('bcdjbjh' in tuple_1)
# tuple.index(element)
print(tuple_1.index(1))

print(tuple_1)

for el in tuple_1:
    if el == 7:
        continue
    print(el)

for el in tuple_1:
    if el == "add":
        pass
    print(el)
else:
    print("Exit without break")

print("end string")

tuple_1[0] = 6
