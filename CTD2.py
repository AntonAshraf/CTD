# Application on lists and loops

A = []
x=0
while True:
  x = input("insert number: ")
  if x == 'q':
    break
  A.append(int(x))

print ("Maximum = ", max(A))
print ("Minimum = ", min(A))
