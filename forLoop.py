'''
Store monthly expances of a store in a list  and find out the total of all months
'''

expenses = [10000, 20000, 11500, 12000, 15000]
# total = expenses[0] + expenses[2] #traditional way

total = 0
for item in expenses:
    total = total + item
print(total)
