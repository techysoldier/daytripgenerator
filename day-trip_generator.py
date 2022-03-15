# Use and practice Python fundamentals, with an emphasis on Single Responsibility.

# Technologies # Python

# User Stories
# Total Unweighted Project Points: /70
# Total Weighted Project Points: /10
    # (5 points): As a developer, I want to make at least three commits with descriptive messages.
    # (5 points): As a developer, I want to store my destinations, restaurants, mode of transportation, and entertainments in their own separate lists.
    # (5 points): As a user, I want a destination to be randomly selected for my day trip.
    # (5 points): As a user, I want a restaurant to be randomly selected for my day trip.
    # (5 points): As a user, I want a mode of transportation to be randomly selected for my day trip.
    # (5 points): As a user, I want a form of entertainment to be randomly selected for my day trip.


    # (15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment if I don’t like one or more of those things.
    # (10 points): As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections.
    # (10 points): As a user, I want to display my completed trip in the console.
    # (5 points): As a developer, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing!


#Creating a list 
# current issues : double printing of destinations, restaurants, mode of transportation, and entertainments
#how to gather all selections to print to console as a itenirary 
#do all functions have a single function?

#  destination section

import random


trip_destinations = ['Venice', 'Greece', 'Belize','Sydney']

def select_random_trip_destination(daytrips):
        #index 0  index 1  index 2 index 3
    chosen_random_destination = random.choice(daytrips)
    print(chosen_random_destination) 
    return chosen_random_destination
select_random_trip_destination(trip_destinations)



print("Do you like your chosen destination?")
answer = input('') 
while answer == 'N':
    print(select_random_trip_destination(trip_destinations)) 
    print("Do you like your chosen destination?")
    answer = input('') 
if answer == 'Y':
      print( 'Great choice')
 

#resturant section


import random
trip_resturants = ['Lisa', 'Ginos', 'Bella','Strasse']
def select_random_trip_resturant(foods):
     #index 0  index 1  index 2 index 3
    chosen_random_resturant = random.choice(foods)
    print(chosen_random_resturant) 
    return chosen_random_resturant

select_random_trip_resturant(trip_resturants)

print("Do you like your chosen destination?")
answer = input('') 
while answer == 'N':
    print ('Sorry to hear your random selection wasnt to your liking')
    print(select_random_trip_resturant(trip_resturants)) 
    print("Do you like your chosen destination?")
    answer = input('') 
    print ('Sorry to hear your selection wasnt to your liking')
    
else:
    print('We will make reservations for your trip')


#transportation section

import random

trip_transportation = ['Train', 'Car', 'Limo','Lyft']

def select_random_trip_transportation(rides):
        #index 0  index 1  index 2 index 3
    chosen_random_transportation = random.choice(rides)
    print(chosen_random_transportation) 
    return chosen_random_transportation


select_random_trip_transportation(trip_transportation)

print("Do you like your chosen destination?")
answer = input('') 
while answer == 'N':
    print ('Sorry to hear your random selection wasnt to your liking')
    print(select_random_trip_transportation(trip_transportation)) 
    print("Do you like your chosen destination?")
    answer = input('') 
    print ('Sorry to hear your selection wasnt to your liking')
    
else:
    print('We will make reservations for your trip')


#entertainment section

import random

trip_entertainment = ['Opera', 'Tours', 'Museums', 'Concert']

def select_random_entertainment(things_to_do):
    #index 0 index 1 index 2 index 3
    chosen_random_entertainment = random.choice(things_to_do)
    print(chosen_random_entertainment)
    return chosen_random_entertainment

select_random_entertainment(trip_entertainment)


print("Do you like your chosen destination?")
answer = input('') 
while answer == 'N':
    print ('Sorry to hear your random selection wasnt to your liking')
    print(select_random_entertainment(trip_entertainment)) 
    print("Do you like your chosen destination?")
    answer = input('') 
    print ('Sorry to hear your selection wasnt to your liking')
else:
    print('We will make reservations for your trip')
    print('Congratulations your trip is booked lets confirm the details')



# #finalize 

# def finalize_transaction(choices_object):
#     choices_object = {
#         'destination': chosen_random_destination,
#         'transportation': chosen_random_transportation,
#         'restaurant': chosen_random_resturant,
#         'entertainment': chosen_random_entertainment
#     }

# finalize_transaction(choices_object)

# print('Time to prepare for your trip. Here are the details, You will be headed to (chosen_random_destination') 
# ('by (chosen_random_transportation), where you will be attending (chosen_random_entertainment) and dining at (chosen_random_resturant)')