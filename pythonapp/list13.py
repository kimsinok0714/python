

menu = [['칼국수', 6000], ['비빔밥', 5500], ['돼지국밥', 7000], 
        ['돈까스', 7000], ['김밥', 2000], ['라면', 2500]]


# 1. 비빔밥과 돈까스의 가격을 출력 하시오.

# print(f'비빔밥의 가격 : {menu[1][1]}')

# print(f'돈까스의 가격 : {menu[3][1]}')

for name, price in menu:  # 언패킹
    if name == '비빔밥' or name == '돈까스':
        print(f'{name} : {price}')

print('=' * 50)

for _list in menu:  
    if _list[0] == '비빔밥' or _list[0] == '돈까스':
        print(f'{_list[0]} : {_list[1]}')


# 2. 사용자 입력으로 메뉴와 가격을 입력 받아 menu 변수에 자료를 추가하는 코드를 작성 하시오.


name, price = input('메뉴와 가격을 입력하세요.(설렁탕 10000) ').split()

menu.append([name,  int(price)])


print(menu)


