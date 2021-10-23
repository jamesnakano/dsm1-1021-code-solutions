import math

bool_to_int = lambda value: int(value)
print(bool_to_int(True))

get_smaller = lambda a,b: min(a,b)
print(get_smaller(15, 13))

def cube(base):
  return base ** 3
print(cube(4))

def absolute_difference(a, b):
  return max(a,b)-min(a,b)
print(absolute_difference(14, 29))

def squared_difference(a, b):
  return (max(a, b)-min(a, b)) ** 2
print(squared_difference(4, 8))

def hours_to_minutes(hours):
  return hours * 60
print(hours_to_minutes(hours = 4))

def get_circumference(radius):
  return radius * 2 * math.pi
print(get_circumference(radius=2))

def linear_transform(x, slope, intercept):
  return slope * x + intercept
print(linear_transform(slope=-2.1, intercept=17.0, x=2.5))

def standardize(x, x_center, scale_size):
  return (x-x_center)/scale_size
print(standardize(scale_size=24.63, x=2.89, x_center=-72.813))
