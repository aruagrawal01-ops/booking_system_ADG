ROUTES = {
    ("new delhi", "mumbai"): 1460,
    ("new delhi", "kolkata"): 1525,
    ("new delhi", "chennai"): 2200,
    ("new delhi", "hyderabad"): 1670,
    ("mumbai", "kolkata"): 1970,
    ("mumbai", "chennai"): 1300,
    ("mumbai", "hyderabad"): 711,
    ("kolkata", "chennai"): 1200,
    ("kolkata", "hyderabad"): 1600,
    ("chennai", "hyderabad"): 633,
}

def get_distance(source, destination):
    source = source.strip().lower()
    destination = destination.strip().lower()

    if (source, destination) in ROUTES:
        return ROUTES[(source, destination)]
    elif (destination, source) in ROUTES:
        return ROUTES[(destination, source)]
    else:
        return None