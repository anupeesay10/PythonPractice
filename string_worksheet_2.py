"""my_string="Python is a high level language"
x=""
for i in my_string:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        x=x+i
print(x)""" #prints only the vowels in the sentence

"""my_string="Python is a high level language"
a=my_string[0:7]
print(a)""" #prints python

"""[-8:]""" #prints the word language

"""[-14:-9]""" #prints level

"""[17:23]""" #prints level

"""my_string="Python is a high level language"
print(my_string[17:23]==my_string[-14:-9])"""#Why does this print false?

my_string="Python is a high level language"
count=0
for i in my_string:
    count=count+1
r_string=""
for j in range(count-1,-1,-1):
    r_string=r_string+my_string[j]
print(r_string) #prints the statement backwards







