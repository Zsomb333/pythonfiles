prompt = "Type add, show or exit: "
todos = []

while True:
    user = input(prompt)
    user = user.strip()
    match user:
        case 'add':
            todo = input("Enter a todo: ")
            capital = todo.capitalize()
            todos.append(capital)

        case 'show' | 'display':

            for item in todos: #item is the individual items or strings or objects in the list which should be visible
                print(item.title())
        case 'exit':
            break
        case _:
            print("likhna sikhle")
print("Bye!")
