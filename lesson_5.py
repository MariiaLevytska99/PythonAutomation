# create set

# empty set set() or {}

first_set = set(['a', 5, 1.23])
print(type(first_set))

# {'H', 'e', 'l', 'o'}
third_set = set("Hello")
print(third_set)

empty_set = set()
print(type(empty_set))

second_set = {0, 1, 2, 3, 4, 5, 0, 0, 0, 1, 2, 3}
print(second_set)

demo_tuple_set = set((((1, 2), 3, 4),))
print(demo_tuple_set)

demo_dict_set = set({'a': 1, "b": 2})
print(demo_dict_set)

# in , not in -, |, &, ^

demo_set = {3, 8, 'a', 'b', "hello"}
element = {'a', 'b', 'c'}

if element in demo_set:
    print("The element is in set")
else:
    print("The element doesn't in set")

# set1 - set2 -> set1.difference(set2)

s1 = {1, 2, 3, 4, 5}
s2 = {2, 3, 8, 9}
s3 = s1 - s2 - {1, 2}
print(s3)
print(s1.difference(s2, {1, 2}))

# set1 | set2  -> s1.union(s2)

s3 = s1 | s2 | {1, 2, 3} | {2, 3}
print(s3)
print(s1.union(s2, {1, 2, 3}, {2, 3}))

# set1 & set2 -> set1.intersection(set2)

s3 = s1 & s2
print(s3)
print(s1.intersection(s2))


#  set1 ^ set2 -> set1.symetric_difference(set2)

s3 = s1 ^ s2
print(s3)
print(s1.symmetric_difference(s2))


# set1.issubset(set2)
print(s1.issubset(s2))

# set1.issuperset(s2)
print(s1.issuperset(s2))

# len(set)
print(len(s1))

# set.copy()
s4 = s1.copy()
print(s4)

demo_list = [5, 3, 2, 6, 8, 9, 0, 1, 2, 3]
filter_set = set(demo_list)
print(filter_set)

# set1 > set2, set1 >= set2

x = {1, 2, 3, 4}
y = {1, 2}
print(x > y)
y = {1, 2, 3, 4}
print(x >= y)

# set1 < set2, set1 <= set2

x = {1, 2, 3, 4}
y = {1, 2, 3, 4, 8, 9, 7}
print(x < y)
x = {1, 2, 3, 4, 8, 9, 7}
print(x <= y)
# ==, !=

print(x == y)
x = {1, 2, 3, 4}
print(x == y)
print(x != y)

# set.add(element)

x.add("hello")
x.add(8)
x.add(False)
x.add(8.9)
print(x)

# set.remove(element)
x.remove(4)
print(x)
# KeyError
# x.remove("abcd")
# x.remove(5)

# set.discard(elem)
x.discard(3)
x.discard(5)
print(x)

# set.pop()
print(x.pop())
print(x)

# KeyError
# y = set()
# print(y.pop())

# set.clear()
x.clear()
print(x)


# dictionary -> {key: value}

dict_1 = {}
dict_1 = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5:"Friday"}
print(dict_1)
print(dict_1[2])
dict_1 = {1: {
    "key1": "value1"
}, 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5:"Friday"}
print(dict_1[1])

key=1.3
dict_2 = dict(Monday=1, Tuesday=2, Wednesday=3, Thursday=4, Friday=5)
dict_3 = dict({1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday"})
dict_3[7] = "Sunday"
print(dict_3)
dict_3[7] = "Sun"
print(dict_3)

dict_3 = dict({1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday"})
dict_2 = dict({6: "Saturday", 7: "Sunday", 5: "Fri"})
# dict_1.update(dict_2)

dict_3.update(dict_2)
print(dict_3)

# del
print("Deleting: ")
dict_3.pop(2)
del dict_3[3]
print(dict_2)
# clear()
dict_3.clear()
print(dict_3)
# dict = {}
dict_3 = {}
print(dict_3)

# in not in
print(dict_2)
print(6 in dict_2)
print(9 not in dict_2)

# dict.get(key, optional_value)
print(dict_2.get(7))
print(dict_2.get(1, "Monday"))

hierarchical_dict = {
    1: {
        "key1": {
            "key2": "value2"
        }
    },
    2: "value2"
}

print(hierarchical_dict[1]['key1']['key2'])
print(hierarchical_dict.get(1).get('key1').get('key2'))

# dict.keys()

print(dict_2.keys())

# dict.values()
print(dict_2.values())

# dict.items()
print(list(dict_2.items()))

# dict.setdefault(key, value)
dict_2.setdefault(1, "Monday")
dict_2.setdefault(6, "Monday")
print(dict_2)

for key, value in dict_2.items():
    print(key, value)

# zip()

list_key = [1, 4, 3, 2]
list_values = ["Value1", "value4", "value3", "value2"]

generated_dict = dict(zip(list_key, list_values))
print(generated_dict)

from collections import OrderedDict
sorted_dict = OrderedDict(sorted(generated_dict.items()))
print(sorted_dict)