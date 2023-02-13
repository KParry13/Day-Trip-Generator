
import random

Destination = ['Chicago', 'Louisville', 'Gatlinburg', 'Myrtle Beach']
Restaurant = ['Cafe Lulu', 'Derby Bowl', 'Wild Bears', 'Sea Captains House']
Transportation = ['Train', 'Helicopter', 'Skyline', 'Motorcycle']
Entertainment = ['Musical', 'Hiking', 'Zipline', 'Aquarium']


def Trip_options(list_trip):
    select_trip= random.choice(list_trip)
    return select_trip

def run_day_trip():
    my_destiantion = Trip_options(Destination)
    print ("Destination: ",my_destiantion)

    my_restaurant = Trip_options(Restaurant)
    print ("Restaurant: ",my_restaurant)

    my_transportaion = Trip_options(Transportation)
    print ("Transportaion: ",my_transportaion)

    my_entertainment = Trip_options(Entertainment)
    print ("Entertainment: ",my_entertainment)



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
        elif answer == 'Transportation':
            my_transportaion = Trip_options(Transportation)
            print ("Transportaion: ",my_transportaion)
        elif answer == 'Entertainment':
            my_entertainment = Trip_options(Entertainment)
            print ("Entertainment: ",my_entertainment)  

        print('How does this sound?')
    answer = input('')
    print('What would you like to change?')
        
    if answer == 'Y':
        print('Great Choice!')
        
    answer = 'N'
    while answer == 'N':

        print(f"Destination: {my_destiantion}")
        print("Restaurant: ",my_restaurant)
        print("Transportaion: ",my_transportaion)
        print("Entertainment: ",my_entertainment)
        print ('confirm your trip')
        print ('Can we make your reservations?')
        answer = input('Y or N')
        if answer == 'N':
            print('Start selections over.')
                    
            my_destiantion = Trip_options(Destination)
          

            my_restaurant = Trip_options(Restaurant)
           

            my_transportaion = Trip_options(Transportation)
           

            my_entertainment = Trip_options(Entertainment)


            

        elif answer == 'Y':
            print('Pack your bags! Your plans are reserved!')




    

    
run_day_trip()