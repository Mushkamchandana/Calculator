from art import logo
print(logo)



def add(n1,n2):
  return n1+n2
def substract(n1,n2):
  return n1-n2
def multiply(n1,n2):
  return n1*n2
def divide(n1,n2):
  return n1/n2
def calculator():
  first =float(input("Whats the first number: "))
  
  
  dict = {'+': add,
          '-': substract,
          '*': multiply,
          '/': divide
         }
  for symbol in dict:
    print(symbol)
  continuation = True
  while continuation:
    operato = input("pick an operator")
    second = float(input("Whats  another number: "))
  
    calculation_function = dict[operato]
    answer = calculation_function(first,second)
    print(f'{first}{operato}{second} = {answer}')
    if input(f'Type y to continue calculating with {answer} and n to stop') == "y":
      first = answer
    else:
      continuation = False
      calculator()
      
calculator()