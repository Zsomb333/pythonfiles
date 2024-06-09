prompt = "Type add or show: "
todos = []

while True:
    todo = input(prompt)
    capital = todo.capitalize()     # capitalize capitalizes the first letter of the sentence or the word

    todos.append(capital)  #append is to edit the variable todos..todos list is being edited by todo
    print(todos)        #a string cannot be appeneded as string is tobe got from user...not to be editted
