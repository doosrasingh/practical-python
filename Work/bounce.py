# bounce.py
#
# Exercise 1.5

height = 100
n = 0

for i in range(10):
    height *= (3/5) 
    n += 1
    print(n, round(height, 4))

