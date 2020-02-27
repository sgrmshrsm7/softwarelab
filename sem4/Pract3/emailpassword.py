import re

email_re = re.compile(r'^[A-Za-z][A-Za-z0-9]*(([_]|[.]|[$])[A-Za-z]+)?[@][a-zA-Z0-9.-]+(\.[a-zA-Z]{2,4})$')
pass_re = re.compile(r'^[A-Z]([a-z]{3}|[a-z]{4})([_]|\W)(\d{2}|\d{3})$')

email = input("Enter Email : ")
x = email_re.search(email)
if x:
    print("The valid email is " + x.group())
else:
    print("Invalid")

password = input("Enter Password : " )
y = pass_re.search(password)
if y:
    print("The valid  is password is " + y.group())
else:
    print("Invalid password")
