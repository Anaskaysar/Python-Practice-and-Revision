'''
Write a function called print_pattern that takes integer number as an argument and prints following pattern if input number is 3,
*
**
***
'''

def print_pattern(shape):
          
          for i in range(shape):
                    s = ''
                    for j in range(i+1):
                              s = s + '*'
                    print(s)

user_input = int(input("Enter The Desired Number: "))

print_pattern(user_input)