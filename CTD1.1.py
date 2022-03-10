# Hello in the first CTD
# The program is to convert from Celsius to Fahrenheit and vice versa

print ("Choose either mode")
print ("Mode 1: Celsius to Fahrenheit")
print ("Mode 2: Fahrenheit to Celsius ")

while True:
  m = int(input())
  if (m == 1 or m == 2):
    break
  else:
    print("Wrong input")

if(m == 1):
  print ("Great please enter Tempreature in Celsiuss")
  t = float(input())
  print (t, "in Celsius is = ", (t * (9 / 5)) + 32, " in Fahrenheit")
  
else:
  print ("Great please enter Tempreature in Fahrenheit")
  t = float(input())
  print (t, "in Fahrenheit is = ", (t -32) * (5/9), " in Celsius")
  
