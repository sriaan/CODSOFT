from art import logo
def add(n1,n2):
  "adding of two numbers"
  return n1+n2

def sub(n1,n2):
  "subtracting of two numbers"
  return n1-n2

def divison(n1,n2):
  "dividing of two numbers"
  return n1/n2

def multiply(n1,n2):
  "multipling of two numbers"
  return n1*n2

operations={
  "+":add,
  "-":sub,
  "*":multiply,
  "/":divison
}


def calculator():
  print(logo)
  num1=float(input("enter the first number:"))
  for symbol in operations:
    print(symbol)
  
  operation_countinues=True
  
  
  
  while operation_countinues: 
    operation_symbol = input("Pick an operation: ") 
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    
    print(f"{num1} {operation_symbol} {num2} = {answer}")
  
  
  
    if input("Type 'y' to continue with {answer},or type 'n' to start new claculation:")=="y":
      num1=answer
    else:
      operation_countinues=False
      calculator()
  
  

calculator()
