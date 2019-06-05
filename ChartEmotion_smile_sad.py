def emoji_convert(message):
    words = message.split(" ")
    emoji = {
        ":(": "😔",
        ":)": "😁"
    }
    outprint = ""
    for word in words:
        outprint += emoji.get(word, word) + " "
    return outprint


message = input("Tell me your feeling right now>>")
print(emoji_convert(message))
