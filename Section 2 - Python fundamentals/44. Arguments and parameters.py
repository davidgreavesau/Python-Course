cars = [
    {"make": "Ford", "model": "Fiesta", "mileage": 23000, "fuel_consumed": 460},
    {"make": "Ford", "model": "Focus", "mileage": 17000, "fuel_consumed": 350},
    {"make": "Mazda", "model": "MX-5", "mileage": 49000, "fuel_consumed": 900},
    {"make": "Mini", "model": "Cooper", "mileage": 31000, "fuel_consumed": 235},
]


def calculate_mpg(car, intro):
    print(intro)
    mpg = car["mileage"] / car["fuel_consumed"]
    name = f"{car['make']} {car['model']}"

    print(f"{name} does {mpg} miles per gallon")


for c in cars:
    calculate_mpg(c,"New car")
