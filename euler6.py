# euler 6
# KeyJect
sumOfSq = 0
sqOfSum = 0
for i in range(1 , 101):
  sqOfSum += i
  sumOfSq += i**2
sqOfSum **= 2
temp = sqOfSum - sumOfSq
print(temp)