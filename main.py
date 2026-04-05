from route import get_distance
from fare import total_fare, fare_breakdown, baggage_alert
from passenger import Passenger
from utils import safe_int_input, generate_booking_id, choice_input
from booking import apply_promo, print_summary
from history import save_booking, show_history
from time_cal import calculate_travel_time


def main():
    print("_______Railway Booking System_______")

    source = input("Enter source: ")
    destination = input("Enter destination: ")

    distance = get_distance(source, destination)

    if not distance:
        print("Invalid route")
        return

    train_type = choice_input(
        "Train type (Fast Passenger / Express / Superfast): ",
        ["Fast Passenger", "Express", "Superfast"]
    )

    travel_class = choice_input(
        "Class (Sleeper / AC 3-Tier / AC 2-Tier): ",
        ["Sleeper", "AC 3-Tier", "AC 2-Tier"]
    )

    n = safe_int_input("Number of passengers: ")

    total = 0
    passengers = []

    for i in range(n):
        print(f"\nPassenger {i+1}")

        name = input("Name: ")
        age = safe_int_input("Age: ")
        baggage = safe_int_input("Baggage weight: ")

        # Create object
        p = Passenger(name, age, baggage)
        passengers.append(p)

        # Baggage alert
        baggage_alert(baggage, travel_class)

        # Fare breakdown
        breakdown = fare_breakdown(distance, age, train_type, travel_class, baggage)

        print("\n_____Fare Breakdown_____")
        for k, v in breakdown.items():
            print(f"{k}: {v}")

        fare = breakdown["Total"]
        print(f"Final Fare for {p.name}: {fare}")

        total += fare

    print("\nSubtotal:", total)

    promo = input("Enter promo code (or press Enter): ")
    if promo:
        total = apply_promo(total, promo)

    booking_id = generate_booking_id()

    travel_time = calculate_travel_time(distance, train_type)

    print("\n_______FINAL BOOKING_______")
    print("Booking ID:", booking_id)
    print("Total Amount:", round(total, 2))
    print("Estimated Travel Time:", travel_time, "hours")

    print_summary(passengers)

    save_booking(f"{booking_id} | {source}-{destination} | ₹{total}")

    choice = input("View booking history? (y/n): ")
    if choice.lower() == 'y':
        show_history()


if __name__ == "__main__":
    main()