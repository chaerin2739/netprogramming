total_sum = 0

for num in range(1, 1001):
    num_str = str(num)
    digit_sum = sum(int(digit) for digit in num_str)
    total_sum += digit_sum

print("1부터 1000까지의 숫자의 각 자리수의 합:", total_sum)
