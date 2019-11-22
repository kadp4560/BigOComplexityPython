from stackClass import Stack


#Write a function rev_string(my_str) that uses a stack to reverse the characters in a string.
def rev_string(reves_string):
    stack = Stack()
    for letter in reves_string:
        stack.push(letter) 
    return stack

# s = Stack()


# s.push('x')
# s.push('y')
# s.push('z')
# print("Peek: =",s.peek())
# print(s.pop())
# print(s.pop())
stack  = rev_string('roma')
while not stack.is_empty():
    print(stack.pop(),end="")




