question = "Do you speak english? y/n"

print(question)
answer = input("Your answer >> ")

while True:
    if answer == "y":
        print("Ok hi!")
        break
    elif answer == "n":
        print("Im smarter than you BUAHAHA!")
        break
    else:
        print("You are entered the wrong letter")
        break