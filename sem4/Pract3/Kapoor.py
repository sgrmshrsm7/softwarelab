import re

name = input("Enter name : ")
x = re.compile(r'^([A-Z][a-z]*\s)+Kapoor')
y = x.search(name)
if y:
    print("Correct Pattern")
else:
    print("Wrong Pattern")
