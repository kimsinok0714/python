# function6.py


# 정수를 입력 받아서 짝수인 경우 True, 홀수인 경우는 False를 반환하는 함수를 정의해보세요 (is_even)
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


# 1 ~ 100 사이의 수 중에서 짝수만 출력해 보세요(is_even 함수 사용할 것)
# for i in range(1, 101, 1):
#     if is_even(i):
#         print(i)


# is_even 함수 사용할 것
# 프로그램 종료 : q
# 짝수인지 확인할 숫자를 입력하세요 : 2
# 2는 짝수입니다.
# 짝수인지 확인할 숫자를 입력하세요 : 5
# 2는 짝수가 아닙니다.


while True:
    answer = input('짝수인지 확인할 숫자를 입력하세요 (종료: q) ')

    if answer == 'q':
        break

    num = int(answer)

    if is_even(num):
        print(f'{num}는 짝수입니다.')
    else:
        print(f'{num}는 짝수가 아닙니다.')


