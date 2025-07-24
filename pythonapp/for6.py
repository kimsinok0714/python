# for5.py
# 구구단을 출력하는 프로그램을 구현하시오.

for dan in range(2, 10, 1):
    print(f'=={dan}단==', end='\t\t')
print()


for i in range(1, 10, 1):
    for j in range(2, 10, 1):
        print(f'{j} * {i} = {j * i}', end ='\t')
    print()


