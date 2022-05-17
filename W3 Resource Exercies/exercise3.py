'''
Write a Python program to display the current date and time.
Sample Output :
Current date and time :
2014-07-05 14:34:14
'''
import datetime #imporing datetime module
now = datetime.datetime.now() #now() function Return the current local date and time, which is defined under datetime module.
print("Current Date and Time : ")
print(now.strftime("%Y-%m-%d %H:%M:%S "))