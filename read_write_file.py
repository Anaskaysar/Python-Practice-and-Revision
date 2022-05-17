# f = open("E:/Python Exercise/funny.txt","w")

# f.write("I am in love")  #write thorugh overwrite

# f.close()  

#write thorugh appending with prev
# f = open("E:/Python Exercise/funny.txt","a")

# f.write("\nI am in love")  

# f.close()  


f = open("E:/Python Exercise/funny.txt","r")
f_out = open("E:/Python Exercise/funny_wc.txt","w")

# print(f.read())  #reading the entire file

#reading line by line
for line in f:
          tokens = line.split(" ")
          print(len(tokens))
          #f_out.write(" wordcount: "+ str(len(tokens))+ " " + line)
f.close()
f_out.close()

