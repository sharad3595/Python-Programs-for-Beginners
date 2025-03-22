itienary = ("ktm","Hetauda","Chitwan")
visited_cities = set()




def display_menu():
    print("Welcome to my Travel Itienary Application")
    print("1. View travel destinations")
    print("2. Mark visited cities")
    print("3. View Visited Cities")
    print("4. View Unvisited/Remaining Cities to visit")

def view_itienary():
    print('Travel Destinations are as follows:')
    for city in itienary:
        print('-',city)

def mark_visited_city(city):
    visited_cities.add(city)
    print(f"{city} marked as visited!!")
    

def view_visited_cities():
    if visited_cities:
        print("You have visited following cities")
        for city in visited_cities:
            print(city)
            

def view_unvisited_cities():
    if(visited_cities):
        print("Remaining Cities to visit are:")
        unvisited = itienary - visited_cities
        print(unvisited)
    else:
        print("No cities visted yet. Please visit any city first.")
    
def main():
    display_menu()

   
    while True:
        choice = int(input("please select an option: "))
        if(choice ==1):
             view_itienary()
        elif(choice == 2):
            mark_city = input("Please enter city name: ")
            if mark_city in itienary:
                mark_visited_city(mark_city)
            else:
                print("City not in the itienary")            
        elif(choice == 3):
            view_visited_cities()
        elif(choice == 4):
            view_unvisited_cities()
        else:
            print("invalid option")

main()
