# exception1.py

# exception handling에 대한 예제 프로그램입니다.

try:
    num = int(input('하나의 숫자를 입력하세요')) # a
    print(f'num : {num}')
except Exception as err:
    print(f'err : {err}')

print('end!!')




