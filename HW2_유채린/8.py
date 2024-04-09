days = {
    'January': 31, 'February': 28, 'March': 31, 'April': 30, 
    'May': 31, 'June': 30, 'July': 31, 'August': 31,
    'September': 30, 'October': 31, 'November': 30, 
    'December': 31
}

user_input = input("월을 입력하세요: ")

if user_input in days:
    print(f"{user_input}은(는) {days[user_input]}일까지 있습니다.")
else:
    print("입력한 월이 잘못되었습니다.")
