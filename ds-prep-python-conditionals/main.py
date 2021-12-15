day_of_week = 'tuesday'
if day_of_week in ('Saturday', 'Sunday'):
  print('Have a good weekend!')
else:
  print("It's a weekday!")
student_1_score = 77
if student_1_score >= 70:
  pass_or_fail = 'You passed!'
else:
  pass_or_fail = "You failed!"
print(student_1_score, pass_or_fail)
student_2_score = 110
if student_2_score < 60:
  letter_grade = 'F'
elif 70 > student_2_score >= 60:
  letter_grade = 'D'
elif 80 > student_2_score >=70:
  letter_grade = 'C'
elif 90 > student_2_score >= 80:
  letter_grade = 'B'
elif 100 > student_2_score >= 90:
  letter_grade = 'A'
elif student_2_score >= 100:
  letter_grade = 'A+'
print(student_2_score, letter_grade)

def get_season_info(x):
  if x == 'summer':
    return("Statistically, it's likely to be hotter today than in 6 months from now. Don't sweat it, though.")
  elif x =='spring':
    return("The flowers are blooming while it's spring, but that correlation, not causation")
  elif x =='autumn':
    return("The leaves seem to regress to warmer colors as autumn approaches its end.")
  elif x =='winter':
    return("There may only be a high likelihood of it being cold today, but there's a 100 percent chance of me wanting that sweater.")
  else:
    return("That's not a season. Most likely.")
print(get_season_info("summer"))
print(get_season_info("spring"))
print(get_season_info("autumn"))
print(get_season_info("winter"))

age = 42
print('adult') if age >= 18 else print('child')
