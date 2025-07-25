# if6.py

# 예) 성적이 90점 이상이면 → A학점
#          80점 이상이면 → B학점
#          70점 이상이면 → C학점
#          60점 이상이면 → D학점
#          60점 미만 → F 학점


score  = int(input('성적을 입력하세요 '))


if score >= 90:
    grade = 'A학점' 
elif score >= 80: # score < 90 and score >= 80 (80 <= score < 90)
    grade = 'B학점'
elif score >= 70: # score < 80 and score >= 70 (70 <= score < 80)
    grade = 'C학점'
elif score >= 60: # score < 70 and score >= 60 (60 <= score < 70)
    grade = 'D학점'
else: # score < 60
    grade = 'F학점'

print(f'{score} 점수는 {grade} 입니다.')



