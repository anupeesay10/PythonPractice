def vowel_switch(file_name):
    switch_variable = ""
    f = open(file_name, "r")
    words = []

    for line in f.readlines():
        words.append(line.strip()) #Append adds the word to the list
    for c in words[0] :
        output =  ""
        for c1 in words[1]:
            if c1 in ["a", "e", "i", "o", "u"]:
                output = output + c
            else:
                output = output + c1
        print(output)




        # if line == "hello":
        #     switch_variable = "h"
        # character = ""
        # switch_word = ""
        # if line == "goodbye":
        #     if character == "o":
        #         character = switch_variable
        #         switch_word = switch_word + character
        #         print(switch_word)




if __name__ == "__main__":
    vowel_switch("In/vowel_switch.txt")