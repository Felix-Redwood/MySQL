import os
import datetime
import pymysql

# Get username from cloud9 workspace
username = os.getenv('C9_USER')

# Connect to the database
connection = pymysql.connect(host='localhost', user=username, password='', db='Chinook')

try:
    # Run a query. Using DictCursor means that rows now include column names, and it is better converted into a JSON format. Using the default cursor returns the rows as a tuple, with no labels
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        list_of_names = ['Fred','Fred']
        # Prepare a string with the same number of placeholders as in list_of_names. ",".join ensures that there is a comma between each list item
        # Joins a comma onto the end of each %s. Each %s is a name, stored in list_of_names
        format_strings = ",".join(['%s']*len(list_of_names))
        # .format runs format_strings
        cursor.execute("DELETE FROM Friends WHERE name in ({})".format(format_strings), list_of_names)
        # Save the changes
        connection.commit()
finally:
    # Close the connection, regardless of whether or not the above was successful
    connection.close()

# The execute() method of the cursor does ONE row, the executemany() method executes multiple rows