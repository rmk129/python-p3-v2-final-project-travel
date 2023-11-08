# lib/cli.py

from helpers import (
    exit_program,
    list_countries,
    find_country_by_name,
    find_countries_by_language,

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
    print("10. Find city by ID")
    print("11. Add city")
    print("12. Update city")
    print("13. Delete city")
    print("14. List all cities in a country")
    print("15. List all visited cities")
    print("16. List all cities not visited")


if __name__ == "__main__":
    main()
