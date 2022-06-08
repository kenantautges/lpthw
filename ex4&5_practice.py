car_make = 'Mazda'
car_model = '3 Series'
car_color = 'Dark Blue'
car_mpg_hwy = 37
car_mpg_city = 29
car_mpg_avg = (car_mpg_hwy + car_mpg_city) / 2

print(f'The car I would like to purchase is a {car_make} {car_model}')
print(f'I prefer the car in {car_color}')
print(f'The specs for highway fuel economy is {car_mpg_hwy} mpg and city is {car_mpg_city} mpg.')
print(f'But, I mostly care about the average fuel economy, which, by my calculations, is ~{car_mpg_avg} mpg')