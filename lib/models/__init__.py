import sqlite3

CONN = sqlite3.connect('travel.db')
CURSOR = CONN.cursor()
