from models.__init__ import CURSOR, CONN
from .country import Country

class City:

    all = {}

    def __init__(self, name, visited, population, country_id, id=None):
        self.name = name
        self.visited = visited
        self.population = population
        self.country_id = country_id

    def __repr__(self):
        return f"<City {self.id}: {self.name}, {self.visited}, {self.population}, {self.country_id}>"
    
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
        if isinstance(population, int) and population > 100000:
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
        
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS cities (
            id INTEGER PRIMARY KEY,
            name TEXT,
            visited BOOLEAN,
            population INTEGER,
            country_id INTEGER,
            FOREIGN KEY (country_id) REFERENCES countries(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS cities;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
                INSERT INTO cities (name, visited, population, country_id)
                VALUES (?, ?, ?, ?)
        """

        CURSOR.execute(sql, (self.name, self.visited, self.population, self.country_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        sql = """
            UPDATE cities
            SET name = ?, visited = ?, population = ?, country_id = ?
            WHERE id = ?
        """
        breakpoint()
        CURSOR.execute(sql, (self.name, self.visited, self.population,
                             self.country_id, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM cities
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def create(cls, name, visited, population, country_id):
        city = cls(name, visited, population, country_id)
        city.save()
        return city
    
    @classmethod
    def instance_from_db(cls, row):
        city = cls.all.get(row[0])
        if city:
            city.name = row[1]
            city.visited = bool(int(row[2]))
            city.population = row[3]
            city.country_id = row[4]
        else:
            city = cls(row[1], bool(int(row[2])), row[3], row[4])
            city.id = row[0]
            cls.all[city.id] = city
        return city
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM cities
        """
        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM cities
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM cities
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

