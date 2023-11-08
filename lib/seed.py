from models.__init__ import CONN, CURSOR
from models.country import Country
from models.city import City

def seed_database():
    Country.drop_table()
    City.drop_table()
    Country.create_table()
    City.create_table()

    spain = Country.create("Spain", "Spanish", 47540000)
    uk = Country.create("United Kingdom", "English", 67736000)
    italy = Country.create("Italy", "Italian", 58870000)
    columbia = Country.create("Columbia", "Spanish", 51520000)
    
    City.create("Barcelona", True, 5687000, spain.id)
    City.create("Seville", False, 701000, spain.id)
    City.create("London", True, 9648000, uk.id)
    City.create("Manchester", False, 2791000, uk.id)
    City.create("Milan", False, 3154000, italy.id)
    City.create("Florence", True, 711000, italy.id)
    City.create("Como", False, 489000, italy.id)
    City.create("Medellin", False, 2569000, columbia.id)
    City.create("Cartagena", True, 914552, columbia.id)

seed_database()
print("Seeded database")