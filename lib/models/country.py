from models.__init__ import CURSOR, CONN

class Country:

    all = {}

    def __init__(self, name, language, population, id=None):
        self.id = id
        self.name = name
        self.language = language
        self.population = population

    def __repr__(self):
        return f"<Country {self.id}: {self.name}, {self.language}, {self.population}>"
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string")
        
    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, language):
        if isinstance(language, str) and len(language):
            self._language = language
        else:
            raise ValueError(
                "Language must be a non-empty string"
            )
        
    @property
    def population(self):
        return self._population
    
    @population.setter
    def population(self, population):
        if isinstance(population, int) and population > 1000:
            self._population = population
        else:
            raise ValueError("Population must be an integer greater then 1000")
        
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS countries (
            id INTEGER PRIMARY KEY,
            name TEXT,
            language TEXT,
            population INTEGER)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS countries;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO countries (name, language, population)
            VALUES (?, ?, ?)
        """

        CURSOR.execute(sql, (self.name, self.language, self.population))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, language, population):
        country = cls(name, language, population)
        country.save()
        return country
    
    def update(self):
        sql = """
            UPDATE countries
            SET name = ?, language = ?, population = ?
            WHERE id = ?
        """
        if isinstance(self.population, int) and self.population > 1000:
            CURSOR.execute(sql, (self.name, self.language, self.population, self.id))
            CONN.commit()
        else:
            raise ValueError("Population must be an integer greater then 1000")

    def delete(self):
        sql = """
            DELETE FROM countries
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        country = cls.all.get(row[0])
        if country:
            country.name = row[1]
            country.language = row[2]
            country.population = row[3]
        else:
            country = cls(row[1], row[2], row[3])
            country.id = row[0]
            cls.all[country.id] = country
        return country
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM countries
        """
        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_language(cls, language):
        sql = """
            SELECT *
            FROM countries
            WHERE language = ?
        """

        rows = CURSOR.execute(sql, (language,)).fetchall()
        if rows:
            return [cls.instance_from_db(row) for row in rows]
        else:
            None

    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM countries
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM countries
            WHERE id is ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def cities(self):
        from .city import City
        sql = """
            SELECT * FROM cities
            WHERE country_id = ?
        """
        CURSOR.execute(sql, (self.id,),)

        rows = CURSOR.fetchall()
        return [City.instance_from_db(row) for row in rows]