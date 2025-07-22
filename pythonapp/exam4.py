# exam4.py

# 초단위의 시간을 입력 받아서 몇 분 몇 초인지 계산하여 출력하세요

user_input = int(input('초단위의 시간을 입력하세요  '))

minutes = user_input // 60
seconds = user_input % 60

print(f'{user_input}초는 {minutes}분 {seconds}초 입니다.')

