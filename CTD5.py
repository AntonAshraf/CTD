bag = []
bag = [10 for i in range(3)]

def userturn():
  print("\033[1;36;40m\n")
  correct_input = False
  # Get the number of bag
  while correct_input == False:
    try:
      user_bag = int(input("Select a bag: "))
      if user_bag <= 0 or user_bag > 3:
        print("Please select a bag between 1 - 3.\n")
      elif bag[user_bag-1] == 0:
        print("This bag is Empty!\n")
      else:
        correct_input = True
    except ValueError:
      print("\nPlease enter a number.")    

  user_bag -= 1;
  correct_input = False
  # Get the number of items to remove
  while correct_input == False:
    try:
      items = int(input("Select number of objects: "))
      if items < 1 or items > 5:
        print("Please select objects between 1 - 5.\n")
      elif items > bag[user_bag]:
        print("This more than what in side the bag!\n")
      else:
        bag[user_bag] = bag[user_bag]-items
        correct_input = True
    except ValueError:
      print("\nPlease enter a number.")
  
  print("You removed ", items, " from bag ", user_bag+1)
  
def computerturn():
  
  # Take what inside the bag if 5 or less
  for i in  range(3):
    if bag[i] <= 5 and bag[i] != 0:
      x = bag[i]
      bag[i] = 0
      print("The computer removed ", x, "from bag ", i+1)
      return
  #  Make the bag with 6 items if it 10 items
  for i in  range(3):
    if bag[i] == 10:
      bag[i] = bag[i]-4
      print("The computer removed 4 form bag ", i+1)
      return
  # Make the bag with 6 items to win next turn
    for i in range(3):
      if bag[i] != 0:
        x = bag[i] - 6
        if x != 0:
          bag[i] = bag[i] - x
          print("The computer removed ", x, "form bag ", i+1)
          return
  # remove at least 1 item
    for i in range(3):
      if bag[i] != 0:
        bag[i] = bag[i] - 1
        print("The computer removed 1 from bag ", i + 1)
        return 

while True:
  
  print("\033[0;37;40m")
  print(bag)
  userturn()
  if bag[0] == 0 and bag[1] == 0 and bag[2] == 0:
    print("\033[1;32;40m")
    print("Congratulations, You Won!!!")
    break
  print("\033[0;37;40m")
  print(bag)
  computerturn()
  if bag[0] == 0 and bag[1] == 0 and bag[2] == 0:
    print("\033[1;31;40m")
    print("Hard Luck, You Lose!")
    break
  print ("-----------------------------------------------------------------")
  