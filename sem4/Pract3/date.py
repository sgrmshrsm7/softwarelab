import re

date = input("Enter date : ")
date_re = re.compile(r'(([0-2][0-9]|(3)[0-1])(/)((0)[1-9]|(1)[0-2])(/)|([0-2][0-9]|(3)[0-1])(-)((0)[1-9]|(1)[0-2])(-))(\d{2}$|\d{4}$)')
y = date_re.search(date)
if y:
    print("Correct Date Format")
else:
    print("Wrong Date Format")
