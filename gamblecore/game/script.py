while True:
    command = input(">> ")
    if command.lower() == "exit":
        print("Bye!")
        break
    else:
        print(f"You typed: {command}")