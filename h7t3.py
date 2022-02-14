text = input('Enter some text: ')

letters = {}

for letter in text:
    if letter.isalpha():
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1

for letter in letters:
    print(letter, ' - ', letters[letter])
