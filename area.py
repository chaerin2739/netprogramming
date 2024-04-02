import math

def cir_area(n):
    area = n*n*3.14
    return area


def cir_circum(r):
    a = r * 2 *3.14
    return a

av=cir_area(3.5)
ab=cir_circum(3.5)

print("%4.2f" %(av))
print("%4.2f" %(ab))