#Writing the file content using direct write module 

# f = open("E:/Python Exercise/input.txt",'w')

# f.write("6,8\n"+"7,6\n"+"2,8\n"+"9,5\n"+"9,6\n")

# f.close()

f = open("E:/Python Exercise/input.txt",'r')

sum =0
for line in f:
          list_nums = line.split(",")
          for j in list_nums:
                    print(list_nums[j])
                    
f.close()


