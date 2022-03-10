
mylist = [6,22,10,999,76,43]

while 1:
  print(mylist)
  x = input ("enter or remove: ")
  if (x == "enter"):
    z = int(input("enter new number "))
    mylist.append(z)
  elif x == "remove":
    if len(mylist) == 5:
      print ("cannot remove, bag is at minimum capacity")
    else:
      z = int(input ("enter number to remove "))
      if z in mylist:
        mylist.remove(z)
      else:
        print("this number not found in the list")
  print("\n")
    
