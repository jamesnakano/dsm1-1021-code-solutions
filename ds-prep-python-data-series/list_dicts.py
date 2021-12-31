# Data Set: Do Not Modify
columns = ("year", "unemployment_rate")
label_order = [
    2001, 2002, 2003, 2004, 2005,
    2006, 2007, 2008, 2009, 2010,
    2011, 2012, 2013, 2014, 2015,
    2016, 2017, 2018, 2019, 2020,
    2021
]
unemployment_rates = [
    {"unemployment_rate": 8, "year": 2013},
    {"unemployment_rate": 5, "year": 2006},
    {"unemployment_rate": 5, "year": 2017},
    {"unemployment_rate": 6, "year": 2015},
    {"unemployment_rate": 6, "year": 2002},
    {"unemployment_rate": 4, "year": 2019},
    {"unemployment_rate": 9, "year": 2012},
    {"unemployment_rate": 4, "year": 2018},
    {"unemployment_rate": 6, "year": 2003},
    {"unemployment_rate": 5, "year": 2007},
    {"unemployment_rate": 11, "year": 2010},
    {"unemployment_rate": 7, "year": 2014},
    {"unemployment_rate": 6, "year": 2004},
    {"unemployment_rate": 5, "year": 2016},
    {"unemployment_rate": 6, "year": 2005},
    {"unemployment_rate": 7, "year": 2021},
    {"unemployment_rate": 5, "year": 2001},
    {"unemployment_rate": 4, "year": 2020},
    {"unemployment_rate": 10, "year": 2011},
    {"unemployment_rate": 8, "year": 2009},
    {"unemployment_rate": 5, "year": 2008}
]

# Write your code below this line:
last = unemployment_rates[-1]
print(last)

first5 = []
i=0
for d in unemployment_rates:
  first5.append((d,))
  i += 1
  if i == 5:
    break
print(first5)

is2000 = False
for d in unemployment_rates:
  for k, v in d.items():
    if 2000 == k or 2000 == v:
      is2000 = True
      break
print(is2000)
is2010=False
for d in unemployment_rates:
  for k,v in d.items():
    if 2010 == k or 2010 == v:
      is2010 = True
      break
print(is2010)

max_year = 0
recent = 0
for d in unemployment_rates:
  if d['year'] > max_year:
    recent = d['unemployment_rate']
    max_year = d['year']
print(recent)

years = []
for d in unemployment_rates:
  years.append(d['year'])
years = set(years)
print(years)

unemp_rates = []
for i in label_order:
  for d in unemployment_rates:
    if d['year'] == i:
      unemp_rates.append(d['unemployment_rate'])
print(unemp_rates)

max_unemp = 0
for d in unemployment_rates:
  if d['unemployment_rate'] > max_unemp:
    max_unemp = d['unemployment_rate']
    maxunemp = d
print(maxunemp)

employment_rate = []
for d in unemployment_rates:
  dic = {'employment_rate': 100 - d['unemployment_rate'], 'year': d['year']}
  employment_rate.append(dic)
print(employment_rate)

unemployment_rates_7plus = []
for d in unemployment_rates:
  if d['unemployment_rate'] >= 7:
    unemployment_rates_7plus.append(d)
print(unemployment_rates_7plus)

count = {}
for d in unemployment_rates:
  if d['unemployment_rate'] in count.keys():
    count[d['unemployment_rate']] += 1
  else:
    count[d['unemployment_rate']] = 1
print(count)
