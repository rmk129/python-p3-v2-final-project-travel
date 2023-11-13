# lib/helpers.py
from models.city import City
from models.country import Country
from models.__init__ import CONN, CURSOR



def exit_program():
    print("Goodbye!")
    exit()

def list_countries():
    countries = Country.get_all()
    print("\nThe following countries are in the Database. Don't see your country? Add it in!\n")
    for country in countries:
        print(f"{country.name}\n" +
              f"Language:{country.language} Population:{country.population}\n")


def find_countries_by_language():
    language = input("Enter the language: ").title()
    countries = Country.find_by_language(language)
    if countries:
        print(f"\nWe found {len(countries)} countries that speak {language}! ")
        for country in countries:
            print(f"\n{country.name}")
    else:
        print("\nNo countries with the stated language")

def create_country():
    name = input("Enter the Country's name: ").title()
    language = input("Enter the Country's language: ").title()
    population = input("Enter the Country's population: ")
    if population.isdigit():
        try:
            country = Country.create(name, language, int(population))
            print(f'\nSuccessfully Added {country.name}!!!!')
        except Exception as exc:
            print("Error creating Country: ", exc)
    else:
        print("Error: Population must be an integer greater then 1000")
    
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
            print(f'Success: {country.name} has been updated!')
        except Exception as exc:
            print("Error updating country: Population must be an integer greater then 1000 or", exc )
    else:
        print(f'Country {input_name} not found')

def delete_country():
    input_name = input("Enter the Country's name: ").title()
    cities = City.get_all()
    if country := Country.find_by_name(input_name):
        cities_in_country = [city for city in cities if city.country_id == country.id]
        for city in cities_in_country:
            city.delete()
        country.delete()
        print(f'\nCountry {input_name} deleted')
    else:
        print(f'\nCountry {input_name} not found')

def countries_with_cities_not_visited():
    cities = City.get_all()
    cities_not_visited = [city for city in cities if city.visited == False]
    countries = set()
    for city in cities_not_visited:
        country = Country.find_by_id(city.country_id)
        countries.add(country)
    for country in countries:
        city_for_country = [city for city in cities_not_visited if city.country_id == country.id]
        print(f"\n{country.name}:The following cities have not been visited:")
        for city in city_for_country:
            print(city.name)


def list_cities():
    cities = City.get_all()
    print("\nThe following cities are in the Database. Don't see your city? Add it in!\n")
    for city in cities:
        country = Country.find_by_id(city.country_id)
        print(f"{city.name}\n"+
              f"Visited:{city.visited}, Population:{city.population}, Country:{country.name}\n")

def find_city_by_name():
    name = input("Enter the city's name: ").title()
    city = City.find_by_name(name)
    if city:
        country = Country.find_by_id(city.country_id)
        print(f"\n{city.name}\n" + f"Visited:{city.visited}, Population:{city.population}, Country: {country.name}\n")
    else:
        print(f"\nCity {name} not found\n")

def cities_by_population_in_country():
    name = input("Enter the Country's name: ").title()
    print(f"\n{name} has the following cities in your database:\n")
    country = Country.find_by_name(name)
    cities = City.get_all()
    cities_in_country = [city for city in cities if city.country_id == country.id]
    cities_in_country.sort(key=lambda x: x.population, reverse=True)
    for city in cities_in_country:
        print(f"{city.name}\n" + f"Visited:{city.visited}, Population:{city.population}\n" )

def create_city():
    print("Leaving any of the following prompts empty will create an Error in creating the city\n")
    name = input("Enter City's name: ").title()
    visited = input("Enter True or False if you have visited the city: ").title()
    population = input("Enter the City's population: ")
    country_name = input("Enter the Country the City is in: ").title()
    country = Country.find_by_name(country_name)
    if population.isdigit() and country and visited == "True" or visited == "False":
        try:
            city = City.create(name, bool(visited), int(population), country.id)
            print(f"Successfully added {city.name} to the database!!")
        except Exception as exc:
            print("Error creating city: ", exc)
    else:
        print("\nERROR: Population must be an integer greater then 1000 or Visited city has to be True or False\n")

def update_city():
    input_name = input("Enter the City's name you wish to update: ").title()
    if city := City.find_by_name(input_name):
        try:
            
            name = input("\nEnter the City's new name: ").title()
            if len(name) > 0:
                city.name = name
            visited = input("Enter True or False if the city has been visited: ")
            if len(visited) > 0:
                is_visited = True if visited.title() == "True" else False
                city.visited = is_visited
            population = input("Enter the City's population: ")
            if len(population) > 3 and population.isdigit():
                city.population = int(population)

            city.update()
            print(f'\nSuccessfully updated {city.name}\n')
        except Exception as exc:
            print("\nError updating {city.name}: \n", exc)
    else:
        print(f'City {input_name} not found')

def delete_city():
    input_name = input("Enter the City's name you wish to delete: ").title()
    if city := City.find_by_name(input_name):
        city.delete()
        print(f'\nCity {input_name} deleted\n')
    else:
        print(f'\nCity {input_name} not found\n')

def list_cities_by_visited():
    input_info = input("Enter Y to see visited and N to see not visited: ").title()
    cities = City.get_all()
    if input_info == "Y" and cities:
        print("\n The following cities HAVE been visited:\n")
        visited_cities = [city for city in cities if city.visited == True]
        for city in visited_cities:
            print(city.name)
    elif input_info == "N" and cities:
        print("\nThe following cities HAVE NOT been visited:\n")
        not_visited_cities = [city for city in cities if city.visited == False]
        for city in not_visited_cities:
            print(city.name)
    else:
        print("Input not valid. Please input Y or N")
    print("\n")



