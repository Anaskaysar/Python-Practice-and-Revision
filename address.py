book = {
          
}
book ['tom'] = {
          'name': 'tom',
          'address': 'Dagonbhuiyan,feni',
          'phone': '1836062305'           
          }
book ['jon'] = {
          'name': 'jon',
          'address': 'Noakhali,feni',
          'phone': '111111111'           
          }
book ['ron'] = {
          'name': 'ron',
          'address': 'Dhaka,bangladesh',
          'phone': '2222222222'           
          }

import json
s = json.dumps(book)
print(s)

with open("E:/Python Exercise/book.txt","w") as f:
          f.write(s)

#directory for reading the file
f = open("E:/Python Exercise/book.txt","r")
s = f.read()
print(s)

#loading json files
book=json.loads(s)
print(book)

#type check
type(book)

print(book['tom'])  #printing a whole item by name

print(book ['tom']['phone']) #printing a single entity of a item

for i in book:
      print(book[i])   #pritning all items from the json file with for loop after converting into dict.