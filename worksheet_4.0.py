my_string = "John Von Neumann developed merge sort algorithm in the year 1945"
count=0
for letter in my_string:
    if letter == " ":
        count = count+1
print(count)