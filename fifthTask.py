a = input()
digits = ""
for x in a:
    if x.isdigit():
        digits += x

if digits:
    print(digits)
else:
    print(0)