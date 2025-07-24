# function8.py

# 위치 인수 (positional augument), 키워드(keyword) 인수

# 함수 정의
def calc(x, y, z):
    print(f'x = {x}, y = {y}, z = {z}')



# 함수 호출
calc(1, 2, 3)       # positional augument

calc(y=2, z=3, x=1) # keyword augument

calc(1, z=3, y=2)  

# calc(x= 1, 2, 3)  