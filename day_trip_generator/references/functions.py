import re
from tabnanny import check
import references.database
import random

def run_time_start_message():
  print('Welcome, to the the random trip advisor!')
run_time_start_message()

def random_location():
  selected_city = random.choice(references.database.list_of_cities)
  user_input = input(f'We recommend {selected_city} would you like to visit this location? y/n: ')
  while user_input != 'y':
    re_selected_city = random_location()
    return re_selected_city
  else:
    print(f'Great selection! you will love {selected_city}!')
    return selected_city
resulted_city = random_location()

def random_transporation():
  selected_transportation = random.choice(references.database.list_of_transportation)
  user_input = input(f'How would you like to travel around {resulted_city} by {selected_transportation}? y/n: ')
  while user_input != 'y':
    re_selected_transporation = random_transporation()
    return re_selected_transporation
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
    re_generated_dining_location = random_diner_location()
    return re_generated_dining_location
  else:
    print(f'{generated_dining_location}, is a great place to eat at!')
  return generated_dining_location 
resulted_dining_location = random_diner_location()

def random_attractions_list():
  if resulted_city == 'charleston, South Carolina':
    selected_attractions_list = references.database.list_of_attractions_charleston
  elif resulted_city == 'Dallas, Texas':
    selected_attractions_list = references.database.list_of_attractions_dallas
  elif resulted_city == 'New York City':
    selected_attractions_list = references.database.list_of_attractions_nyc
  elif resulted_city == 'Santa Fe, New Mexico':
    selected_attractions_list = references.database.list_of_attractions_santa_fe
  elif resulted_city == 'New Orleans':
    selected_attractions_list = references.database.list_of_attractions_new_orleans
  elif resulted_city == 'San Antonio, Texas':
    selected_attractions_list = references.database.list_of_attractions_san_antonio
  return selected_attractions_list
result_attractions_list = random_attractions_list()


def random_attraction_location():
  generated_attraction = random.choice(result_attractions_list)
  user_input = input(f'While in {resulted_city} would you like to vist {generated_attraction}? y/n: ')
  while user_input != 'y':
    re_generated_attraction = random_attraction_location()
    return re_generated_attraction
  else:
    print(f'{generated_attraction} great choice!')
  return generated_attraction
resulted_attraction = random_attraction_location()


def draft_final_destination():
  draft_finale = [resulted_city, resulted_transportation, resulted_attraction, resulted_dining_location]
  user_input = input(f'Your trip summary: location: {resulted_city}, transportation: {resulted_transportation}, dining: {resulted_dining_location}, Attraction: {resulted_attraction}. Would you like to confirm this trip? y/n: ')
  if user_input != 'y':
    re_user_input = input('which aspect of the trip would you like to change?("location", "transportation", "dining" or "attractions"): ')
    if re_user_input == 'location':
      re_draft_finale = [random_location(),
      random_dining_list(),
      random_attractions_list(),
      random_transporation(),
      random_diner_location(),
      random_attraction_location()]
      draft_final_destination()
      return re_draft_finale
    elif re_user_input == 'transportation':
      random_transporation()
      re_draft_finale[1] = draft_final_destination()
      return re_draft_finale
    elif re_user_input == 'dining':
      re_draft_finale = random_diner_location()
      draft_final_destination()
      return re_draft_finale
    elif re_user_input == 'attractions':
      re_draft_finale = random_attraction_location()
      draft_final_destination()
      return re_draft_finale
  else:
    print(f'Your weekend adventure is set! ')
  return draft_finale
resulted_destination = draft_final_destination()


# def print_final_destination():
#   while resulted_destination != resulted_city or resulted_attraction or resulted_dining_location or resulted_transportation:
#     if resulted_destination in references.database.list_of_cities:
#       resulted_city = resulted_destination
#       return resulted_city
#     elif resulted_destination in references.database.:
#       resulted_attraction = resulted_destination
#       return resulted_attraction
#     elif resulted_destination in references.database.list_of_transportation:
#       resulted_transportation = resulted_destination
#       return resulted_transportation
#   else:
#     print(f'Your finalized trip summary: location: {resulted_city}, transportation: {resulted_transportation}, dining: {resulted_dining_location}, Attraction: {resulted_attraction}.')
# print_final_destination()