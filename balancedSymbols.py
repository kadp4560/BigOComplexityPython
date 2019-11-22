from stackClass import Stack

def par_checker(str_symbol):
    index = 0 
    balanced = True
    stack = Stack()
    while index < len(str_symbol) and balanced:
        symbol = str_symbol[index]
        if symbol in "({[" :
            stack.push(symbol)
        else:
            if stack.is_empty():
                balanced = False
            else:
                top = stack.pop()
                if not matches(top, symbol):
                    balanced = False
        print("symbol",symbol,"balanced",balanced)
        index = index + 1

    return balanced and stack.is_empty()

def matches(open, close):
    opens = "([{"
    closes = ")]}" 
    return opens.index(open) == closes.index(close)


print(par_checker('{{([][])}()}'))
