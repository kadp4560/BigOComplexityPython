from stackClass import Stack

def par_checker(str_symbol):
    index = 0 
    balanced = True
    stack = Stack()
    while index < len(str_symbol) and balanced:
        symbol = str_symbol[index]
        if symbol == "(" or symbol =="[":
            stack.push(symbol)
        else:
            if stack.is_empty():
                balanced = False
            else:
                stack.pop()
        index = index + 1

    return balanced and stack.is_empty()

print(par_checker('([[]])')) 