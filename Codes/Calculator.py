operator = input("Enter an Operator (+ - * /)")
number1 = float(input("Enter the 1st Number :"))
number2 = float(input("Enter the 2nd Number :"))

if operator == "+" :
  result = number1 + number2
  print(f"The result is : {result}")
elif operator == "-" :
  result = number1 - number2
  print(f"The result is : {result}")
elif operator == "*" :
  result = number1 * number2
  print(f"The result is : {result}") 
elif operator == "/":
  result = number1 / number2
  print(f"The result is : {result}") 
else :
  print("The operator is invalid !!")
