import references.database
import random

def run_time_start_message():
  print('Welcome, to the the random trip advisor!')
run_time_start_message()

def random_location():
  selected_city = random.choice(references.database.list_of_cities)
  user_input = input(f'We recommend {selected_city} would you like to visit this location? y/n: ')
  while user_input != 'y':
    random_location()
    break
  else:
    print(f'Great selection! you will love {selected_city}!')
    return selected_city
resulted_city = random_location()

def random_transporation():
  selected_transportation = random.choice(references.database.list_of_transportation)
  user_input = input(f'How would you like to travel around {resulted_city} by {selected_transportation}? y/n: ')
  while user_input != 'y':
    random_transporation()
    break
  else:
    print(f'{selected_transportation} is a great way to get around the city!')
  return selected_transportation
resulted_transportation = random_transporation()

def random_dining_list():
  if resulted_city == 'charleston, South Carolina':
    selected_dining_list = references.database.list_of_dining_charleston
  elif resulted_city == 'Dallas, Texas':
    selected_dining_list = references.database.list_of_dining_dallas
  elif resulted_city == 'New York City':
    selected_dining_list = references.database.list_of_dining_nyc
  elif resulted_city == 'Santa Fe, New Mexico':
    selected_dining_list = references.database.list_of_dining_santa_fe
  elif resulted_city == 'New Orleans':
    selected_dining_list = references.database.list_of_dining_new_orleans
  elif resulted_city == 'San Antonio, Texas':
    selected_dining_list = references.database.list_of_dining_san_antonio
  return selected_dining_list
result_dining_list = random_dining_list()

def random_diner_location():
  generated_dining_location = random.choice(result_dining_list)
  user_input = input(f'For diner how would you like to eat at {generated_dining_location}? y/n: ')
  while user_input != 'y':
    random_diner_location()
    break
  else:
    print(f'{generated_dining_location}, is a great place to eat at!')
  return generated_dining_location
resulted_dining_location = random_diner_location()

