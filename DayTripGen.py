
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

Y = 'Great Selection!'

print('Does this sound like a trip for you?')
answer = input('')
while answer == 'N':
    print('What is not to your liking?')
    answer = input('')
    if answer == 'Destination':
        my_destiantion = Trip_options(Destination)
        print ("Destination: ",my_destiantion)
    elif answer == 'Restaurant':
        my_restaurant = Trip_options(Restaurant)
        print ("Restaurant: ",my_restaurant)
    elif answer == 'Mode of Transportation':
        my_transportaion = Trip_options(Mode_of_Transportation)
        print ("Transportaion: ",my_transportaion)
    elif answer == 'Entertainment':
        my_entertainment = Trip_options(Entertainment)
        print ("Entertainment: ",my_entertainment)  
while answer == 'Y':
    print('Nice!')
    break


def confirmation(options):
    select_trip = options
    options=confirmation
    for options in Trip_options:
    
        print ("Destination: ",my_destiantion)
        print ("Restaurant: ",my_restaurant)
        print ("Transportaion: ",my_transportaion)
        print ("Entertainment: ",my_entertainment)

    print ('Can we make your reservations?')
    answer = input('Y or N')
    while answer == 'N':
        print('Start selections over.')
    while answer == 'Y':
        print('Pack your bags! Your plans are reserved!')




    

    
