data = input("Enter numbers: ").split()
numbers = [int(x) for x in data]
result = [num * 2 for num in numbers if num % 2 == 0]
print(*(result))