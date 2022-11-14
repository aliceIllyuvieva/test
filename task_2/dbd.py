import sqlalchemy as db
import pandas as pd

config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'user',
    'password': 'password',
    'database': 'testdatabase'
}
db_user = config.get('user')
db_pwd = config.get('password')
db_host = config.get('host')
db_port = config.get('port')
db_name = config.get('database')

connection_str = f'mysql+pymysql://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}'

#in order to provide some results I fill in the table with potential values, this part can be eliminated in real life untill get_connection() fucn
engine = db.create_engine(connection_str)
connection = engine.connect()
connection.execute("""delete from TestBase""")
connection.execute("""INSERT INTO TestBase (category, product) VALUES (1, 11)""")
connection.execute("""INSERT INTO TestBase (category, product) VALUES (1, 12)""")
connection.execute("""INSERT INTO TestBase (category, product) VALUES (1, 13)""")
connection.execute("""INSERT INTO TestBase (category, product) VALUES (1, 14)""")
connection.execute("""INSERT INTO TestBase (category, product) VALUES (2, 11)""")
connection.execute("""INSERT INTO TestBase (category, product) VALUES (3, 11)""")

def get_connection():
    engine = db.create_engine(connection_str)
    return engine
