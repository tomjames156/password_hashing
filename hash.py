import bcrypt

correct_pass = False
user_pass = b''
password = b'supersecretpassword'
salt = bcrypt.gensalt()
hashed_pass = bcrypt.hashpw(password, salt)

while not(correct_pass):
    user_pass = input("\nEnter your password: ")
    user_pass = str.encode(user_pass)

    if bcrypt.checkpw(user_pass, hashed_pass):
        correct_pass = True
        print("\nAccess Granted, Welcome back Tomi")
    else:
        print("\nSorry, Wrong Password")