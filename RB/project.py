# Creating a function that checks whether a number is prime or composite
def isPrime(n):
    if n < 0:
        return "Negative numbers are not considered"
    if n < 2:
        return "Neither prime nor composite"
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return "Composite number"
    return "Simple number"
# Testing function
try:
    a = int(input("Input integer number: "))
    print(f"{a} - {isPrime(a)}")
# If a non-integer number is entered, an error is displayed
except ValueError:
    print("Please, enter integer number!!!")
