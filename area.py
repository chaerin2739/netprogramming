import math

def cir_area(n):
    area = n*n*math.pi
    return area


def cir_circum(r):
    a = r * 2 *math.pi
    return a

av=cir_area(3.5)
ab=cir_circum(3.5)

print("%4.2f" %(av))
print("%4.2f" %(ab))