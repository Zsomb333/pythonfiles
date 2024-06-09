menu = []
while True:
    ask = input("do you want something")
    ask = ask.strip()
    match ask:
         case 'yes':
             ans = input("enter food item!")
             menu.append(ans)
         case 'no':
             print("thora sa khale")
         case 'show':
             print("your order:")

             for item in menu:
                 print(item)

         case 'exit':
             break
         case _ :
             print("likhna sikhle")

print("byee!!!")