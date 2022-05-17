f = open("E:/Python Exercise/poem.txt","r")

#print(f.read())

for line in f:
          tokens = line.split(" ")
          print(tokens)
          
f.close()         