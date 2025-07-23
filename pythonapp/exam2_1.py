# exam2_1.py

# 사용자로부터 두 수를 입력 받아 둘 중에서 큰 수를 출력하는 프로그램입니다.
# 조건 연산자 사용할 것!!

x  = int(input('첫 번째 정수  : '))
y  = int(input('두 번째 정수  : '))

max_value = (x if x > y else y)

print(f'{x} 과 {y} 중 큰 수는 {max_value} ')

