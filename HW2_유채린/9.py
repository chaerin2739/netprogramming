d = [
    {'name': 'Todd', 'phone': '555-1414', 'email': 'todd@mail.net'},
    {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
    {'name': 'Princess', 'phone': '555-3141', 'email': ''},
    {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@mail.net'}
]

# 전화번호가 8로 끝나는 사용자 이름 출력
for user in d:
    if user['phone'].endswith('8'):
        print(user['name'])

# 이메일이 없는 사용자 이름을 출력하라.
for user in d:
    if not user['email']:
        print(user['name'])


# 사용자 이름을 입력하면 전화번호, 이메일을 출력하라. 이름이 없으면 '이름이
#없습니다'라는 메시지를 출력하라

def find_user_info(name):
    for user in d:
        if user['name'] == name:
            phone = user['phone']
            email = user['email']
            if email:
                print(f"전화번호: {phone}, 이메일: {email}")
            else:
                print(f"전화번호: {phone}, 이메일: 이메일 정보가 없습니다")
            return
    print("이름이 없습니다")

user_name = input("사용자 이름을 입력하세요: ")
find_user_info(user_name)