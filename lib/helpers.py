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

def create_country():
    name = input("Enter the Country's name: ").title()
    language = input("Enter the Country's language: ").title()
    population = int(input("Enter the Country's population: "))
    try:
        country = Country.create(name, language, population)
        print(f'Success: {country}')
    except Exception as exc:
        print("Error creating company: ", exc)

def update_country():
    input_name = input("Enter the country's name: ").title()
    if country := Country.find_by_name(input_name):
        try:
            name = input("Enter the Country's new name: ").title()
            country.name = name
            language = input("Enter the Country's new language: ").title()
            country.language = language
            population = int(input("Enter the Country's new population "))
            country.population = population

            country.update()
            print(f'Success: {country}')
        except Exception as exc:
            print("Error updating country: ", exc)
    else:
        print(f'Country {input_name} not found')

def delete_country():
    input_name = input("Enter the Country's name: ").title()
    if country := Country.find_by_name(input_name):
        country.delete()
        print(f'Country {input_name} deleted')
    else:
        print(f'Country {input_name} not found')

def countries_with_cities_not_visited():
    cities = City.get_all()
    cities_not_visited = [city for city in cities if city.visited == False]
    countries = set()
    for city in cities_not_visited:
        country = Country.find_by_id(city.country_id)
        countries.add(country)
    for country in countries:
        print(country)

def list_cities():
    cities = City.get_all()
    for city in cities:
        print(city)

