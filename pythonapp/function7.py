# function7.py
# 디폴트 인수

# 함수 정의
def greet(name, msg = 'Good morning'):
    print(f'{msg}, {name}')


# 함수 호출
greet('철수', '좋은 아침')
greet('철수')


