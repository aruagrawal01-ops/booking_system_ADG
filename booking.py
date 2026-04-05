def apply_promo(subtotal, code):
    if code == "ADG20":
        return subtotal * 0.8
    elif code == "WINTER500":
        return max(0, subtotal - 500)
    else:
        print("Invalid promo code.")
        return subtotal

def print_summary(passengers):
    print("\n_____Passenger Summary_____")
    for p in passengers:
        print(f"{p.name} | Age: {p.age} | Baggage: {p.baggage}kg")