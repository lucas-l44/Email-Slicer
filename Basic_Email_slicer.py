print("This program will slice given emails.")
print("When all emails have been typed, hit enter to continue.")
lst = list()
email = "start"
while email != "":
    email = input("Please enter your email:").strip()
    if email == "":
        break
    else:
        lst.append(email)

for i in lst:
    user = i[:i.index('@'):]
    dom = i[i.index('@'):]
    print("Username:", user, " and your Domain:", dom)
