def average_of_scores(file_name):
    f = open(file_name, "r")
    for line in f.readlines(): #should I use f.readlines or f.readline or f.read?
        for character in line:
            if ord(character) >= 97 and ord(character) <= 122 or ord(character) >= 65 and ord(character) <= 90:








if __name__ == "__main__":
    average_of_scores("In/winter_python_problems_#4.txt")
