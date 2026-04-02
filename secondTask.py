a = input("Enter string: ")
longest = ""
current = ""

for char in a:
    if current == "" or char > current[-1]:
        current += char
    else:
        if len(current) > len(longest):
            longest = current
        current = char

if len(current) > len(longest):
    longest = current

print(longest)