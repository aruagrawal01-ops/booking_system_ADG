TRAIN_SPEED = {
    "Superfast": 120,
    "Express": 110,
    "Fast Passenger": 90
}

def calculate_travel_time(distance, train_type):
    speed = TRAIN_SPEED[train_type]
    time = distance / speed
    return round(time, 2)