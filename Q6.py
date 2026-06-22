psw = "python123"
c = 0
while True:
    password = input("Enter the password: ")
    if password == psw:
        print("Access granted")
        break
    else:
        c = c + 1
        print("Access denied. Try again.")
        if c == 3:
            print("Account locked.")
            break