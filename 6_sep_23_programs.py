
#wap to add two numbers

a= int(input("Please enter a first number = "))
b= int(input("Please enter a second number = "))
print("Addition of two numbers = ", a+b)

#a, b = int(input("please enter your numbers= "))
#print("addition = ", a+b)



#wap to have two inputs from user seperated by space
ser_input = input("Enter two numbers separated by a space: ")

# Split the input string into two parts based on the space delimiter
inputs = ser_input.split()

print(inputs)

# Check if there are exactly two inputs
if len(inputs) == 2:
    num1 = float(inputs[0])
    num2 = float(inputs[1])

    # Now you can use num1 and num2 for further calculations
    print(f"You entered: num1={num1}, num2={num2}")
else:
    print("Please enter exactly two numbers separated by a space.")


# wap to Reverse a stringz

xyz = input("please enter the string")
reverse = xyz[::-1]
print(reverse)

reverse1 = ""
for i in xyz:
    reverse1 = i + reverse1

print(reverse1)

#wap to determine even or odd number

x = int(input("Please input a number"))
if x%2 == 0:
    print("the number is even")
else:
    print("the number is odd")


xy = [12, 23, 32, 45, 98, 78, 4, 3]

for i in xy:
    if i % 2 == 0:
        print("the number", i, "is even")
    else:
        print("the number", i, "is odd")


# wap to reverse a number

rev = input("Please input a number to reverse")

rev1 = ""
for i in rev:
    rev1= i + rev1

print("the reverse number is ", rev1)

