# tuple1.py

_tuple = (1, 2, 3, 4, 5)

print(_tuple)

print(type(_tuple))

print(dir(_tuple))  # __iter__


print(_tuple[1])


# _tuple[1] = 20  # TypeError : 변경


# for ~ in

for i in _tuple:
    print(i)
