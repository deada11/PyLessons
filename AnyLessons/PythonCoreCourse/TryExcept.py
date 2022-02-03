fruits = ["apple", "cherry", "banana", "kiwi", "lemon", "pear", "peach", "avocado"]
# your code goes here
try:
    num = int(input())
    print(fruits[num])
except (IndexError, ValueError):
    print("Wrong number")

# print(fruits[num] if 0 <= num <= 7 else "Wrong number")

