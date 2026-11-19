
command = "start"
match command:
    case "start":
        print("Starting...")
    case "stop":
        print("Stopping...")
    case "pause":
        print("Paused")
    case _:
        print("Unknown command")  # _ is the default case

