def split_word(word):
    index = word.find('a')
    if index != -1:
        first_part = word[:index+1]
        second_part = word[index+1:]
        return first_part, second_part
    else:
        return word, ''


word = input("Your word: ")


first_part, second_part = split_word(word)


print(first_part)
print(second_part)
