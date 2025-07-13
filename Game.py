print("Type 'help' to see available commands.")

car_started = False  # Track whether the car is started

while True:
    command = input("> ").lower()

    if command == "start":
        if car_started:
            print("Car is already started.")
        else:
            car_started = True
            print("Car is started.")
    elif command == "stop":
        if not car_started:
            print("Car is already stopped.")
        else:
            car_started = False
            print("Car is stopped.")

    elif command == "help":
        print("""
Available commands:
  start - to start the car
  stop  - to stop the car
  break - to quit the game
""")
    elif command == "break":
        print("Quitting the game. Goodbye! thank you for playing")
        break
    else:
        print("I don't understand that command.")