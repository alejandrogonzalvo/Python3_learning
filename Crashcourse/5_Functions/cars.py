# !/usr/bin/python3.5


def make_car(manufacturer, model, **aditional_info):
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model 
    for key, value in aditional_info.items():
        car[key] = value
    return car
car = make_car('toyota', 'c4', color= 'black', scheduled_obsolescence= '5 years')
print(car)