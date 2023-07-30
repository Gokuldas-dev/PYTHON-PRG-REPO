age = int(input("Enter Your Age : "))

if age >= 100:
  print("You are to old to sign up !!")  
elif age >= 18:
  print("You are now signed up !")
elif age <= 0:
  print("You haven't been born yet !! ") 
else:
  print("You must be 18+ to sign up") 
