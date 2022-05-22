x = input("Enter First Number: ")
y = input("Enter Second Number: ")

try:
    z = int(x) / int(y)
except Exception as e:
    print("Exception occurred: ", e)
    z = None
print("Division is : ", z)
