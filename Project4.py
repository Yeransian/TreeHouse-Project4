from collections import OrderedDict
import datetime
import sys
import csv

from peewee import *

db = SqliteDatabase('inventory.db')


class Product(Model):
    content = TextField()
    id = PrimaryKeyField()
    product_name = TextField(unique=True)
    product_price = TextField()
    product_quantity = TextField()
    date_updated = DateTimeField(datetime.datetime.now)

    class Meta:
        database = db



def migrate_data():
    with open('inventory.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        keys = next(reader)
        #ordered = ([OrderedDict(zip(keys,row)) for row in reader ])

        print([OrderedDict(zip(keys,row)) for row in reader ])



def initialize():
    """ Initialize an Sqlite database called inventory.db."""
    db.connect()
    db.create_tables([Product], safe=True)




def create_model():
    """ Create a model called Product that the Peewee ORM will use to build the database. 
The Product model should have five attributes: product_id, product_name, product_quantity, 
product_price. Use PeeWee's built in primary_key functionality for the product_id field,
 so that each product will have an automatically generated unique identifier."""
    productname = ('product_name')


def csv_To_DB():
    return


def add_entry():
    """Add entries to the database"""




def view_entries():
    """View entries in the database"""
    entries = Product.select()
    for entry in entries:
        print(entry)


def backup_db():
    """Backup Database to a CSV File"""
    return


def search_entry(entry):
    """Search for an entry in the database"""
    view_entry(input('Search query'))


def menu_loop():

    choice = None
    while choice != 'q':
        for key, value in menu.items():
            print('{}) {}'.format(key, value.__doc__))
        choice = input('Action: ').lower()
        if choice in menu:
            menu[choice]()


menu = OrderedDict([
    ('a', add_entry),
    ('v', view_entries),
    ('b', backup_db),
    ('s', search_entry)
])


if __name__ == '__main__':

     initialize()  # Ensure you are connected to the database you created/initialized
     migrate_data()
#     load() # Ensure you load the CSV products data into the created table
     menu_loop() # Run the application so the user can make menu choices and interact with the application.