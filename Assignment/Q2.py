c = True
while c:    
    op = input("enter the operator that you want to perform operation with: (+,-,*,/,%): ")
    n1 = int(input('enter num1: '))
    n2 = int(input('enter num2: '))
    if op == '+':
        print(n1+n2)
    elif op == '-':
        print(n1-n2)
    elif op == '*':
        print(n1*n2)
    elif op == '/':
        print(n1/n2)
    elif op == '%':
        print(n1%n2)
    else:
        print('operator not recognized')
    c = False
    t = input('do u want to continue? y/n: ').lower()
    if t=='y':
        c = True
        