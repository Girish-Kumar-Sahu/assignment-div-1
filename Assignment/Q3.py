def sol(password):
    if len(password) <= 8:
        return False

    capital = False
    lower =  False
    numeric = False
    for ch in password:
        if ch.islower():
            lower = True
        if ch.isupper:
            capital = True
        if ch.isdigit:
            numeric = True
    if lower and capital and numeric:
        return True
    else:
        return False
x = input("Enter your Password: ")
print(sol(x))