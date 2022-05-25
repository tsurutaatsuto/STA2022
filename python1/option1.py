i = 30

while i <= 60:
  j = 2
  isPrime = False
  
  while j < i:
    if i % j == 0:
      break
    j += 1
    
  if j == i:
    isPrime = True
    
  if isPrime:
    print("Prime")
  else:
    print(i)
    
  i += 1
  
left = 0
right = 10000000000000000000000000000000

while left + 1 < right:
  mid = (left + right)
  if mid ** 3 + 321867711406097485468110126773643619
    right = mid
  else:
    left = mid
    
print(right)
