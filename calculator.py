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
    input_string = input("Enter your equation > ")
    input_equation = input_string.strip(" ")
    token = input_equation.split(' ')
    operand_list =[]
    
    
    for operand in token[1:]:
        operand = float(operand)
        operand_list.append(operand)

    if token[0] == "q":
        print("We will exit")
        break

    elif token[0] == "+":
        result = add(operand_list[0],operand_list[1])
                
    elif token[0] == "-":
        result =  subtract(operand_list[0], operand_list[1])

    elif token[0] == "*":
        result = multiply(operand_list[0],operand_list[1])
        
    elif token[0] == "/":
        result = divide(operand_list[0], operand_list[1])
            
    elif token[0] == "square":
        result = square(operand_list[0])

    elif token[0] == "cube":
        result = cube(operand_list[0])

    elif token[0] == "power":
        result = power(operand_list[0], operand_list[1])

    elif token[0] == "mod":
        result = mod(operand_list[0],operand_list[1])
            
    else:
        print("Input was invalid")

    print(result)