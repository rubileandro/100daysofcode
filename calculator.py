def add(n1, n2):
  return n1 + n2

# Subtract
def subtract(n1, n2):
  return n1 - n2

# Multiply
def multiply(n1, n2):
  return n1 * n2

# Divide
def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  num1 = int(input('What\'s the first number?: \n'))
  for operation in operations:
    print(operation)
  should_continue = True

  while should_continue:
    operation_symbol = input('Pick an operation: ')
    num2 = int(input('What\'s the next number?: \n'))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)

  print(f'{num1} {operation_symbol} {num2} = {answer}')

  if input(f'Type "y" to continue with {answer}, or type "n" to exit.: ') == "y":
    num1 = answer 
  else:
    should_continue = False

calculator()

# Alternative 

# Addition
def add(n1, n2):
  return n1 + n2
  
# Subtraction
def sub(n1, n2):
  return n1 - n2
  
# Multiplication 
def multi(n1, n2):
  return n1 * n2

# Division
def divide(n1, n2):
  return n1 / n2

# Exponent
def exponent(n1, n2):
  return n1 ** n2

operations = {
  "+": add,
  "-": sub,
  "*": multi,
  "/": divide,
}

num1 = int(input("What's the first number?: "))
for symbol in operations:
  print(symbol)
operation_symbol = input("choose an operation from the line above: ")
num2 = int(input("What's the second number?: "))
calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")
