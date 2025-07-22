# operator6.py

# 논리 연산자에 대한 예제 프로그램입니다.


score = 90  # 120

# result = 0 <= score <= 100

result = score >= 0 and score <= 100

print(result)


result = score >= 0 and score <= 100

print(result)  # True

result = score < 0 or score > 100

print(result)  # False


flag = True

result = not flag

print(result)  # False

