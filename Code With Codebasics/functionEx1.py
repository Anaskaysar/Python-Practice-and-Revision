def calculate_area(base, height):
    area = 1
    area = 1 / 2 *(base * height)
    return area


base = int(input('Enter The Base  of triangle:'))
height = int(input('Enter The Height  of triangle:'))

print(calculate_area(base, height))
