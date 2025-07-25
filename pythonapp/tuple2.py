
# tuple2.py
# 패킹과 언패킹에 대한 예제 프로그램입니다.

# packing
_tuple = 1, 2

print(_tuple)

print(type(_tuple))


# unpacking
a, b, c = (1, 2, 3)

print(f'a = {a}, b = {b}, c = {c}')



p = (1, 2), (3, 4)

print(p)

x, y = p

print(x)
print(y)