frequency = {}
given_data = [
    "one",
    "two",
    "three",
    "one",
    "four",
    "five",
    "seven",
    "ten",
    "seven",
    "one",
]
for word in given_data:
    count = frequency.get(word, 0)
    frequency[word] = count + 1
new_freq = frequency.items()
print(set(new_freq))