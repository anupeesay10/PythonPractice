def number_of_sentences(file_name):
    f = open(file_name, "r")
    sentence_count = 0
    s = 0
    for line in f.readlines():
        for sentence in line.split("."):
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
        # print(sentence_count - 1)
    print(s)
    real_sentence_count = sentence_count - 1
    return s,real_sentence_count
    f.close()


def write_file(file_name, largest, sentences):
    f = open(file_name,"w")
    f.write("largest, %d\n" %(largest))
    f.write("number, %d\n" %(sentences))
    f.close()


if __name__ == "__main__":
    in_file = "In/paragraph.txt"
    out_file = "Out/paragraph.csv"
    l,n = number_of_sentences(in_file)
    write_file(out_file, l, n)