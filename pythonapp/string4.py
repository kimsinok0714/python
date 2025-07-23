# string4.py
# 문자열의 길이 (len 함수)를 구하는 예제

str = 'hello'

length = len(str)  # 파이썬에서 제공하는 내장 함수 

print(f'str 문자열의 길이 : {length}')

str1 = ' hello '

print(f'str1 문자열의 길이 : {len(str1)}')

print(f'str1 문자열의 길이 : {len(str1.strip())}')   # strip() : 공백 제거 함수