# exam2_3.py

# 문자열 중앙에 있는 문자를 출력한다. 
# 짝수개의 문자를 가진 문자열은 가운데 2 개의 문자, 홀수개의 문자를 가진 문자열은 가운데 한 문자 출력
# 예) 문자열을 입력하세요 : weekday
#     가운데 문자 : k
#     문자열을 입력하세요 : mother
#     가운데 문자 : t h


str = input('문자열을 입력하세요 ').strip()

if len(str) == 0:
    print('문자열을 정확히 입력하세요')
    exit(0)

if len(str) % 2 == 0: # 짝수개의 문자를 가진 문자열
    mid =  len(str) // 2
    print(str[mid - 1 : mid + 1])
else: ## 홀수개의 문자를 가진 문자열
    mid = len(str) // 2
    print(str[mid])



