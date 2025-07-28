# list16.py
# List Comprehension( 리스트 컴프리헨션)
# 기존의 리스트나 반복 가능한(iterable) 객체를 기반으로 간결하고 효율적인 리스트를 생성하는 방법입니다.
# [표현식 for 변수 in iterable if 조건식]


_list = []
for i in range(1, 11, 1):
    _list.append(i ** 2)

print(_list)


_list = [ i ** 2 for i in range(1, 11, 1)]

print(_list)

