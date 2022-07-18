class Car():
    def __init__(self, make, model, color, year):
        self.make = make.upper()
        self.model = model.upper()
        self.color = color.upper()
        self.year = year

    def __str__(self):
        return f"<Car | {self.year} {self.make} {self.model} in {self.color}>"

    def __repr__(self):
        return f"<Car | {self.year} {self.make} {self.model} in {self.color}>"

    def __eq__(self, __o):
        return self.year == __o.year
    
    def __lt__(self, __o):
        return self.year < __o.year

    def __gt__(self, __o):
        return self.year > __o.year
    
    def __le__(self, __o):
        return self.year <= __o.year

    def __ge__(self, __o):
        return self.year >= __o.year


delorean = Car('delorean', 'dmc-12', 'gray', 1981)
vw = Car('volkswagen', 'beetle', 'yellow', 1967)    
ford = Car('Ford', 'Econoline', 'fluffy', 1984)    
lotus = Car('lotus', 'esprit', 'gray', 1990)    
mercedes = Car('mercedes-benz', '230sl', 'skyblue', 1997) 

cars = [delorean, vw, ford, lotus, mercedes]
cars.sort()
print("GUESS THE MOVIE BY CAR: ")
count = 1
for car in cars:
    
    print(f"\n{count}. {car}")
    count += 1