# Method 1:
f = open('file.txt')
while True:
line = f.readline()    
  if not line:        
    break    
  print(line)
  
# Method 2:
with open('file.txt') as f:    
lines = f.readlines()    
for line in lines:        
  print(line)
  
# Method 3:
with open('file.txt') as f:
  for line in f:
    print(line)
