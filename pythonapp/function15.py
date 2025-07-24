# function15.py

# 알파벳 소문자와 숫자를 랜덤하게 조합하여 일회용 패스워드를 생성하는 프로그램을 만드세요.
# 패스워드의 길이는 6자리로 합니다. genPass()라는 함수를 작성하고 이 함수가 랜덤하게 생성된 패스워드를 반환하게 합니다.
# 모두 3개의 패스워드를 생성하여 출력하도록 합니다

# 함수 정의

import string
import random

def getPass():
    str = string.ascii_lowercase + string.digits
    password = ''

    for _ in range(6):  # _ : 변수를 사용하지 않겠다는 의미
        password += random.choice(str)

    return password

    
    
print(getPass())
print(getPass())
print(getPass())





