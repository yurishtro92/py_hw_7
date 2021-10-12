import sys
stack = []
class Stack:

    def isEmpty():
        if stack == []:
            return True
        else:
            return False

    def push(x):
        stack.append(x)
        return

    def pop():
        stack.pop()
        if stack != []:
            return stack[-1]
        else:
            return #print([])

    def peek():
        return stack[-1]

    def size():
        return len(stack)
# Stack.push(1)
# Stack.push(2)
# Stack.push(3)
# Stack.isEmpty()
# Stack.size()
# Stack.peek()
# Stack.pop()

def string_check(string):
    if len(string) % 2 != 0:
        print('Несбалансировано')
        sys.exit()
    for x in string:
        if x == '}' and stack == []:
            print('Несбалансировано')
            sys.exit()
        if x == ')' and stack == []:
            print('Несбалансировано')
            sys.exit()
        if x == ']' and stack == []:
            print('Несбалансировано')
            sys.exit()
        if x == '(' or x == '[' or x == '{':
            Stack.push(x)
        if x == ')' and Stack.peek() == '(':
            Stack.pop()
        if x == ']' and Stack.peek() == '[':
            Stack.pop()
        if x == '}' and Stack.peek() == '{':
            Stack.pop()
    if stack == []:
         print('Сбалансировано')
    else:
         print('Несбалансировано')

string_check('(((([{}]))))')
string_check('}{}')
