# lib/helpers.py
from models.city import City
from models.country import Country
from models.__init__ import CONN, CURSOR


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

def find_city_by_name():
    name = input("Enter the city's name: ").title()
    city = City.find_by_name(name)
    print(city) if city else print(f"City {name} not found")

def cities_by_population_in_country():
    name = input("Enter the Country's name: ").title()
    country = Country.find_by_name(name)
    cities = City.get_all()
    cities_in_country = [city for city in cities if city.country_id == country.id]
    cities_in_country.sort(key=lambda x: x.population, reverse=True)
    for city in cities_in_country:
        print(city)

def create_city():
    name = input("Enter City's name: ").title()
    visited = bool(input("Enter True or False if you have visited the city: "))
    population = int(input("Enter the City's population: "))
    country_name = input("Enter the Country the City is in: ").title()
    country = Country.find_by_name(country_name)

    try:
        city = City.create(name, visited, population, country.id)
        print(f"Success: {city}")
    except Exception as exc:
        print("Error creating city: ", exc)

def update_city():
    input_name = input("Enter the City's name: ").title()
    if city := City.find_by_name(input_name):
        try:
            name = input("Enter the City's new name: ")
            city.name = name
            visited = bool(input("Enter True or False if the city has been visited: "))
            city.visited = visited
            population = int(input("Enter the City's population: "))
            city.population = population

            city.update()
            print(f'Success: {city}')
        except Exception as exc:
            print("Error updating {city}: ", exc)
    else:
        print(f'City {input_name} not found')

def delete_city():
    input_name = input("Enter the City's name: ").title()
    if city := City.find_by_name(input_name):
        city.delete()
        print(f'City {input_name} deleted')
    else:
        print(f'City {input_name} not found')

def list_cities_by_visited():
    input_info = input("Enter Y to see visited and N to see not visited: ").title()
    cities = City.get_all()
    if input_info == "Y" and cities:
        visited_cities = [city for city in cities if city.visited == True]
        for city in visited_cities:
            print(city)
    elif input_info == "N" and cities:
        not_visited_cities = [city for city in cities if city.visited == False]
        for city in not_visited_cities:
            print(city)
    else:
        print("Input not valid. Please input Y or N")



