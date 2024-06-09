menu = []

while True:
    ask = input("want something to eat?")
    ask = ask.strip()
    match ask:
        case 'yes':
            ans = input("enter the food iten: ")
            menu.append(ans)

        case 'no':
            print("thora sa khale")





        case 'show':
            print("your order: ")
            for item in menu:
                print(item)
        case 'exit':

            break
        case _:
            print("likhna sikhkle")
print("byee")