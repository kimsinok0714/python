# list1.py
# 리스트에 대한 예제 프로그램입니다.
# list : collection, sequence 자료형

subject_list = ['영어' ,'수학', '사회', '과학']

print(subject_list)

print(f'subject_list 자료형 : {type(subject_list)}')   # list

print(subject_list[0])  # index

print(type(subject_list[0]))

print(subject_list[-1])

print(subject_list[3])

print(subject_list[len(subject_list) - 1])

print(f'subject_list 항목의 개수 : {len(subject_list)}')



for subject in subject_list:  # sequnece : list
    print(subject)
