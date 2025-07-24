# function14.py

# 사칙 연산을 수행하는 4개의 함수(add(), sub(), mul(), div())를 작성한다. 
# 이들 함수를 이용하여 10 + 20 * 30 을 계산해보자.

# 함수 정의
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x // y


# 10 + 20 * 30
print(add(10, mul(20, 30)))
