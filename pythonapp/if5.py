# if5.py
# 다중 선택 if문에 대한 예제
# 정수를 입력 받아서 양수, 음수, 0 인지를 출력하는 예제 프로그램입니다.

num = int(input('정수를 입력하세요 '))

# if num > 0:
#     print('양수')
# elif num < 0:   # num <= 0
#     print('음수')
# else:   # num == 0
#     print('0')


if num == 0:
    print('0')
elif num > 0:   # num != 0
    print('양수')
else:   # num < 0
    print('음수')

