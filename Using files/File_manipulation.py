def read_file(file_name):
    f = open(file_name, "r")
    s = 0
    count = 0
    sum = 0
    for line in f.readlines():
        line = line.strip()
        line = int(line)
        if s < line:
            s = line
        count = count + 1
        sum = sum + line
    mean = sum / count
    f.close()
    return s,mean


def write_file(file_name, largest, mean):
    f = open(file_name,"w")
    f.write("largest, %d\n" %(largest))
    f.write("mean,%f\n" %(mean))
    f.close()


if __name__ == "__main__":
    in_file = "In/data.txt"
    out_file = "Out/data.csv"
    l,m = read_file(in_file)
    write_file(out_file,l,m)
