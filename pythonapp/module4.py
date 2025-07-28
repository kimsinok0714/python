# module4.py
# 사용자 정의 모듈(mymodule) 을 테스트 하는 예제 프로그램입니다.


# import mymodule


# result = mymodule.calculate_circle_area(5)

# print(f'원의 넓이 : {result:.2f}')


from mymodule import calculate_circle_area, MAX_VALUE

result = calculate_circle_area(5)

print(f'원의 넓이 : {result:.2f}')

print(f'MAX_VALUE : {MAX_VALUE}')



