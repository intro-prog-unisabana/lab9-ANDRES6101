from aircraft import Aircraft

def main():
    print("Enter aircraft model:")
    model = input().strip()
    plane = Aircraft(model)

    while True:
        print("Enter command (A for ascent, D for descent, X to exit):")
        command = input().strip()

        if command == "X":
            break

        parts = command.split()
        action = parts[0]
        feet = int(parts[1])

        if action == "A":
            plane.ascend(feet)
        elif action == "D":
            plane.descend(feet)

    print(f"Final altitude: {plane.altitude} feet")


if __name__ == "__main__":
    main()