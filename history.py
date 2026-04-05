def save_booking(data):
    with open("history.txt", "a") as f:
        f.write(data + "\n")


def show_history():
    try:
        with open("history.txt", "r") as f:
            print("\n--- Booking History ---")
            print(f.read())
    except:
        print("No history found.")

def choice_input(prompt, choices):
    while True:
        value = input(prompt)
        if value in choices:
            return value
        print("Invalid choice. Try again.")