from collections import OrderedDict
import datetime
import sys
import csv

from peewee import *

db = SqliteDatabase('inventory.db')


class Product(Model):

    id = AutoField()
    product_name = TextField(unique=True)
    product_price = TextField()
    product_quantity = TextField()
    date_updated = DateField(datetime.datetime.now().strftime('%m/%d/%Y'))

    class Meta:
        database = db


def migrate_data():
    with open('inventory.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        keys = next(reader)
        ordered = ([OrderedDict(zip(keys,row)) for row in reader ])
        # print([OrderedDict(zip(keys,row)) for row in reader ])
        # od = [OrderedDict(zip(keys,row) for row in reader)]
        for item in ordered:
            try:
                p_n = item['product_name']
                p_p = item['product_price']
                p_q = item['product_quantity']
                d_u = item['date_updated']
                Product.create(product_name=p_n,
                               product_price=p_p,
                               product_quantity=p_q,
                               date_updated=d_u)
            except IntegrityError:
                break


def initialize():
    """ Initialize an Sqlite database called inventory.db."""
    db.connect()
    db.create_tables([Product], safe=True)


def view_entries(search_query=None):
    """ View entries. """
    entries = Product.select().order_by(Product.id.asc())
    #print(entries)
    for entry in entries:
        print("ID: {}, Product Name: {}, Product Price: {}, Product Quantity: {}, Last Updated: {}\n".format(
            entry.id, entry.product_name, entry.product_price, entry.product_quantity, entry.date_updated))
        order = ("ID: {}, Product Name: {}, Product Price: {}, Product Quantity: {}, Last Updated: {}\n".format(
            entry.id, entry.product_name, entry.product_price, entry.product_quantity, entry.date_updated))



    # if search_query:
    #     #     entries = entries.where(Product.product_name.contains(search_query))
    #     # for entry in entries:
    #     #      timestamp = entry('%A %B %d, %Y %I:%M%p')
    #     #      print(timestamp)
    #     #      print('='*len(timestamp))
    #     #      print(entry.content)
    #     #      print('\n\n' + '=' * len(timestamp))
    #     #      print('n) for next entry')
    #     #      print('d) Delete entry')
    #     #      print('q) return to main menu')
    #     #
    #     #      next_action = input('Action: [N\q\d] ').lower().strip()
    #     #      if next_action == 'q':
    #     #          break
    #     #      elif next_action == 'd':
    #     #          delete_entry(entry)


def search_entry():
    """Search entries for a string."""
    s = input('Search Query')
    view_entries(s)


def backup_db():
    """Backup Database to a CSV File"""
    # TODO: Create backup function to export database into a CSV format file
    return


def add_entry():
    """Add entries to the database"""


def id_search():
    """Search for an entry by ID"""
    find_id = input("Enter an ID number")
    #Product.get_by_id(find_id)
    print(Product.get_by_id(find_id))               #select().order_by(Product.id.asc())



def menu_loop():

    choice = None
    while choice != 'q':
        for key, value in menu.items():
            print('{}) {}'.format(key, value.__doc__))
        choice = input('Action: ').lower()
        if choice in menu:
            menu[choice]()
        elif choice == ('v'):
            view_entries()
        elif choice == ('s'):
            s = input('Search Query')
            search_entry(s)


menu = OrderedDict([
    ('a', add_entry),
    ('v', view_entries),
    ('b', backup_db),
    ('s', search_entry),
    ('id', id_search)
])


if __name__ == '__main__':

     initialize()  # Ensure you are connected to the database you created/initialized
     migrate_data()
     menu_loop() # Run the application so the user can make menu choices and interact with the application.