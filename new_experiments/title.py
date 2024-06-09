prompt = "Enter a todo:"
todos = []
while True:
    todo = input(prompt)
    title = todo.title() #.title cpaitalizes the first letter of every word in teh sentence
    print(title)
    todos.append(title)
    print(todos)
