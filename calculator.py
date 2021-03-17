"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

# repeat forever:
 
#     tokenize input
#         if the first token is "q":
#             quit
#         else:
#             (decide which math function to call based on first token)
#             if the first token is 'pow':
#                   call the power function with the other two tokens

#             (...etc.)

while True:
    choice = input("Enter your equation > ")
    token = choice.split(' ')
    if token[0] == "q":
        print("We will exit")
        break

    elif token[0] == "+":
        result = add(token[1],token[2])
        
    elif token[0] == "-":
        result =  subtract(token[1], token[2])

    elif token[0] == "*":
        result = multiply(token[1],token[2])
   
    elif token[0] == "/":
        result = divide(token[1], token[2])
    
    elif token[0] == "square":
        result = square(token[1])

    elif token[0] == "cube":
        result = cube(token[1])

    elif token[0] == "power":
        result = power(token[1], token[2])

    elif token[0] == "mod":
        result = mod(token[1],token[2])
#
    else:
        print(result)