#Simple Login System
saved_username = "admin"
saved_password = "python123"

is_logged_in = True #It's better to be False and if login is success then will be True.

username = input("Please enter your username: ")
password = input("Please enter your password: ")
print("")

if username == saved_username and password == saved_password:
    print("Log in successful!")
    print(f"Login: {is_logged_in}")
else:
    print("Wrong username or password.")
    print(False)


#Overall 5.90