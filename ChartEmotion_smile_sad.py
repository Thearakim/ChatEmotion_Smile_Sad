message = input("Tell me your feeling right now >>> ")
words = message.split(' ')
emoji = {
    ":)": "😊",
    ":(": "😔",
}
outprint = ''
for word in words:
    outprint += emoji.get(word, word) +' '
print(outprint)

