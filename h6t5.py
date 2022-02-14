text = input()
text_part = text.split(" ")
len_word = 0
word = ""

for elem in text_part:
    if len(elem) > len_word:
        len_word = len(elem)
        word = elem

print(word)
