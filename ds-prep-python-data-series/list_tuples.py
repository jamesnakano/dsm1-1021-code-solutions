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
    (2005, 6),
    (2001, 5),
    (2013, 8),
    (2011, 10),
    (2017, 5),
    (2006, 5),
    (2009, 8),
    (2021, 7),
    (2002, 6),
    (2007, 5),
    (2012, 9),
    (2014, 7),
    (2003, 6),
    (2019, 4),
    (2016, 5),
    (2015, 6),
    (2018, 4),
    (2008, 5),
    (2010, 11),
    (2004, 6),
    (2020, 4)
]

# Write your code below this line:
last = unemployment_rates[-1]
print(last)

first5 = unemployment_rates[:5]
print(first5)

is2000 = False
for x in unemployment_rates:
  if 2000 in x:
    is2000 = True
    break
print(is2000)

is2010 = False
for x in unemployment_rates:
  if 2010 in x:
    is2010 = True
    break
print(is2010)

max_year = 0
recent = 0
for x in unemployment_rates:
  if x[0] > max_year:
    recent = x[1]
print(recent)

years = []
for x in unemployment_rates:
  years.append(x[0])
years = set(years)
print(years)

ordered_emp = []
for i in label_order:
  for x in unemployment_rates:
    if x[0] == i:
      ordered_emp.append(x[1])
      break
print(ordered_emp)

max_unemp = 0
maxunemp = ()
for x in unemployment_rates:
  if x[1] > max_unemp:
    max_unemp = x[1]
    maxunemp = x
print(maxunemp)

employment_rate = []
for x in unemployment_rates:
  employment_rate.append((x[0], 100-x[1]))
print(employment_rate)

unemployment_rates_7plus = []
for x in unemployment_rates:
  if x[1] >= 7:
    unemployment_rates_7plus.append(x)
print(unemployment_rates_7plus)

count = {}
for x in unemployment_rates:
  if x[1] in count.keys():
    count[x[1]] += 1
  else:
    count[x[1]] = 1
print(count)
