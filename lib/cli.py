# lib/cli.py

from helpers import (
    exit_program,
    list_countries,
    find_country_by_name,
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


# def main():
#     while True:
#         menu()
#         choice = input("> ")
#         if choice == "0":
#             exit_program()
#         elif choice == "1":
#             list_countries()
#         elif choice == "2":
#             find_country_by_name()
#         elif choice == "3":
#             find_countries_by_language()
#         elif choice == "4":
#             create_country()
#         elif choice == "5":
#             update_country()
#         elif choice == "6":
#             delete_country()
#         elif choice == "7":
#             countries_with_cities_not_visited()
#         elif choice == "8":
#             list_cities()
#         elif choice == "9":
#             find_city_by_name()
#         elif choice == "10":
#             cities_by_population_in_country()
#         elif choice == "11":
#             create_city()
#         elif choice == "12":
#             update_city()
#         elif choice == "13":
#             delete_city()
#         elif choice == "14":
#             list_cities_by_visited()
#         else:
#             print("Invalid choice")


# def menu():
#     print("\n Welcome to your Travel BucketList DataBase \n" +
#           "****************************************** \n" +
#           "Please select an option:")
#     print("0. Exit the program")
#     print("1. List all countries")
#     print("2. Find country by name")
#     print("3. Find countries by language")
#     print("4. Add country")
#     print("5. Update country")
#     print("6. Delete country")
#     print("7. Show all countries with cities that have not been visited")
#     print("8. List all cities")
#     print("9. Find city by name")
#     print("10. List all cities in a country sorted by population")
#     print("11. Add city")
#     print("12. Update city")
#     print("13. Delete city")
#     print("14. List cities by visited or not visited")

def first_menu():
    print("\n Welcome to your Travel BucketList DataBase \n" +
          "****************************************** \n" +
          "Please select an option:")
    print("Type A to see the options for Countries")
    print("Type B to see the options for Cities")
    print("Type E to Exit the program")

def country_menu():
    print("\nWelcome to your Countries' Menu\n" + 
          "******************************\n" +
          "Here you can view and find different countries as well as Add, Update, Delete, and Filter accordingly\n")
    print("Type 1 to List all countries")
    print("Type 2 to Find country by name")
    print("Type 3 to Find countries by language")
    print("Type 4 to Add country")
    print("Type 5 to Update country")
    print("Type 6 to Delete country")
    print("Type 7 to Show all countries with cities that have not been visited")
    print("Type 8 to go back to the main menu")

def city_menu():
    print("Welcome to your City's Menu \n" +
          "***************************\n" +
          "Here you can view and find different cities as well as Add, Update, Delete, and Filter accordingly\n")
    print("Type 1 to List all cities")
    print("Type 2 to Find city by name")
    print("Type 3 to List all cities in a country sorted by population")
    print("Type 4 to Add city")
    print("Type 5 to Update city")
    print("Type 6 to Delete city")
    print("Type 7 to List cities by visited or not visited")
    print("Type 8 to Go back to the main menu")

def main():
    while True:
        first_menu()
        choice = input("> ").title()
        if choice == "A":
            while True:
                country_menu()
                choice_2 = input("> ")
                if choice_2 == "1":
                    list_countries()
                elif choice_2 == "2":
                    find_country_by_name()
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
                    main()
                else:
                    print("Invalid choice. Please re-renter a valid option")
        elif choice == "B":
            while True:
                city_menu()
                choice_3 = input("> ")
                if choice_3 == "1":
                    list_cities()
                elif choice_3 == "2":
                    find_city_by_name()
                elif choice_3 == "3":
                    cities_by_population_in_country()
                elif choice_3 == "4":
                    create_city()
                elif choice_3 == "5":
                    update_city()
                elif choice_3 == "6":
                    delete_city()
                elif choice_3 == "7":
                    list_cities_by_visited()
                elif choice_3 == "8":
                    main()
                else:
                    print("Invalid choice. Please re-renter a valid option")
        elif choice == "E":
            exit_program()
        else:
            print("Invalid choice. Please re-renter a valid option")
    


if __name__ == "__main__":
    main()
