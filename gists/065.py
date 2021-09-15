# Infinite loop - termination by break
n = 0
while True:
  n += 1    
  print(n)    
  if n == 1024:        
    break

# Stop loop with break and continue 
n = 0
while n < 5:
  n += 1    
  if n == 4:
    break    
  if n == 1:
    continue
  print(n)
