# this is the second version of q2 with a different approach
s = input('enter the statement: ').strip()
if '+' in s:
    n1,n2 = map(int, s.split('+'))
    print(n1+n2)
elif '-' in s:
    n1,n2 = map(int, s.split('-'))
    print(n1-n2)
elif '*' in s:
    n1,n2 = map(int, s.split('*'))
    print(n1*n2)
elif '/' in s:
    n1,n2 = map(int, s.split('/'))
    print(n1/n2)
elif '%' in s:
    n1,n2 = map(int, s.split('%'))
    print(n1%n2)
else:
    print('enter a valid statement with just 2 numbers and a operator from this (+,-*/%)')