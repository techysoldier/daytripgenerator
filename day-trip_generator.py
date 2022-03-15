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
# current issues :finishing out transaction ie.  As a user, I want to display my completed trip in the console.
# currently running up until like 128 anything put after does not function

#  destination section

from ast import Return
import random


trip_destinations = ['Venice', 'Greece', 'Belize','Sydney']

def select_random_trip_destination(daytrips):
        #index 0  index 1  index 2 index 3
    chosen_random_destination = random.choice(daytrips)
    print(chosen_random_destination) 
    return chosen_random_destination
choices_objecta = select_random_trip_destination(trip_destinations)



print("Do you like your chosen destination?")
answer = input('') 
while answer == 'N':
    print(select_random_trip_destination(trip_destinations)) 
    print("Do you like your chosen destination?")
    answer = input('') 
if answer == 'Y':
      print( 'Great choice')
 

#resturant section


trip_resturants = ['Lisa', 'Ginos', 'Bella','Strasse']
def select_random_trip_resturant(foods):
     #index 0  index 1  index 2 index 3
    chosen_random_resturant = random.choice(foods)
    print(chosen_random_resturant) 
    return chosen_random_resturant

choices_objectb = select_random_trip_resturant(trip_resturants)

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


trip_transportation = ['Train', 'Car', 'Limo','Lyft']

def select_random_trip_transportation(rides):
        #index 0  index 1  index 2 index 3
    chosen_random_transportation = random.choice(rides)
    print(chosen_random_transportation) 
    return chosen_random_transportation


choices_objectc = select_random_trip_transportation(trip_transportation)

print("Do you like your chosen transportation?")
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


trip_entertainment = ['Opera', 'Tours', 'Museums', 'Concert']

def select_random_entertainment(things_to_do):
    #index 0 index 1 index 2 index 3
    chosen_random_entertainment = random.choice(things_to_do)
    print(chosen_random_entertainment)
    return chosen_random_entertainment

choices_objectd = select_random_entertainment(trip_entertainment)


print("Do you like your chosen entertainment?")
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


choices_objecta = select_random_trip_destination
choices_objectb = select_random_trip_resturant
choices_objectc = select_random_trip_transportation
choices_objectd = select_random_entertainment

def finalize_trip():
    print('Here is your current itinerary')
    print(select_random_trip_destination)
    print(select_random_trip_resturant)
    print(select_random_trip_transportation)
    print(select_random_entertainment)   
    print('Do you have any objections?')
answer = input('Y or N')
while answer == 'N':
    Return 
while answer == 'Y':
    print('Thank you for using the trip generator. Please enjoy your trip!')