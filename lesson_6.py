def add(num1: int, num2: int):
    return num1 + num2


def add_with_defolt_value(num1, num2=5):
    return num1 + num2


result = add(2, 5)
print(result)

res_2 = add(num1=result, num2=6)
res_3 = add(num2=6, num1=3)

print(add_with_defolt_value(1, 2))
print(add_with_defolt_value(1))


def print_demo_text(text, additional=""):
    print(text)
    if additional != "":
        print(text+additional)


def custom_reserve(text: str) -> str:
    tmp_text = ""
    i = len(text) - 1
    while i >= 0:
        tmp_text += text[i]
        i -= 1
    return tmp_text


result = custom_reserve(text="demo text")
print(result)

result = custom_reserve("demo text")
print(result)

n = 3
stepin = 1

if stepin == 1:
    def to_pow(n):
        return n

else:
    if stepin == 2:
        def to_pow(n):
            return n*n

    else:
        def to_pow(n):
            return n**3

result = to_pow(1)
print(result)
result_2 = to_pow(2)
print(result_2)
result_3 = to_pow(3)
print(result_3)


def func_name(*args):
    pass


func_name(1, 2, 3, 4, 5)
func_name(1, 2, 3)
func_name()


def make_pizza(*ingridients):
    print(ingridients)


make_pizza("cheese")
make_pizza("chesese", "tomato")
make_pizza("chesese", "tomato", "peperoni")


def build_profile(**user_info):
    for key, value in user_info.items():
        print(f"{key}: {value}")


build_profile(user_name="Mariia", last_name="Levytska")
build_profile(user_name="Mariia", last_name="Levytska", age=23)


def isPalindrome(inputString: str) -> bool:
    if inputString == inputString[::-1]:
        return True
    return False


text = input("Enter text: ")

is_palindrome = isPalindrome(text)
if is_palindrome:
    print("Is palindrome")
else:
    print("Is not palindrome")


is_palindrome = isPalindrome(text)
if isPalindrome(text):
    print("Is palindrome")
else:
    print("Is not palindrome")


def swap(a, b):
    tmp = a
    a = b
    b = tmp
    return a, b

a, b = swap(3, 4)
print(a)
print(b)


def function1():
    text = "Hello world"
    def function2():
        print(text)
        def function3():
            pass
    function2()

function1()

def recursive_function():
    print("It's recursive function")
    recursive_function()

# recursive_function()

def factorial(n):
    print("Iteration")
    if n == 1:
        f = 1
    else:
        f = n*factorial(n-1)

    return f

print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(4))

n = 4
fact = 1
while n > 0:
    fact = fact*n
    n = n-1

print(fact)
