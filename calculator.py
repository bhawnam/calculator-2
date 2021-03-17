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
    new_list =[]
    
    
    for i in token[1:]:
        i = float(i)
        new_list.append(i)

    if token[0] == "q":
        print("We will exit")
        break

    elif token[0] == "+":
        result = add(new_list[0],new_list[1])
                
    elif token[0] == "-":
        result =  subtract(new_list[0], new_list[1])

    elif token[0] == "*":
        result = multiply(new_list[0],new_list[1])
        
    elif token[0] == "/":
        result = divide(new_list[0], new_list[1])
            
    elif token[0] == "square":
        result = square(new_list[0])

    elif token[0] == "cube":
        result = cube(new_list[0])

    elif token[0] == "power":
        result = power(new_list[0], new_list[1])

    elif token[0] == "mod":
        result = mod(new_list[0],new_list[1])
            
    else:
        print("Input was invalid")

    print(result)