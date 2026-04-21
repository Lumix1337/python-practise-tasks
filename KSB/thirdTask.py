text = input("Enter string: ")
words = text.split()
word_counts = {}
order = []

for word in words:
    if word not in word_counts:
        word_counts[word] = 1
        order.append(word)
    else:
        word_counts[word] += 1

for word in order:
    print(f"{word}: {word_counts[word]}")