passenger = (12, True, 'Bonnell, Miss. Elizabeth', 'female', 58)
print(passenger)
name = passenger[2]
age = passenger[-1]
print(name, age)
survived_and_name = passenger[1:3]
gender_age = passenger[-2:]
print(survived_and_name, gender_age)
is_female = 'female' in passenger
is_male = 'male' in passenger
print(is_female, is_male)

def get_survival_info(passenger):
  (id, survived, name, gender, age) = passenger
  new_passenger = (age, gender, survived)
  return new_passenger

print(get_survival_info(passenger))
print(get_survival_info((11, True, "Sandstrom, Miss. Marguerite Rut", "female", 4)))
print(get_survival_info((28, False, "Fortune, Mr. Charles Alexander", "male", 19)))
print(get_survival_info((51, False, "Panula, Master. Juha Niilo", "male", 7)))
