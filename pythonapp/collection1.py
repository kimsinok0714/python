# collection.py

# 1. 다음 조건을 보고 회원가입을 위한 프로그램 코드를 작성 하시오.
#    - 아이디는 반드시 10자리 이상
#    - 패스워드는 반드시 8 ~ 16자리 사이
#    - 패스워드에 아이디가 포함되면 안됨
#    - 패스워드에는 다음의 특수 문자가 반드시 하나 이상 포함
#      (~, !, @, #, $, %, ^, &, *, _, ?)


# 함수 정의
def is_valid_signup(user_id, user_pwd):

    special_characters = '~!@#$%^&*_?'
    
    if len(user_id) < 10:
        return "아이디는 반드시 10자리 이상이어야 합니다."
    
    if len(user_pwd) < 8 or len(user_pwd) > 16:
        return "패스워드는 반드시 8 ~ 16자리 사이어야 합니다."
    
    if user_id in user_pwd:
        return "패스워드에 아이디가 포함되면 안됩니다."

    if not any(ch in special_characters  for ch in user_pwd):  # All False
        return "패스워드에는 다음의 특수 문자(~!@#$%^&*_?)가 반드시 하나 이상 포함되여야 합니다."
    
    return "회원가입이 성공적으로 이루어졌습니다."



# 사용자로 부터 아이디와 비밀번호를 입력 받아서 유효성을 체크합니다.

user_id =  input('아이디를 입력하세요 ')
user_pwd =  input('비밀번호를 입력하세요 ')

result = is_valid_signup(user_id, user_pwd)
print(result)
