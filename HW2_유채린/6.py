total_sum = 0

# 1부터 1000까지의 숫자에 대해 반복합니다.
for num in range(1,1001):
    # 각 숫자를 문자열로 변환하여 각 자리수의 합을 구합니다.
    num_str = str(num)
    digit_sum = 0
    for digit_char in num_str:
        digit_sum += int(digit_char)
    
    # 전체 합에 현재 숫자의 각 자리수의 합을 더합니다.
    total_sum += digit_sum

print("1부터 1000까지의 숫자의 각 자리수의 합:", total_sum)