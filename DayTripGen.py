
import random

Destination = ['Chicago', 'Louisville', 'Gatlinburg', 'Myrtle Beach']
Restaurant = ['Cafe Lulu', 'Derby Bowl', 'Wild Bears', 'Sea Captains House']
Mode_of_Transportation = ['Train', 'Helicopter', 'Skyline', 'Motorcycle']
Entertainment = ['Musical', 'Hiking', 'Zipline', 'Aquarium']



def Trip_options(list_trip):
    select_trip= random.choice(list_trip)
    return select_trip

my_destiantion = Trip_options(Destination)
print ("Destination: ",my_destiantion)

my_restaurant = Trip_options(Restaurant)
print ("Restaurant: ",my_restaurant)

my_transportaion = Trip_options(Mode_of_Transportation)
print ("Transportaion: ",my_transportaion)

my_entertainment = Trip_options(Entertainment)
print ("Entertainment: ",my_entertainment)


def determine_satisfaction(current_trip, Trip_options):
    user_satisfied= input('Are you satisfied with this trip?')
    yes = ('Awesome! Pack your bags!')
    no = input('What would you like to change?')
    if yes:
        print(yes)

    
