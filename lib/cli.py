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
    update_city
    

)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_countries()
        elif choice == "2":
            find_country_by_name()
        elif choice == "3":
            find_countries_by_language()
        elif choice == "4":
            create_country()
        elif choice == "5":
            update_country()
        elif choice == "6":
            delete_country()
        elif choice == "7":
            countries_with_cities_not_visited()
        elif choice == "8":
            list_cities()
        elif choice == "9":
            find_city_by_name()
        elif choice == "10":
            cities_by_population_in_country()
        elif choice == "11":
            create_city()
        elif choice == "12":
            update_city()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all countries")
    print("2. Find country by name")
    print("3. Find countries by language")
    print("4. Add country")
    print("5. Update country")
    print("6. Delete country")
    print("7. Show all countries with cities that have not been visited")
    print("8. List all cities")
    print("9. Find city by name")
    print("10. List all cities by population in a country")
    print("11. Add city")
    print("12. Update city")
    print("13. Delete city")
    print("14. List all visited cities")
    print("15. List all cities not visited")


if __name__ == "__main__":
    main()
