import time
balance = 0
def deposit(amount):
    global balance
    balance+=amount
    return balance
def inquiry():
    global balance
    return balance
def withdrawl(amount):
    global balance
    balance-=amount
    return balance
x = True
while x:
    print("enter a for deposit b for inquiry c for withdrawal e for exit the program")
    use = input("enter the operation: ")
    if use == 'a':
        amt = int(input("\nenter the amount u want to deposit: "))
        print(deposit(amt))
        time.sleep(1.5)
    elif use == 'b':
        print('\n',inquiry())
        time.sleep(1.5)
    elif use == 'c':
        amt = int(input("\nenter the amount u want to withdraw: "))
        print(withdrawl(amt))
        time.sleep(1.5)
    elif use == 'e':
        exit()
    else:
        print('\nenter a valid key for operations')
        time.sleep(1.5)