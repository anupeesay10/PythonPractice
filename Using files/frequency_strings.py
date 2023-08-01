"""
Write a program to read the file to read a file that contains multiple paragraphs.
Create an output file that contains:
1. Number of paragraphs
2. Number of sentences per paragraph.
3. Total number of alphabets
4. Total number of digits
5. Total number of punctuations (any characters that are not digits or alphabets)

"""

def read_file(file_name):
    f = open(file_name, "r")
    number_of_par = 0
    letters = 0
    digits = 0
    punctuations = 0
    sentences_per_par = 0
    for line in f.readlines():
        for paragraph in line.split("\n"):
            paragraph = paragraph.strip()
            if len(paragraph) == 0:
                continue
            number_of_par = number_of_par + 1
            for sentence in paragraph.split("."):
                sentences_per_par = sentences_per_par + 1
        for character in line:
            if (ord(character) >= 97 and ord(character) <= 122) or (ord(character) >= 65 and ord(character) <= 90):
                letters = letters + 1
            elif ord(character) >= 48 and ord(character) <= 57:
                digits = digits + 1
            else:
                punctuations = punctuations + 1
    f.close()
    return number_of_par, sentences_per_par, letters, digits, punctuations



def write_file(file_name, num_par, sent_per_par, let, dig, punct):
    f = open(file_name,"w")
    f.write("number of paragraphs, %d\n" %(num_par))
    f.write("sentences per paragraphs, %d\n" %(sent_per_par))
    f.write("number of alphabets, %d\n" %(let))
    f.write("number of digits, %d\n" %(dig))
    f.write("number of punctuations, %d\n" %(punct))
    f.close()


if __name__ == "__main__":
    in_file = "In/grealish.txt"
    out_file = "Out/grealish.csv"
    n,s,l,d,p = read_file(in_file)
    write_file(out_file, n,s,l,d,p)



