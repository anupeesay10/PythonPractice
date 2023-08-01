"""def reverse_word(my_str):
    reverse_sentence = ""
    word = ""
    count = 0
    for letter in my_str:
        if letter == " ":
            count = count + 1
            if count % 1 == 0:
                print(word)
                for i in range(len(word)-1,-1,-1):
                    reverse_sentence = word[i]
            else:
                reverse_sentence = word + letter
    return reverse_sentence"""


def reverse_word1(my_s):
    rev = ""
    for word in my_s.split(" "):
        for character in word:
            rev = character + rev
        print(rev, end = " ")
        rev = ""
        # for i in range(len(word)-1,-1,-1):
        #     rev = rev + word[i]
    return rev


if __name__ == "__main__":
    my_string = input("Enter a sentence:")
    m_s_ = reverse_word1(my_string)
    print(m_s_)

