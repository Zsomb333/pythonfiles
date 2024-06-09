prompt = "Type add, show, edit or exit: "
todos = []

while True:
    user = input(prompt)
    user = user.strip()
    match user:
        case 'add':
            todo = input("Enter a todo: ")
            todo = todo.capitalize()
            todos.append(todo)

        case 'show' | 'display':

            for item in todos: #item is the individual items or strings or objects in the list which should be visible
                print(item.title())
        case 'exit':
            break
        case 'edit': #to edit the list items
            print("Got it!")
            number = int(input("number of the todo to edit: ")) # int is for converting the string which can be a string letter or number..int() coonverts the string to integer
            number = number - 1
            new_todo = input(" Edit the todo ")
            todos[number] = new_todo #this todos[] is a indexing....anything in the list gets a index starts from 0....to access it we use todos[indexnumber]



        case _:
            print("likhna sikhle")
print("Bye!")
