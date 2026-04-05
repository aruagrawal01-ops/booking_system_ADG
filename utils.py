import random

def generate_booking_id():
    return "RB" + str(random.randint(1000, 9999))

def safe_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Value must be positive.")
                continue
            return value
        except:
            print("Invalid input. Enter a number.")

def choice_input(prompt, choices):
    while True:
        value = input(prompt)
        if value in choices:
            return value
        print("Invalid choice. Please try again.")