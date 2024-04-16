#다음과 같이 구성되는 문자열을 구분 문자(&, =)로 분리하여
#딕셔너리로 반환하는 함수를 포함하는 프로그램을 작성하라.
#예) 문자열 'led=on&motor=off&switch=off'이고 구분 문자가 '&', '='일 때
#{'led':'on', 'motor':'off', 'switch':off'} 반환


def parse_string(input_string, delimiter1='&', delimiter2='='):
    # 입력 문자열을 delimiter1을 기준으로 분리하여 리스트로 만듭니다.
    pairs = input_string.split(delimiter1)
    print(pairs)
    # 결과를 저장할 딕셔너리를 생성합니다.
    result = {}
    # 각 쌍에 대해 반복하여 딕셔너리에 추가합니다.
    for pair in pairs:
        # 각 쌍을 delimiter2를 기준으로 분리하여 key와 value로 분리합니다.
        key, value = pair.split(delimiter2)
        # key와 value를 딕셔너리에 추가합니다.
        result[key] = value
    return result

# 예제 문자열
input_string = 'led=on&motor=off&switch=off'
# 함수 호출
result_dict = parse_string(input_string)
print(result_dict)  # 출력: {'led': 'on', 'motor': 'off', 'switch': 'off'}



