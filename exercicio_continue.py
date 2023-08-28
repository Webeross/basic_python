user_word = input("Digite uma palavra: ")
user_word = user_word.upper()

vowels = 'AEIOU'
word_without_vowels = ''

for letter in user_word:
    if letter == 'A':
        continue
    elif letter == 'E':
        continue
    elif letter == 'I':
        continue
    elif letter == 'O':
        continue
    elif letter == 'U':
        continue
    else:
        word_without_vowels += letter

print("Palavra sem vogais:", word_without_vowels)