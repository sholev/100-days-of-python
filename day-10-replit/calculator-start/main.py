from replit import clear

from art import logo


def add(n1, n2):
  return n1 + n2


def subtract(n1, n2):
  return n1 - n2


def multiply(n1, n2):
  return n1 * n2


def divide(n1, n2):
  return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
  print(logo)
  num1 = float(input("First number?: "))
  for symbol in operations:
    print(symbol)

  while True:
    operation_symbol = input("Pick and operation: ")
    num2 = float(input("Next number?: "))
    result = operations[operation_symbol](num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {result}")
    if input("Continue? y/n: ") != "y":
      clear()
      calculator()
      break

    num1 = result


calculator()
