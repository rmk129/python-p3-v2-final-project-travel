# from models.__init__ import CURSOR, CONN
from lib.models.country import Country

class City:

    all = {}

    def __init__(self, name, visited, population, country_id, id=None):
        self.name = name
        self.visited = visited
        self.population = population
        self.country_id = country_id

    def __repr__(self):
        return (
            f"<City {self.id}: {self.name}, {self.visited}, {self.population} " +
            f"Country ID: {self.country_id}>"
            )
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError(
                "Name must be a non-empty string"
            )
        
    @property
    def visited(self):
        return self._visited
    
    @visited.setter
    def visited(self, visited):
        if isinstance(visited, bool):
            self._visited = visited
        else:
            raise ValueError("Visited must be True or False")
        
    @property
    def population(self):
        return self._population
    
    @population.setter
    def population(self, population):
        if isinstance(population, int) and population < Country.all[self.country_id].population:
            self._population = population
        else:
            raise ValueError("Population must be an Integer less than the population of its country")
        
    @property
    def country_id(self):
        return self._country_id

    @country_id.setter
    def country_id(self, country_id):
        if type(country_id) is int and Country.find_by_id(country_id):
            self._country_id = country_id
        else:
            raise ValueError(
                "country_id must reference a country in the database")
