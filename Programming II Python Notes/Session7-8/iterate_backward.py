text = "abcdefghijklmnop"

for letter in text:
    print(letter)

i = 0
while i < len(text)-1:
    print(text[i])
    i += 1

i = len(text) -1
while i >= 0:
    print(text[i], end="")
    i -= 1

print()
i = 0
while i < len(text):
    print(text[len(text)-i-1], end="")
    i += 1