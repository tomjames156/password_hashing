import bcrypt

correct_pass = False # boolean to check whether password is correct or not
user_pass = b'' 
password = b'supersecretpassword'  # user stored plain text password
salt = bcrypt.gensalt() # generate salt for the password
hashed_pass = bcrypt.hashpw(password, salt) # get hash for the password using the salt

while not(correct_pass):
    # Keeps asking the user until they enter the correct password or the escape value
    user_pass = input("\nEnter your password or 'q' to Quit: ") # allow user to enter their password
    if(user_pass == 'q'): # break out of the loop
        print("Goodbye!")
        break
    user_pass = str.encode(user_pass) # convert the password to a byte string

    if bcrypt.checkpw(user_pass, hashed_pass): # if password entered is correct
        correct_pass = True # boolean to check password set to True and stop asking for password
        print("\nAccess Granted, Welcome back Tomi")
    else: # if password entered is not correct
        print("\nSorry, Wrong Password")