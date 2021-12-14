# simple_database-tkinter-psycopg2-
Simple database. Realise on python and PostgreSQL using tkinter, psycopg2.

#tkinter #postgreSQL #psycopg2 #postgresql


---> RUN

1. A data your database is configured in file 'Config.py'   
2. Run 'Openly_window.py'



---> HOW TO USE?

1\ The required table is selected in the window on the left and remains active

2\ Press 'Receive'

ADD DATA

1\ The required table is selected in the window on the right and remains active

2\ The data is filled in the row to the right

3\ Press 'Add'

Example: {id serial, name varchar(20), age smallinteger} - 'Alexey', 21

DELETE DATA

1\ The required table is selected in the window on the right and remains active

2\ Select the ID to be deleted

3\ Press 'Delete'



To login as administrator - login:admin, password:admin

The administrator's functionality is an extended user functionality. Here you can see all users (format: ID (serial), name(string), password(string)) and changes made in the database (format: ID (serial), action("add" or "delete" - string), ID object(integer), object table(integer))



-Without OOP-
