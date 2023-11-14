# lib/cli.py

from helpers import (
    exit_program,
    list_countries,
    find_countries_by_language,
    create_country,
    update_country,
    delete_country,
    countries_with_cities_not_visited,
    list_cities,
    find_city_by_name,
    cities_by_population_in_country,
    create_city,
    update_city,
    delete_city,
    list_cities_by_visited
    

)


def first_menu():
    print("\n Welcome to your Travel BucketList Database \n" +
          "****************************************** \n" +
          "Please select an option:")
    print("Type A to enter the Database for Countries")
    print("Type E to Exit the program")

def country_menu():
    print("\nWelcome to your Countries' Menu\n" + 
          "******************************\n" +
          "Here you can view and find different countries as well as Add, Update, Delete, and Filter accordingly\n")
    print("To access the City's menu, Type 2 and select the Country of which the Cities you wish to see\n")
    print("Type 1 to List all countries")
    print("Type 2 to List all cities in a country sorted by population")
    print("Type 3 to Find countries by language")
    print("Type 4 to Add country")
    print("Type 5 to Update country")
    print("Type 6 to Delete country")
    print("Type 7 to Show all countries with cities that have not been visited")
    print("Type 8 to List all cities in the database")
    print("Type E to exit the program")

def city_menu():
    print("Welcome to your City's Menu \n" +
          "***************************\n" +
          "Here you can view and find different cities in the selected country" +
            " as well as Add, Update, Delete, and Filter accordingly\n")
    print("Type 1 to Find city by name")
    print("Type 2 to Add city")
    print("Type 3 to Update city")
    print("Type 4 to Delete city")
    print("Type 5 to List cities by visited or not visited")
    print("Type 10 to Go back to the Countries' menu")

def main():
    while True:
        first_menu()
        choice = input("> ").title()
        if choice == "A":
            country_handler()
        elif choice == "E":
            exit_program()
        else:
            print("Invalid choice. Please re-renter a valid option")

def country_handler():
    while True:
        country_menu()
        choice_2 = input("> ")
        if choice_2 == "1":
            list_countries()
        elif choice_2 == "2":
            country = cities_by_population_in_country()
            if country:
                city_handler(country)
        elif choice_2 == "3":
            find_countries_by_language()
        elif choice_2 == "4":
            create_country()
        elif choice_2 == "5":
            update_country()
        elif choice_2 == "6":
            delete_country()
        elif choice_2 == "7":
            countries_with_cities_not_visited()
        elif choice_2 == "8":
            list_cities()
        elif choice_2.title() == "E":
            exit_program()
        else:
            print("Invalid choice. Please re-renter a valid option")

def city_handler(country):
    while True:
        city_menu()
        choice_3 = input("> ")
        if choice_3 == "1":
            find_city_by_name(country)
        elif choice_3 == "2":
            create_city(country)
        elif choice_3 == "3":
            update_city(country)
        elif choice_3 == "4":
            delete_city(country)
        elif choice_3 == "5":
            list_cities_by_visited()
        elif choice_3 == "10":
            country_handler()
        else:
            print("Invalid choice. Please re-renter a valid option")   


if __name__ == "__main__":
    main()

