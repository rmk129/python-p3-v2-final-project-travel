# lib/helpers.py
from models.city import City
from models.country import Country


def exit_program():
    print("Goodbye!")
    exit()

def list_countries():
    countries = Country.get_all()
    for country in countries:
        print(country)

def find_country_by_name():
    name = input("Enter the Country's Name: ").title()
    country = Country.find_by_name(name)
    print(country) if country else print(f'Country {name} not found')

def find_countries_by_language():
    language = input("Enter the language: ").title()
    countries = Country.find_by_language(language)
    if countries:
        for country in countries:
            print(country)
    else:
        print("No countries with the stated language")
