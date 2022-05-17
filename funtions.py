def caclulate_total(exp):

    total = 0
    for i in exp:
        total = total + i
    return total


tom_exp = [100, 120, 130, 111]
joes_exp = [110, 150, 133, 113]

toms_total = caclulate_total(tom_exp)
print(toms_total)


def sum (a, b):
    print(a)
    print(b)
    total = a + b
    return total

add1=sum(b=5,a=4)
print(add1)
