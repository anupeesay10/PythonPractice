"""
Problem: Accept a paragraph from the user and find the following:
1. Number of sentences
Ex:10
2. Number of words per sentence
Ex:
Sentence number     number of words
---------------     ---------------
1                   4
2                   5
...                 ...

3. Find the largest of the numbers.txt that you find in the paragraph.
*Use minimum number of for loops possible
*Assumption: numbers.txt are not embedded into the words

"""


def number_of_sentences(par):
    sentence_count = 0
    s = 0
    for sentence in par.split("."):
        sentence_count = sentence_count + 1
        word_count = 0
        for word in sentence.split():
            word_count = word_count + 1
            num = ""
            for char in word:
                if ord(char) >= 47 and ord(char) <= 57:
                    num = num + char
                elif len(num) > 0:  #Why is this an elif statement?
                    num = int(num)
                    if s < num:
                        s = num
                    num = ""    #This resets back to line 28 correct?
            if len(num) > 0:    #Please explain why this counts for numbers.txt at the end? This is a separate if statement to line 29?
                num = int(num)
                if s < num:
                    s = num
        if len(sentence) > 0:
            print("%d \t %d" %(sentence_count,word_count))  #what does \t mean
    print(sentence_count - 1)
    print(s)


"""def number_of_words(par):
    count2 = 0
    count3 = 0
    for character in par:
        if character == " ":
            count2 = count2 +1
            count3 = count2 +1
    return count3"""


"""def number_of_words_each_sentence(par):
    sentence_number = 0
    number_of_words = 0
    for character in par:
        if character == ".":
            sentence_number = sentence_number + 1
            print(sentence_number)
    for words in par:
        for char in words:
            if char == " ":
                number_of_words = number_of_words + 1
                if char == ".":
                    break
                print(number_of_words)"""

if __name__ == "__main__":
    paragraph = input("Enter a paragraph:")
    number_of_sentences(paragraph)
    """print(pg1)"""
    """pg2 = number_of_words(paragraph)
    print(pg2)
    pg3 = number_of_words_each_sentence(paragraph)
    print(pg3)"""


