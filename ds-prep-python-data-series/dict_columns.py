# Data Set: Do Not Modify
columns = ("year", "unemployment_rate")
label_order = [
    2001, 2002, 2003, 2004, 2005,
    2006, 2007, 2008, 2009, 2010,
    2011, 2012, 2013, 2014, 2015,
    2016, 2017, 2018, 2019, 2020,
    2021
]
unemployment_rates = {
    'year': [
        2009, 2011, 2005, 2016, 2001,
        2012, 2019, 2007, 2021, 2018,
        2010, 2013, 2006, 2017, 2015,
        2014, 2008, 2004, 2003, 2020,
        2002
    ],
    'unemployment_rate': [
        8, 10, 6, 5, 5,
        9, 4, 5, 7, 4,
        11, 8, 5, 5, 6,
        7, 5, 6, 6, 4,
        6
    ]
}

# Write your code below this line:
last = {}
last['year'] = unemployment_rates['year'][-1]
last['unemployment_rate'] = unemployment_rates['unemployment_rate'][-1]
print(last)

first_five = []
for i in range(5):
  first_five.append((unemployment_rates['year'][i], unemployment_rates['unemployment_rate'][i]))
print(first_five)
is_2000 = 2000 in unemployment_rates['year']
print(is_2000)
is_2010 = 2010 in unemployment_rates['year']
print(is_2010)
recent = unemployment_rates['unemployment_rate'][unemployment_rates['year'].index(max(unemployment_rates['year']))]
print(recent)

years = set(unemployment_rates['year'])
print(years)

unemployment = []
for x in label_order:
  unemployment.append(unemployment_rates['unemployment_rate'][unemployment_rates['year'].index(x)])
print(unemployment)

max_unemp = (unemployment_rates['year'][unemployment_rates['unemployment_rate'].index(max(unemployment_rates['unemployment_rate']))], unemployment_rates['unemployment_rate'][unemployment_rates['unemployment_rate'].index(max(unemployment_rates['unemployment_rate']))])
print(max_unemp)

employment_rates = {
  'year':  [],
  'employment_rate': []
}
for i in range(len(unemployment_rates['year'])):
  employment_rates['year'].append(unemployment_rates['year'][i])
  employment_rates['employment_rate'].append(100 - unemployment_rates['unemployment_rate'][i])
print(employment_rates)

unemployment_rates_7plus = {
    'year':  [],
    'employment_rate': []
}
for i in range(len(unemployment_rates['year'])):
  if unemployment_rates['unemployment_rate'][i] >=7:
    unemployment_rates_7plus['year'].append(unemployment_rates['year'][i])
    unemployment_rates_7plus['employment_rate'].append(unemployment_rates['unemployment_rate'][i])
print(unemployment_rates_7plus)

count = {}
for i in range(len(unemployment_rates['year'])):
  if unemployment_rates['unemployment_rate'][i] in count.keys():
    count[unemployment_rates['unemployment_rate'][i]] +=1
  else:
    count[unemployment_rates['unemployment_rate'][i]] = 1

print(count)
