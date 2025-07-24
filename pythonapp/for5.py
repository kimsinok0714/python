# for5.py
# 구구단을 출력하는 프로그램을 구현하시오.

for i in range(2, 10, 1):
    print(f'== {i}단 ==')
    for j in range(1, 10, 1):
        print(f'{i} * {j} = {i * j}')