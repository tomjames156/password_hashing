import bcrypt

password = b'supersecretpassword'
password2 = b'supersecretpasswordt'

hashed = bcrypt.hashpw(password, bcrypt.gensalt())

if bcrypt.checkpw(password, hashed):
    print("Correct")
else:
    print("Wrong Password")

print(hashed)