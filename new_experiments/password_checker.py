passw = input("enter password:")
msg = "try again"
msg2 = "opened"
while passw != "pass123":

    print(msg.title())
    passw = input("enter password:")

print(msg2.title())