numbers = input('Enter numbers separated by spaces: ')

num = list(int(numbers))

#Squares 함수에 numbers 요소를 하나씩 대입
print('Squared number: [',list(map(lambda n : n**2, num)),']')
