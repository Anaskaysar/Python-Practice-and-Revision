exp = [10000, 20000, 11500, 12000, 15000]
total = 0
for i in range(len(exp)):
    print("Month: ", (i + 1), "Expenses:", exp[i])
    total = total + exp[i]
print('Total Expenses: ', total)

# for in locations for loop
key_locations = 'chair'
locations = ["garage", "living room", "closet", "chair"]

for i in locations:
    if i == key_locations:
        print("Found The KEy")
        break
    else:
        print("Key Not Found")
        continue
