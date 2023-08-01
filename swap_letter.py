def letter_swap(wd):
    s=""
    for i in range(0, len(wd) - 1, 2):
        s = s + wd[i+1] + wd[i]
    return s



if __name__ == "__main__":
    word = input("Enter a word ")
    lets_w = letter_swap(word)
    print(lets_w)