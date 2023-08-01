def character_follow(wd):
    new_word = ""
    new_character = ""
    for character in wd:
        if (ord(character) >= 65 and ord(character) <= 90) or (ord(character) >= 97 and ord(character) <= 122):
            new_word = new_word + chr(ord(character) + 1)
    return new_word




if __name__ == "__main__":
    word = input("Enter a word:")
    word_follow = character_follow(word)
    print(word_follow)


