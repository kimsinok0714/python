# function1.py
# 사용자 정의 함수에 대한 예제 프로그램입니다.


# 함수 정의
def hello(user_name):
    return "Hello, " + user_name


# 함수 호출
result = hello('홍길동')
print(type(result))  # str
print(result)