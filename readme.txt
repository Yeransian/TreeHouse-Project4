Create your application file
Create a new file in your project directory called app.py. Be sure to import the appropriate Python and Peewee modules at the top of this file.

Read in the existing CSV data
Read the inventory.csv file into your program, and create a list that contains each product inside the csv file as a dictionary. Be sure to clean up the data before adding each product dictionary to your list:

the value for product_quantity will be stored as an integer
the value for product_price will be stored as an integer and converted to cents ($3.19 becomes 319, for example)
the value for date_updated will be stored as a date.
Hint: You'll need the datetime module for this.
Initialize your Sqlite database
Initialize an Sqlite database called inventory.db.

Create your Product model
Create a model called Product that the Peewee ORM will use to build the database. The Product model should have five attributes: product_id, product_name, product_quantity, product_price. Use PeeWee's built in primary_key functionality for the product_id field, so that each product will have an automatically generated unique identifier.

Add the data from CSV into the database
Create a function that will add the products listed in the inventory.csv file to the database.

Create a Menu to make selections
Create a function to handle interaction with the user of your app. This function should prompt the user to enter v in order to view the details of a single product in the database, a to add a new product to the database, or b to make a backup of the entire contents of the database.

Displaying a product by its ID
Create a function to handle getting and displaying a product by its product_id.

Adding a new product to the database
Create a function to handle adding a new product to the database. This function should prompt the user to enter the product's name, quantity, and price. The function must process the user provided value for price from a string to an int. Be sure the value you stored for the price field to the database is converted to cents ($2.99 becomes 299, for example).

Backup the database (Export new CSV)
Create a function to handle making a backup of the database. The backup should be written to a .csv file.

Connect the database and create tables
In your dunder main method:

Ensure you are connected to the database you created/initialized
Ensure you load the CSV products data into the created table
Run the application so the user can make menu choices and interact with the application.