# File handling

"""pygame is a cross-platform set of python modules designed for writing video games."""

""" Open function is a built in function in python which is used to interact with the flat files in all the operating systems


r   - open the file in read mode
w   - open the file in write mode
a   - open the file in append mode
r+  - open the file in read and write mode
w+  - open the file in write and read mode
a+  - open the file in append and read mode
rb  - open the file in read binary mode
wb  - open the file in write binary mode
ab  - open the file in append binary mode
"""

#Read file

infile = open(r"C:\Users\divya\Desktop\TestData\1.txt.txt")

x= infile.read()
print(x)
print(infile.tell())
print(infile.seek(0,0))   #this looks interesting function

print(infile.readlines())


#Write file(r"C:\Users\divya\Desktop\TestData\5.txt", "w")
outfile = open(r"C:\Users\divya\Desktop\TestData\2.txt", "w")          #created a new file 2.txt
outfile.closed

outfile = open(r"C:\Users\divya\Desktop\TestData\4.txt", "w")
outfile.write("This is line number 1 \n this is line number 2 \n this is line number 3")
outfile.flush()
outfile.closed

with open(r"C:\Users\divya\Desktop\TestData\5.txt", "w") as file:
    file.write("this is some data that needs to be added in file. Always read and write. Always apply what you have learned")


# write a program to write data from file 5.txt to new file name newfile.txt

infile=open(r"C:\Users\divya\Desktop\TestData\5.txt", "r")
outfile=open(r"C:\Users\divya\Desktop\TestData\newfile.txt", "w")
outfile.write(infile.read())
outfile.closed
infile.closed




