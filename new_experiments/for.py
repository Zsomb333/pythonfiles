meals = []
while True:

    ask = input("want something more?")
    ask = ask.strip()
    match ask:
        case 'yes':
            ans = input("do enter the food item: ")
            meals.append(ans)
        case 'no':
            print("okay!")

        case 'show':

            print("showing your meal:")
            for item in meals:
                print(item)

        case _:
            print("ans with yes o rno ")
