# string2.py
# 키보드를 사용하여 점수를 입력 받아서 출력하는 프로그램입니다.

score = int(input('점수를 입력하세요 '))

print(f'score :  {score}')
print(f'score 자료형 :  {type(score)}')  # int

line = '=' * 100

print(line)

a = 14.5

print(int(a))  # 14

num_str = '1234.567'

print(float(num_str))

print(f'num_str : {float(num_str):.2f}')


b = 'python'

print(int(num_str)) # ValueError