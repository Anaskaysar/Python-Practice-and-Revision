'''
Write a program that ask user to enter a number. Program should then tell if number is odd or even
'''
number =input("Enter a Number To check: ")
number =int(number)
if number%2==0:
    print("The number is Even")
else:
    print("Number is Odd")
