def reaction_path(km_per_hour):
    return km_per_hour * (3/10)

def brake_distance(km_per_hour):
    return (km_per_hour/10)**2

def stopping_distance(km_per_hour):
    return reaction_path(km_per_hour) + brake_distance(km_per_hour)

distance = stopping_distance(int(input("Enter speed in km/h: ")))

print(distance)
