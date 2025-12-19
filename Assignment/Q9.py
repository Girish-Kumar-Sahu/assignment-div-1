lst = list(map(int, input('enter numbers (seprate them by space): ').split()))
lst = list(set(lst))
lst.sort()
if len(lst)>1:
    print(lst[-2])
    
