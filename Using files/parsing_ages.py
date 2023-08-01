def read_ages(file_name):
    f = open(file_name, "r")
    student_name = ""
    s = 0
    line_count = 0
    for line in f.readlines():
        line = line.strip()
        name,age = line.split(",")  #fields[0] is name, fields[1] is age
        print("Student name: %s" %(name), "Student's age: %s" %(age))
        s = s + int(age)
        line_count = line_count + 1
    mean = s / line_count
    return mean


if __name__ == "__main__":
    m= read_ages("In/ages.txt")
    print(m)