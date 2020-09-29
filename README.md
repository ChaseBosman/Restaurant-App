## Restaurant table and ticket manager
#### The purpose of this application is to simplify a waiters job through managing their tables and customers. The application communicates with an SQLite database to populate food categories and menu items. Waiters have the ability to sign customers up for memberships in order to acculumate points through their personal file stored on AWS S3. The application is loaded onto a tablet that waiters utilize throughout their shift. Waiters manage their entire table section from the application, allowing table management instantly from a table. Orders are relayed to the kitchen/bar directly from the application This not only results in a massive improvement in waiter efficiency, but also completely removes the need for paper tickets and computer stations around the restaurant.  

## Instructions
#### Server side is ran through "in_progress_window.py". Client is ran through "table_select_window.py". The server side, "in_progress_window.py", needs to be executed prior to the client side "table_select.window.py". "table_select_window.py" is utilized by the waiter,"in_progress_window.py" is utilized by the kitchen/bar.

## Database ERD
![alt text](https://i.imgur.com/mpezkFr.png)
