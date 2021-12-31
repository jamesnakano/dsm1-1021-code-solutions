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
    2002: 6,
    2020: 4,
    2007: 5,
    2015: 6,
    2010: 11,
    2014: 7,
    2001: 5,
    2006: 5,
    2004: 6,
    2009: 8,
    2013: 8,
    2008: 5,
    2021: 7,
    2018: 4,
    2011: 10,
    2005: 6,
    2016: 5,
    2019: 4,
    2012: 9,
    2017: 5,
    2003: 6
}

# Write your code below this line:
last = {}
last['year'] = 2003
last['unemployment_rate'] = unemployment_rates[2003]
print(last)

first5 = []
i=0
for k,v in unemployment_rates.items():
  first5.append((k,v))
  i+=1
  if i == 5:
    break
print(first5)

is2000 = 2000 in unemployment_rates.keys()
print(is2000)
is2010 = 2010 in unemployment_rates.keys()
print(is2010)

recent = unemployment_rates[max(unemployment_rates.keys())]
print(recent)

year = set(unemployment_rates.keys())
print(year)

sorted_emp = []
for x in label_order:
  sorted_emp.append(unemployment_rates[x])
print(sorted_emp)

max_unemp = max(unemployment_rates.values())
print(max_unemp)

employment_rate = {}
for k,v in unemployment_rates.items():
  employment_rate[k] = 100-v
print(employment_rate)

unemp_plus7 = {}
for k,v in unemployment_rates.items():
  if v >= 7:
    unemp_plus7[k] = v
print(unemp_plus7)

count = {}
for v in unemployment_rates.values():
  if v in count.keys():
    count[v] +=1
  else:
    count[v] = 1
print(count)
