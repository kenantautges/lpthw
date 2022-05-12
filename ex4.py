#Exercise 4 - Variables and Names
# number of cars available
cars = 100
# number of seats in a car
space_in_a_car = 4.0
# number of drivers driving out on the road
drivers = 30
# number of passengers
passengers = 90
# subtracting two values to determine what is not available
cars_not_driven = cars - drivers
# number of cars on the rode will equal the number of drivers, common sense imho
cars_driven = drivers
# adding number of cars plus number of seats in a car to determine capacity
carpool_capacity = cars_driven + space_in_a_car
# to find the average, divide a value by another value
average_passengers_per_car = passengers / cars_driven

# prints a statement and includes the defined variable in between the text strings.
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")