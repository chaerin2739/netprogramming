days = {
    'January': 31, 'February': 28, 'March': 31, 'April': 30, 
    'May': 31, 'June': 30, 'July': 31, 'August': 31,
    'September': 30, 'October': 31, 'November': 30, 
    'December': 31
}

user_input = input("월을 입력하세요: ")

if user_input in days:
    print(f"{user_input}은(는) {days[user_input]}일까지 있습니다.")


for month, day in days.items():
    if day == 31 :
        print(month)


# 월을 알파벳 순서대로 정렬하여 리스트에 저장합니다.
sorted_months = sorted(days.keys())

# 정렬된 월을 순서대로 출력합니다.
for month in sorted_months:
    print(month)



# 일수를 기준으로 오름차순으로 정렬된 (key, value) 튜플 리스트를 생성합니다.
sorted_days = sorted(days.items(), key=lambda x: x[1])

# 정렬된 (key, value) 튜플 리스트를 순서대로 출력합니다.
for month, day in sorted_days:
    print(f"{month}: {day}")



# 사용자로부터 3자리 월 약어를 입력받습니다.
user_input = input("월의 3자리 약어를 입력하세요: ").capitalize()

# 입력된 약어에 해당하는 월이 있는지 확인하고, 있다면 해당 월의 일수를 출력합니다.
if user_input in days:
    month = user_input
    days_in_month = days[month]
    print(f"{month}의 일수는 {days_in_month}일 입니다.")
else:
    print("올바른 월의 3자리 약어를 입력하세요.")