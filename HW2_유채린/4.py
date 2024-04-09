def gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

num1 = int(input("첫 번째 수를 입력하세요: "))
num2 = int(input("두 번째 수를 입력하세요: "))

result = gcd(num1, num2)

print(result)