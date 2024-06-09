prompt = "Type add, show or exit: "
todos = []

while True:
    user = input(prompt)
    user = user.strip()  #if teh input has a space after the ord...strip remove the space if the iundividual word
    match user:
        case 'add':
            todo = input("Enter a todo: ")
            capital = todo.capitalize()
            todos.append(capital)

        case 'show':

            for item in todos: #item is the individual items or strings or objects in the list which should be visible
                print(item.title)
        case 'exit':
            break
        case whatever:   #any shit which does not match the case
            print("unknown command detected!")
print("Bye!")
