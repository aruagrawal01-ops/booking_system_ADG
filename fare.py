def slab_fare(distance):
    fare = 100 

    if distance <= 100:
        fare += distance * 1.0
    elif distance <= 300:
        fare += 100 * 1.0
        fare += (distance - 100) * 0.8
    else:
        fare += 100 * 1.0
        fare += 200 * 0.8
        fare += (distance - 300) * 0.6

    return fare


def senior_discount(age, fare):
    if age > 60:
        return fare * 0.6
    return fare


def train_multiplier(train_type, fare):
    if train_type == "Fast Passenger":
        return fare * 1.0
    elif train_type == "Express":
        return fare * 1.25
    elif train_type == "Superfast":
        return fare * 1.5
    return fare


def class_multiplier(travel_class, fare):
    if travel_class == "Sleeper":
        return fare * 1.0
    elif travel_class == "AC 3-Tier":
        return fare * 1.5
    elif travel_class == "AC 2-Tier":
        return fare * 2.0
    return fare


def baggage_fee(weight, travel_class):
    limits = {
        "Sleeper": 20,
        "AC 3-Tier": 30,
        "AC 2-Tier": 40
    }

    extra = max(0, weight - limits[travel_class])
    return extra * 15

def baggage_alert(weight, travel_class):
    limits = {
        "Sleeper": 20,
        "AC 3-Tier": 30,
        "AC 2-Tier": 40
    }

    if weight > limits[travel_class]:
        print("Baggage exceeds free limit! Extra charges applied.")


def surcharge(train_type):
    if train_type == "Superfast":
        return 100
    elif train_type == "Express":
        return 50
    return 0


def total_fare(distance, age, train_type, travel_class, baggage):
    fare = slab_fare(distance)
    fare = senior_discount(age, fare)
    fare = train_multiplier(train_type, fare)
    fare = class_multiplier(travel_class, fare)
    fare += baggage_fee(baggage, travel_class)
    fare += surcharge(train_type)

    return round(fare, 2)

def fare_breakdown(distance, age, train_type, travel_class, baggage):
    breakdown = {}

    #1
    slab = slab_fare(distance)
    breakdown["Slab Fare"] = round(slab, 2)

    #2
    after_discount = senior_discount(age, slab)
    discount_value = slab - after_discount
    breakdown["Senior Discount"] = round(-discount_value, 2)

    #3
    after_train = train_multiplier(train_type, after_discount)
    train_extra = after_train - after_discount
    breakdown["Train Premium"] = round(train_extra, 2)

    #4
    after_class = class_multiplier(travel_class, after_train)
    class_extra = after_class - after_train
    breakdown["Class Premium"] = round(class_extra, 2)

    #5
    baggage_cost = baggage_fee(baggage, travel_class)
    breakdown["Baggage Fee"] = round(baggage_cost, 2)

    #6
    surcharge_cost = surcharge(train_type)
    breakdown["Surcharge"] = round(surcharge_cost, 2)

    total = (slab - discount_value + train_extra + class_extra + baggage_cost + surcharge_cost)
    breakdown["Total"] = round(total, 2)

    return breakdown