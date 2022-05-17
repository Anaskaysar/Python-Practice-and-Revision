def calculate_area(base, height,shape):
          if shape == 'traingle':
                    area = 1
                    area = 1 / 2 *(base * height)
                    return area
          elif shape == 'rectangle':
                    area = base*height

dim1 = int(input('Enter The First Dimension:'))
dim2 = int(input('Enter The Height  of triangle:'))
shape = input("Enter The Shape (traingle or rectangle) : ")

print(calculate_area(dim1, dim2,shape))
