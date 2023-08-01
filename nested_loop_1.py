def word_count(sent):
    w = 0
    l = 0
    d = 0
    for word in sent.split():
        w = w + 1
        for letter in word:
            o = ord(letter)
            if o >=48 and o <= 57:
                d = d +1
            elif (o >=65 and o<=91) or (o >=97 and o <= 122):
                l = l + 1
    return w,l,d



if __name__ == "__main__":
    sentence= input("Enter a sentence:")
    w_c,l_c,d_c= word_count(sentence)
    print(w_c,l_c,d_c)


