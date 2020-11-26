## Canvas data portal to Postgres


This repository has an SQL script (DDL) and a python script that will allow you to migrate the content of canvas data portal to a postgres database quickly and easily.


Inside my repositories there is a script that allows to do the same for MySQL, but unlike this one, the repository for MySQL bases the data loading on bash scripts.


Simply put, postgres is better suited to adapt to hardware and handle large volumes of data compared to MySQL alongside innoDB (I did not test myisam)


#### Requirements:

- Python 3.7.9

- Postgres 13


#### USE:
1) Create a database in postgres

2) Load canvas_data_postgres.sql inside your database

3) Modify the necessary variables within the python file

4) Check the imports of the python file and install the ones you do not have, 
for this you can use pip install PACKAGE_NAME

5) Run the python script files_to_tables.py

6) Go for a coffee and wait for the script to finish


Eventually canvas data portal can update columns or values for ENUMs, if you receive an error message it is likely due to an update by canvas, feel free to modify the SQL file and re-execute all the steps.
