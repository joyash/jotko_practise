total = 0
while True:
  user = input()
  if user == '0':
      print("The grand total is",total)
      break
  if user.isdigit():
     user = float(user)
     total += user
     print('The totoal is now',total)
  else:
      print("That wasn't a number.")

